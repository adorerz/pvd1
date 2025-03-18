# main/urls.py

from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('dashboard/', views.dashboard, name='dashboard'),

    # Creating, editing, deleting, printing, analyzing SpiritualRecords
    path('record/', views.record, name='record'),
    path('edit/<int:record_id>/', views.edit_record, name='edit_record'),
    path('delete/<int:pk>/', views.delete_record, name='delete_record'),
    path('print/<int:pk>/', views.print_record, name='print_record'),
    path('analyze/<int:pk>/', views.analyze_record, name='analyze_record'),
    path('interpret/<int:record_id>/', views.interpret_record, name='interpret_record'),

    # Sharing SpiritualRecords
    path('toggle-community-sharing/<int:record_id>/', views.toggle_community_sharing, name='toggle_community_sharing'),

    # Profile
    path('profile/', views.profile, name='profile'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),

    # Community
    path('community/', views.community, name='community'),

    # Likes
    path('like-community-post/<int:post_id>/', views.like_community_post, name='like_community_post'),
    path('like-record/<int:record_id>/', views.like_record, name='like_record'),

    # Comments & Interpretations
    path('post-record-interpretation/<int:record_id>/', views.post_record_interpretation, name='post_record_interpretation'),
    path('post-record-comment/<int:record_id>/', views.post_record_comment, name='post_record_comment'),
    path('post-community-comment/<int:post_id>/', views.post_community_comment, name='post_community_comment'),
]
