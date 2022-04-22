from dataclasses import fields
from doctest import Example
from operator import imod
from pyexpat import model
from rest_framework import  serializers
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .utils import  CustomException
from .models import Post, FavoritePost


# Register serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','password','first_name', 'last_name','email')
        extra_kwargs = {
            'password':{'write_only': True},
        }
        
    def create(self, validated_data):
        try:
            user = User.objects.create_user(username=validated_data['username'], email=validated_data['email'], password = validated_data['password'],first_name=validated_data['first_name'], last_name=validated_data['last_name'])
            return user
        except Exception as e:
            raise CustomException(str(e))


class GetPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title','description','image']

    def create(self, validated_data):
        try:
            user = self.context["request"].user
            validated_data.update({'user':user})
            post = Post.objects.create(**validated_data)
            return post
        except Exception as e:
            raise CustomException(str(e))
        
        
class FavoritePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoritePost
        exclude = ('is_liked', )

        
    def create(self, validated_data):
        user = self.context["request"].user
        try:
            favorite_obj = FavoritePost.objects.get(post=validated_data['post'], user=user)
            if favorite_obj.is_liked == True:
                favorite_obj.delete()
                return True
        except FavoritePost.DoesNotExist:
            obj = FavoritePost.objects.create(post=validated_data['post'],user=user,is_liked=True)
            return obj
        except Exception as e:
            raise CustomException(str(e))
        