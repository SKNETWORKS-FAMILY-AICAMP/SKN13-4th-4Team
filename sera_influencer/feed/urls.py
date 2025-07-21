from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.feed, name='feed'),
    path('delete-comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
]