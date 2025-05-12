from django.shortcuts import render
from rest_framework import generics

from django.views.generic import ListView
from .models import Post
from .serializers import PostSerializer

class PostPageView(ListView):
    model = Post
    template_name = "posts.html"

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
