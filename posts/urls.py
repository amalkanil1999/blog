from django.urls import path
from posts.views import create_posts,my_posts,delete_posts,draft_posts,edit_posts


app_name="posts"

urlpatterns = [
    path("create/",create_posts,name='create_posts'),
    path("my_posts/",my_posts,name='my_posts'),
    path("delete/<int:id>/",delete_posts,name="delete_posts"),
    path("draft/<int:id>/",draft_posts,name="draft_posts"),
    path("edit/<int:id>/",edit_posts,name="edit_posts"),
]
