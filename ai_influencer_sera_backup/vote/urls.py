from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.vote, name='vote'),
    path('vote/', views.vote, name='vote'),
    path('vote-result/', views.vote_result, name='vote_result'),
]