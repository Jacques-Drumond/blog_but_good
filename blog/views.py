from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from .models import Post,Author,Tag
from django.views.generic import ListView, 
from django.views import View
# Create your views here.
from .forms import CommentForm

class StartingPageView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"
    def get_queryset(self):
        query = super().get_queryset()
        data = query[:3]
        return data


class ListAllPosts(ListView):
    template_name = "blog/all_posts.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"
    def get_queryset(self):
        query = super().get_queryset()
        return query


class PostDetail(View):
    template_name = "blog/post_detail.html"
    model = Post

    def get():
    
    def post():


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tags"] = self.object.tags.all()
        context["comment_form"] = CommentForm()
        return context