# main/admin.py

from django.contrib import admin
from .models import (
    User,
    SpiritualRecord,
    RecordComment,
    RecordInterpretation,
    CommunityPost,
    CommunityComment
)

# 1) Register the User model
admin.site.register(User)


# 2) Inlines for SpiritualRecord (comments & interpretations)
class RecordCommentInline(admin.TabularInline):
    model = RecordComment
    extra = 1  # Display one blank comment form by default


class RecordInterpretationInline(admin.TabularInline):
    model = RecordInterpretation
    extra = 1  # Display one blank interpretation form by default


@admin.register(SpiritualRecord)
class SpiritualRecordAdmin(admin.ModelAdmin):
    """
    Admin for SpiritualRecord model (dreams, visions, prophecies).
    Includes:
    - List of shared vs. unshared
    - Inline comments & interpretations
    - Search by username or text content
    - Filter by record_type, date, shared status
    """
    list_display = ('id', 'record_type', 'user', 'is_shared', 'likes', 'created_at')
    list_filter = ('record_type', 'is_shared', 'created_at')
    search_fields = ('user__username', 'text')
    inlines = [RecordCommentInline, RecordInterpretationInline]


# 3) Inlines for CommunityPost (comments only)
class CommunityCommentInline(admin.TabularInline):
    model = CommunityComment
    extra = 1  # Display one blank comment form by default


@admin.register(CommunityPost)
class CommunityPostAdmin(admin.ModelAdmin):
    """
    Admin for CommunityPost model.
    Allows admin to see, edit, delete or moderate posts
    and their comments in one place.
    """
    list_display = ('id', 'title', 'user', 'likes', 'created_at')
    list_filter = ('created_at', )
    search_fields = ('title', 'content', 'user__username')
    inlines = [CommunityCommentInline]
