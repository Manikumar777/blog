from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy
# Create your views here.

# ListView ----> To display multiple instances of a table in database
class BlogListView(ListView):
    model = Post
    template_name = "home.html"
# DetailView ----> to display one instance of a table in database
class BlogDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"

class BlogCreateView(CreateView):
    model = Post
    template_name = "post_new.html"
    fields = ['title','author','body','techspecific']

class BlogUpdateView(UpdateView):
    model = Post
    template_name = "post_edit.html"
    fields = ['title','body']

class BlogDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("blog")