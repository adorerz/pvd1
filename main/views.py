# main/views.py

import json
import re
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.views.decorators.csrf import csrf_exempt

from .models import (
    User,
    SpiritualRecord,
    UserProfile,
    RecordComment,
    RecordInterpretation,
    CommunityPost,
    CommunityComment
)
from .forms import SpiritualRecordForm, SignupForm
from .services.interpretation import interpret_text
from weasyprint import HTML


def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


@login_required
def dashboard(request):
    records = SpiritualRecord.objects.filter(user=request.user)
    total_shared_records = SpiritualRecord.objects.filter(is_shared=True).count()
    total_users = User.objects.count()

    return render(request, "dashboard.html", {
        "records": records,
        "total_shared_records": total_shared_records,
        "total_users": total_users,
    })


@login_required
def record(request):
    """
    Create a SpiritualRecord (dream/vision/prophecy).
    Can handle both text and audio submissions.
    """
    if request.method == 'POST':
        # Check if this is an audio upload or text submission
        if 'audio_name' in request.POST or 'audio' in request.FILES:
            audio_form = SpiritualRecordForm(request.POST, request.FILES)
            if audio_form.is_valid():
                rec = audio_form.save(commit=False)
                rec.user = request.user
                rec.save()
                messages.success(request, 'Your recording has been saved successfully.')
                return redirect('dashboard')
            else:
                messages.error(request, 'Error saving your recording. Please try again.')
        else:
            text_form = SpiritualRecordForm(request.POST)
            if text_form.is_valid():
                rec = text_form.save(commit=False)
                rec.user = request.user
                rec.save()
                messages.success(request, 'Your text entry has been saved successfully.')
                return redirect('dashboard')
            else:
                messages.error(request, 'Error saving your text entry. Please try again.')
    else:
        text_form = SpiritualRecordForm()
        audio_form = SpiritualRecordForm()

    return render(request, 'record.html', {
        'text_form': text_form,
        'audio_form': audio_form,
    })


@login_required
def edit_record(request, record_id):
    rec = get_object_or_404(SpiritualRecord, id=record_id, user=request.user)

    if request.method == "POST":
        form = SpiritualRecordForm(request.POST, request.FILES, instance=rec)
        if form.is_valid():
            updated_record = form.save(commit=False)
            # If the user checks "is_shared," it's set
            updated_record.is_shared = "is_shared" in request.POST
            updated_record.save()
            messages.success(request, 'Record updated successfully.')
            return redirect("dashboard")
    else:
        form = SpiritualRecordForm(instance=rec)

    return render(request, "edit_record.html", {"form": form})


@login_required
def delete_record(request, pk):
    rec = get_object_or_404(SpiritualRecord, pk=pk, user=request.user)
    rec.delete()
    messages.success(request, 'The record has been deleted successfully.')
    return redirect('dashboard')


@login_required
def print_record(request, pk):
    rec = get_object_or_404(SpiritualRecord, pk=pk, user=request.user)
    html_string = render_to_string('print_record.html', {'record': rec})
    html = HTML(string=html_string)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename=record_{rec.pk}.pdf'
    html.write_pdf(response)
    return response


@login_required
def analyze_record(request, pk):
    """
    Analyzes the text of the SpiritualRecord for word count, 
    symbolic interpretation, etc.
    """
    rec = get_object_or_404(SpiritualRecord, pk=pk, user=request.user)

    if rec.text:
        text = rec.text
        word_count = len(text.split())
        character_count = len(text)
        sentence_count = text.count('.') + text.count('!') + text.count('?')
        
        # Attempt a symbolic interpretation
        interpretation = interpret_text(text)

        # Simple positivity/negativity measure
        positive_words = {"light", "joy", "angel", "blessing", "peace", "gold", "victory"}
        negative_words = {"darkness", "storm", "fear", "serpent", "danger", "warning"}

        positive_matches = sum(1 for w in text.lower().split() if w in positive_words)
        negative_matches = sum(1 for w in text.lower().split() if w in negative_words)

        if positive_matches > negative_matches:
            emotional_tone = "Uplifting and Encouraging 🌟"
        elif negative_matches > positive_matches:
            emotional_tone = "Warning or Cautionary ⚠️"
        else:
            emotional_tone = "Neutral or Reflective 🤔"

        # Find top 3 frequent words (excluding common filler words)
        words = re.findall(r'\b\w+\b', text.lower())
        word_frequencies = {}
        for w in words:
            word_frequencies[w] = word_frequencies.get(w, 0) + 1

        common_words = {"the", "and", "of", "to", "a", "in", "it", "is", "i", "that", "with"}
        filtered = [(w, c) for w, c in word_frequencies.items() if w not in common_words]
        frequent_words = sorted(filtered, key=lambda x: x[1], reverse=True)[:3]
        if frequent_words:
            frequent_words_str = ", ".join([f"{w} ({c} times)" for w, c in frequent_words])
        else:
            frequent_words_str = "No significant repetition."

        analysis = {
            'word_count': word_count,
            'character_count': character_count,
            'sentence_count': sentence_count,
            'text_preview': (text[:150] + '...') if len(text) > 150 else text,
            'interpretation': interpretation,
            'emotional_tone': emotional_tone,
            'frequent_words': frequent_words_str
        }
    else:
        analysis = None

    return render(request, 'analyze_record.html', {'record': rec, 'analysis': analysis})


@login_required
def interpret_record(request, record_id):
    """
    Show a symbolic dictionary interpretation for the record text.
    """
    rec = get_object_or_404(SpiritualRecord, id=record_id, user=request.user)
    text_to_interpret = rec.text if rec.text else ""
    interpretation_data = interpret_text(text_to_interpret)

    structured_interpretation = []
    for symbol, details in interpretation_data.items():
        structured_interpretation.append({
            "symbol": symbol.title(),
            "meaning": details["meaning"],
            "scripture": details["scripture"]
        })

    return render(request, "interpret_record.html", {
        "record": rec,
        "interpretation": structured_interpretation
    })


@login_required
@csrf_exempt
def toggle_community_sharing(request, record_id):
    """
    Toggle whether a SpiritualRecord is shared publicly in the community.
    """
    if request.method == "POST":
        rec = get_object_or_404(SpiritualRecord, id=record_id, user=request.user)
        try:
            data = json.loads(request.body)
            is_shared = data.get("is_shared", False)
            rec.is_shared = is_shared
            rec.save()
            return JsonResponse({"status": "success", "is_shared": rec.is_shared})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=400)

    return JsonResponse({"status": "error", "message": "Invalid request"}, status=400)


@login_required
def profile(request):
    # Typically you'd load a ProfileForm to edit user.profile
    # or user details. Simplified here:
    return render(request, 'profile.html')


@login_required
def edit_profile(request):
    # Handle editing the user or user.profile as needed
    messages.info(request, "Profile update not implemented in this example.")
    return redirect("profile")


@login_required
def community(request):
    """
    Community hub. Displays:
    - A form to create a new CommunityPost
    - List of CommunityPosts
    - List of shared SpiritualRecords
    """
    if request.method == 'POST':
        # Creating a new community post
        title = request.POST.get('title', '').strip()
        content = request.POST.get('content', '').strip()
        if title and content:
            CommunityPost.objects.create(user=request.user, title=title, content=content)
            messages.success(request, 'Community post created successfully.')
            return redirect('community')

    # Display data
    community_posts = CommunityPost.objects.order_by('-created_at')
    shared_records = SpiritualRecord.objects.filter(is_shared=True).order_by("-created_at")

    total_shared = shared_records.count()
    active_users = (
        SpiritualRecord.objects.filter(is_shared=True)
        .values("user")
        .distinct()
        .count()
    )

    return render(request, "community.html", {
        "community_posts": community_posts,
        "shared_records": shared_records,
        "total_shared": total_shared,
        "active_users": active_users,
    })


@login_required
@csrf_exempt
def like_community_post(request, post_id):
    """
    Increment 'likes' for a CommunityPost.
    """
    if request.method == 'POST':
        post = get_object_or_404(CommunityPost, id=post_id)
        post.likes += 1
        post.save()
        return JsonResponse({'success': True, 'likes': post.likes})
    return JsonResponse({'success': False, 'error': 'Invalid request'}, status=400)


@login_required
@csrf_exempt
def like_record(request, record_id):
    if request.method == 'POST':
        rec = get_object_or_404(SpiritualRecord, id=record_id)
        if not rec.is_shared:
            return JsonResponse({'success': False, 'error': 'Record not shared'}, status=400)
        rec.likes += 1
        rec.save()
        return JsonResponse({'success': True, 'likes': rec.likes})
    return JsonResponse({'success': False, 'error': 'Invalid request'}, status=400)



@login_required
@csrf_exempt
def post_record_interpretation(request, record_id):
    """
    Post a new interpretation on a SHARED SpiritualRecord.
    """
    if request.method == 'POST':
        rec = get_object_or_404(SpiritualRecord, id=record_id, is_shared=True)
        content = request.POST.get('interpretation', '').strip()
        if content:
            interpretation = RecordInterpretation.objects.create(
                user=request.user,
                record=rec,
                content=content
            )
            return JsonResponse({
                "success": True,
                "username": request.user.username,
                "content": interpretation.content,
                "date": interpretation.created_at.strftime("%b %d, %Y %H:%M")
            })
        else:
            return JsonResponse({"success": False, "error": "Empty interpretation."})
    return JsonResponse({"success": False, "error": "Invalid request"})


@login_required
@csrf_exempt
def post_record_comment(request, record_id):
    """
    Post a new comment on a SHARED SpiritualRecord.
    """
    if request.method == 'POST':
        rec = get_object_or_404(SpiritualRecord, id=record_id, is_shared=True)
        content = request.POST.get('comment', '').strip()
        if content:
            comment = RecordComment.objects.create(
                user=request.user,
                record=rec,
                content=content
            )
            return JsonResponse({
                "success": True,
                "username": request.user.username,
                "content": comment.content,
                "date": comment.created_at.strftime('%b %d, %Y %H:%M')
            })
        else:
            return JsonResponse({"success": False, "error": "Empty comment."})
    return JsonResponse({'success': False, 'error': 'Invalid request method.'})


@login_required
@csrf_exempt
def post_community_comment(request, post_id):
    """
    Post a new comment on a CommunityPost.
    """
    if request.method == 'POST':
        post = get_object_or_404(CommunityPost, id=post_id)
        content = request.POST.get('comment', '').strip()
        if content:
            comment = CommunityComment.objects.create(
                user=request.user,
                post=post,
                content=content
            )
            return JsonResponse({
                "success": True,
                "username": request.user.username,
                "content": comment.content,
                "date": comment.created_at.strftime('%b %d, %Y %H:%M')
            })
        else:
            return JsonResponse({"success": False, "error": "Empty comment."})
    return JsonResponse({'success': False, 'error': 'Invalid request method.'})
