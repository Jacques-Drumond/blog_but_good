from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from .models import Post,Author,Tag
from django.views.generic import ListView
from django.urls import reverse
from django.views import View
from django.http import HttpResponseRedirect
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

    def get(self, request, slug):
    
        post = Post.objects.get(slug=slug)
        context = {
            "post": post,
            "post_tags": post.tags.all(),
            'comment_form': CommentForm(),
            "comments": post.comments.all().order_by("-id")
        }
        return render(request, "blog/post_detail.html", context)

    def post(self, request, slug):
        post = Post.objects.get(slug=slug)
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse("post-detail-page", args=[slug]))
        
        else:
            context = {
                "post": post,
                "post_tags": post.tags.all(),
                'comment_form': comment_form,
                "comments": post.comments.all().order_by("-id")
            }
            return render(request, "blog/post_detail.html", context)