from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django_filters.views import FilterView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import *
from .filters import *
from .forms import *

class PostDetail(DetailView):
    model = Post
    template_name = 'flatpages/post.html'
    context_object_name = 'post'
    pk_url_kwarg = 'id'

class PostsList(ListView):
    model = Post
    ordering = '-date_in'
    template_name = 'flatpages/posts.html'
    context_object_name = 'posts'
    paginate_by = 10

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     self.filterset = PostFilter(self.request.GET, queryset)
    #     return self.filterset.qs
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['filterset'] = self.filterset
    #     return context

class SearchPostsList(ListView):
    model = Post
    ordering = '-date_in'
    template_name = 'flatpages/search.html'
    context_object_name = 'search'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

class PostCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'flatpages/post_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.type = Post.news
        post.save()
        return redirect('post_detail', id=post.pk)

class ArticleCreate(CreateView):
    form_class = ArticleForm
    model = Post
    template_name = 'flatpages/article_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.type = Post.articles
        post.save()
        return redirect('post_detail', id=post.pk)

class PostUpdate(LoginRequiredMixin ,UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'flatpages/post_edit.html'

class ArticleUpdate(LoginRequiredMixin, UpdateView):
    form_class = ArticleForm
    model = Post
    template_name = 'flatpages/article_edit.html'

class PostDelete(DeleteView):
    model = Post
    template_name = 'flatpages/post_delete.html'
    success_url = reverse_lazy('post_list')

class ArticleDelete(DeleteView):
    model = Post
    template_name = 'flatpages/article_delete.html'
    success_url = reverse_lazy('post_list')