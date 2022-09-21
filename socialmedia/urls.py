"""socialmedia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from rest_framework import routers

from socialapp import views

router = routers.DefaultRouter()
#Admin
router.register('create-post', views.StoryCreateViewSet, basename='create-post')
router.register('viewlike-dislike', views.ViewLikedPostViewSet, basename='like-dislike')
router.register('story', views.StoryViewSet, basename='story')
#User
router.register('like-dislike', views.LikeDislikeViewSet, basename='like-dislike')
router.register('list-post', views.ListPostViewSet, basename='list-post')
router.register('user-liked-post', views.UserLikedPostViewSet, basename='user-liked-post')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rest/', include('rest_auth.urls')),
    path('api/', include(router.urls)),
]
