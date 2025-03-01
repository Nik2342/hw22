from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blog.models import Blog


class BlogListView(ListView):
    model = Blog

    def get_queryset(self):
        return Blog.objects.filter(is_published = True)


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object

class BlogCreateView(CreateView):
    model = Blog
    fields = ("title", "content")
    success_url = reverse_lazy("blog:blogs_list")

class BlogUpdateView(UpdateView):
    model = Blog
    fields = ("title", "content")
    success_url = reverse_lazy("blog:blogs_list")

    def get_success_url(self):
        return reverse("blog:blog_detail", args = [self.kwargs.get("pk")])

class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy("blog:blogs_list")