"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from home import views as home_views
from chat import views as chat_views
from feed import views as feed_views
from vote import views as vote_views
from account import views as account_views





urlpatterns = [
    path('admin/', admin.site.urls),

    # Home app
    path('', home_views.home_view, name="home"),
    # Chat app
    path('chat/', chat_views.chat, name='chat'),
    # Feed app
    path('feed/', feed_views.feed, name='feed'),
    path('feed/like/<int:post_id>/', feed_views.toggle_like, name='toggle_like'),
    path('feed/delete-comment/<int:comment_id>/', feed_views.delete_comment, name='delete_comment'),
    # Vote app
    path('vote/', vote_views.vote, name='vote'),
    # Account app
    path('account/', account_views.profile_view, name='account'),  # account → profile_view
    path('login/', account_views.login_view, name='login'),
    path('signup/', account_views.signup_view, name='signup'),
    path('logout/', account_views.logout_view, name='logout'),
    path('api/check-login/', account_views.check_login_status, name='check_login'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

