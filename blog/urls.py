from django.urls import path, include
from blog.apps import BlogConfig
from blog.views import (
    BlogListView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
)

app_name = BlogConfig.name


urlpatterns = [
    path("blogs_list/", BlogListView.as_view(), name="blogs_list"),
    path("blogs/<int:pk>", BlogDetailView.as_view(), name="blog_detail"),
    path("blogs/create", BlogCreateView.as_view(), name="blog_create"),
    path("blogs/<int:pk>/update", BlogUpdateView.as_view(), name="blog_update"),
    path("blogs/<int:pk>/delete", BlogDeleteView.as_view(), name="blog_delete"),
]
