from django.urls import path
from . import views

urlpatterns = [
    path("", views.StartingPageView.as_view(), name="starting-page"),
    path("posts/", views.ListAllPosts.as_view(), name="posts-page"),
    path("posts/<slug:slug>", views.PostDetail.as_view(), name="post-detail-page"),
]