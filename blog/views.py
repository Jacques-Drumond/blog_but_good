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

        stored_posts = request.session.get("stored_posts")

        if stored_posts is not None:
            is_saved_for_later = post.id in stored_posts # type: ignore
        else:
            is_saved_for_later = False

        comments = post.comments.all().order_by("-id") # type: ignore
        if comments is None or len(comments) == 0:
            has_comments = False
        else:
            has_comments = True
        context = {
            "post": post,
            "post_tags": post.tags.all(),
            'comment_form': CommentForm(),
            "comments": comments, # type: ignore
            "has_comments": has_comments,
            "is_saved_for_later": is_saved_for_later
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
                "comments": post.comments.all().order_by("-id") # type: ignore
            }
            return render(request, "blog/post_detail.html", context)


class ReadLaterView(View):

    def get(self, request):
        stored_posts = request.session.get("stored_posts")

        context = {}

        if stored_posts is None or len(stored_posts) == 0:
            context["posts"] = []
            context["has_posts"] = False
        else:
            posts = Post.objects.filter(id__in=stored_posts)
            context["posts"] = posts
            context["has_posts"] = True
        
        return render(request, "blog/stored_posts.html", context)

    def post(self, request):
        stored_posts = request.session.get("stored_posts")

        if stored_posts is None:
            stored_posts = []

        post_id = int(request.POST['post_id'])

        if post_id not in stored_posts:
            stored_posts.append(post_id)
        
        else:
            print("removido do read later")
            stored_posts.remove(post_id)

        request.session["stored_posts"] = stored_posts

        return HttpResponseRedirect("/")