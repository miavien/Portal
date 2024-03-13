from django.shortcuts import render
from datetime import datetime
from django.views.generic import ListView, DetailView
from .models import *
from .filters import PostFilter

class PostsList(ListView):
    model = Post
    ordering = '-date_in'
    template_name = 'flatpages/posts.html'
    context_object_name = 'posts'
    paginate_by = 2

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

class PostDetail(DetailView):
    model = Post
    template_name = 'flatpages/post.html'
    context_object_name = 'post'
    pk_url_kwarg = 'id'