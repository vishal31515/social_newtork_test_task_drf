from django.test import TestCase, Client
from django.contrib.auth.models import User
from rest_framework import status
from .models import Post
from .serializer import PostSerializer
from django.urls import reverse


client = Client()


class GetAllPostTest(TestCase):
    """ Test module for GET all post API """

    def setUp(self):
        user = User.objects.create(username='admin', password="admin@123", first_name="name")
        Post.objects.create(
            user=user,title='Post1', description='post description')
        Post.objects.create(
            user=user,title='Post2', description='post description1')
        
    def test_get_all_post(self):
        response = client.get(reverse('all_post'))
        post = Post.objects.all()
        serializer = PostSerializer(post, many=True)
        self.assertEqual(response.data['data'], serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)