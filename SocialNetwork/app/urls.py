from unicodedata import name
from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import UserRegistration, PostView, SingelPostView, LikeDislikeView, AllPost

urlpatterns = [
    path('sign-up', UserRegistration.as_view(), name="signup"),
    
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('post', PostView.as_view(), name="post"),
    path('post/<int:id>', SingelPostView.as_view(), name="singel_post"),
    path('like-dislike', LikeDislikeView.as_view(), name="like_dislike"),
    path('all-post', AllPost.as_view(), name="all_post")
]
