from django.shortcuts import render
from django.views.generic import CreateView, ListView
from .models import Blog
from django.urls import reverse_lazy


class BlogListView(ListView):
    model = Blog


class BlogCreateView(CreateView):
    model = Blog
    fields = "__all__"
    success_url = reverse_lazy("Blog:list")
