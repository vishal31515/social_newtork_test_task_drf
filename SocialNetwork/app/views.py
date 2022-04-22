import re
from urllib import response
from django.shortcuts import render

from rest_framework.views import APIView
from .serializer import RegisterSerializer, FavoritePostSerializer, PostSerializer, GetPostSerializer
from django.contrib.auth.models import User
from rest_framework import status
from response_messages.status_messages import response_status
from rest_framework.response import Response
from .models import Post, FavoritePost
from rest_framework.permissions import IsAuthenticated


class UserRegistration(APIView):
    
    def post(self, request):
        response = {}
        try:
            signup_serializer = RegisterSerializer(data=request.data)
            if signup_serializer.is_valid():
                signup_serializer.save()
                response["status"] = status.HTTP_201_CREATED
                response["message"] = response_status.USER_CREATED
            else:
                response["status"] = status.HTTP_400_BAD_REQUEST
                response["message"] = signup_serializer.errors
        except Exception as e:
            response["status"] = status.HTTP_400_BAD_REQUEST
            response["message"] = str(e)
        return Response(response)
    

class AllPost(APIView):
    
    def get(self, request):
        response = {}
        try:
            posts = Post.objects.all()
            serializer = GetPostSerializer(posts, many=True)
            response["status"] = status.HTTP_200_OK
            response["data"] = serializer.data
        except Exception as e:
            response["status"] = status.HTTP_400_BAD_REQUEST
            response["data"] = []
            response['error'] = str(e)
        return Response(response)

    

class PostView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        response = {}
        try:
            posts = Post.objects.all()
            serializer = GetPostSerializer(posts, many=True)
            response["status"] = status.HTTP_200_OK
            response["data"] = serializer.data
        except Exception as e:
            response["status"] = status.HTTP_400_BAD_REQUEST
            response["data"] = []
            response['error'] = str(e)
        return Response(response)
            
    def post(self, request):
        response = {}
        try:
            serializer = PostSerializer(
                data=request.data, context={"request": request}
            )
            if serializer.is_valid():
                serializer.save()
                response["status"] = status.HTTP_201_CREATED
                response["data"] = serializer.data
            else:
                response["status"] = status.HTTP_400_BAD_REQUEST
                response["error"] = serializer.errors    
        except Exception as e:
            response["status"] = status.HTTP_400_BAD_REQUEST
            response['error'] = str(e)
        return Response(response)
            
            
class SingelPostView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get_object(self, id):
        try:
            post_obj = Post.objects.get(id=id)
            return post_obj
        except:
            return False
        
    def get(self, request, id):
        response = {}
        try:
            obj = self.get_object(id)
            if obj:
                serializer = PostSerializer(obj)
                response["status"] = status.HTTP_200_OK
                response["data"] = serializer.data
            else:
                response["status"] = status.HTTP_400_BAD_REQUEST
                response["error"] = "Post not found"
        except Exception as e:
            response["status"] = status.HTTP_400_BAD_REQUEST
            response['error'] = str(e)
        return Response(response)
       
            
    def put(self, request, id):
        response = {}
        try:
            obj = self.get_object(id)
            request.data.update({"user": request.user.id})
            if obj:
                serializer = PostSerializer(data=request.data, partial=True)
                
                if serializer.is_valid():
                    serializer.save()
                    response["status"] = status.HTTP_200_OK
                    response["data"] = serializer.data
                else:
                    response["status"] = status.HTTP_400_BAD_REQUEST
                    response["error"] = serializer.errors
            else:
                response["status"] = status.HTTP_400_BAD_REQUEST
                response["error"] = "NO Post found"
        except Exception as e:
            response["status"] = status.HTTP_400_BAD_REQUEST
            response['error'] = str(e)
        return Response(response)
       
        
    def delete(self, request, id):
        response = {}
        try:
            obj = self.get_object(id)
            if obj:
                obj.delete()
                response["status"] = status.HTTP_200_OK
                response["data"] = "Post succesfully deleted"
            else:
                response["status"] = status.HTTP_400_BAD_REQUEST
                response["error"] = "Post not found"
        except Exception as e:
            response["status"] = status.HTTP_400_BAD_REQUEST
            response['error'] = str(e)
        return Response(response)
        
        
        
class LikeDislikeView(APIView):
    
    def get(self, request):
        response = {}
        try:
            posts = FavoritePost.objects.filter(user=request.user)
            serializer = FavoritePostSerializer(posts, many=True)
            response["status"] = status.HTTP_200_OK
            response["data"] = serializer.data
        except Exception as e:
            response["status"] = status.HTTP_400_BAD_REQUEST
            response["data"] = []
            response['error'] = str(e)
        return Response(response)
    
    def post(self, request):
        response = {}
        try:
            request.data._mutable = True
            request.data.update({"user": request.user.id})
            serializer = FavoritePostSerializer(data=request.data, context={"request": request})
            if serializer.is_valid():
                obj = serializer.save()
                if obj == True:
                    response["status"] = status.HTTP_200_OK
                    response["message"] = "Post succesfully Dislike"
                else:
                    response["status"] = status.HTTP_200_OK
                    response["data"] = serializer.data
            else:
                response["status"] = status.HTTP_400_BAD_REQUEST
                response["error"] = serializer.errors
        except Exception as e:
            response["status"] = status.HTTP_400_BAD_REQUEST
            response['error'] = str(e)
        return Response(response)