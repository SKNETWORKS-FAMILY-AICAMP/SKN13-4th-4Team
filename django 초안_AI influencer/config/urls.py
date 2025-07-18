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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from core import views as core_views
from my_influencer import views as influencer_views


urlpatterns = [
    path('admin/', admin.site.urls),
    # Core 앱 - 홈페이지, 프로필, 인증
    path("", core_views.home, name="home"),
    path('profile/', core_views.profile_view, name='profile'),
    path('login/', core_views.login_view, name='login'),
    path('signup/', core_views.signup_view, name='signup'),
    path('logout/', core_views.logout_view, name='logout'),
    path('vote/', core_views.vote_view, name='vote'),
    path('api/check-login/', core_views.check_login_status, name='check_login'),

    # My_influencer 앱 - AI 기능과 콘텐츠
    path("chat/", influencer_views.chat, name="chat"),
    path("feed/", influencer_views.feed, name="feed"),
    path("products/", influencer_views.products, name="products"),
    path("delete-comment/<int:comment_id>/", influencer_views.delete_comment, name="delete_comment"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


