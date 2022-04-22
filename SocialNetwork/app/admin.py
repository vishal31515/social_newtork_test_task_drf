from django.contrib import admin
from .models import Post, FavoritePost

admin.site.register(Post)
admin.site.register(FavoritePost)