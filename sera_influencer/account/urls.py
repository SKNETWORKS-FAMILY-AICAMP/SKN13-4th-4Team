from django.urls import path, include
from . import views

urlpatterns = [
    path('profile_change/', views.profile_view, name='profile'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
]