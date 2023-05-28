from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from datetime import date
from .models import BlogPost
# Create your views here.


def starting_page(request):
    latest_posts = BlogPost.objects.order_by('-date')[:3]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })

def posts(request):
    all_posts = BlogPost.objects.all()
    return render(request, "blog/all_posts.html", {
        "posts": all_posts
    })

def post_detail(request, slug):
    try:
        post = BlogPost.objects.get(slug=slug)
        return render(request, "blog/post_detail.html", {
            "post": post
        })
    except BlogPost.DoesNotExist:
        return render(request, "404.html")