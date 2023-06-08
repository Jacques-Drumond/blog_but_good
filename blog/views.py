from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from .models import Post,Author,Tag
# Create your views here.


def starting_page(request):
    latest_posts = Post.objects.order_by('-date')[:3]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })

def posts(request):
    all_posts = Post.objects.order_by('-date')
    return render(request, "blog/all_posts.html", {
        "posts": all_posts
    })

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    author = post.author
    tag = post.tags
    print(tag)
    return render(request, "blog/post_detail.html", {
        "post": post,
        "tags": post.tags.all()
    })
