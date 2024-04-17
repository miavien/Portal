from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.core.cache import cache
import pytz

from .models import *
from .filters import *
from .forms import *


class PostDetail(DetailView):
    model = Post
    template_name = 'flatpages/post.html'
    context_object_name = 'post'
    pk_url_kwarg = 'id'

    def get_object(self, *args, **kwargs):
        obj = cache.get(f'post-{self.kwargs['id']}', None)
        if not obj:
            obj = super().get_object(queryset=self.queryset)
            cache.set(f'post-{self.kwargs['id']}', obj)
        return obj


class PostsList(ListView):
    model = Post
    ordering = '-date_in'
    template_name = 'flatpages/posts.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_authors'] = not self.request.user.groups.filter(name='authors').exists()
        context['timezones'] = pytz.common_timezones
        return context

    def post(self, request):
        if 'timezone' in request.POST:
            request.session['django_timezone'] = request.POST['timezone']
        return redirect('post_list')


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


class PostCreate(CreateView, PermissionRequiredMixin):
    form_class = PostForm
    model = Post
    template_name = 'flatpages/post_edit.html'
    permission_required = ('News.add_post',)

    def form_valid(self, form):
        post = form.save(commit=False)
        # post.type = Post.news
        post.save()
        return super().form_valid(form)


class ArticleCreate(CreateView, PermissionRequiredMixin):
    form_class = ArticleForm
    model = Post
    template_name = 'flatpages/article_edit.html'
    permission_required = ('News.add_post',)

    def form_valid(self, form):
        post = form.save(commit=False)
        post.type = Post.articles
        post.save()
        return super().form_valid(form)


class PostUpdate(LoginRequiredMixin, UpdateView, PermissionRequiredMixin):
    form_class = PostForm
    model = Post
    template_name = 'flatpages/post_edit.html'
    permission_required = ('News.change_post',)


class ArticleUpdate(LoginRequiredMixin, UpdateView, PermissionRequiredMixin):
    form_class = ArticleForm
    model = Post
    template_name = 'flatpages/article_edit.html'
    permission_required = ('News.change_post',)


class PostDelete(DeleteView):
    model = Post
    template_name = 'flatpages/post_delete.html'
    success_url = reverse_lazy('post_list')


class ArticleDelete(DeleteView):
    model = Post
    template_name = 'flatpages/article_delete.html'
    success_url = reverse_lazy('post_list')


@login_required
def upgrade_me(request):
    user = request.user
    authors_group = Group.objects.get(name='authors')
    if not request.user.groups.filter(name='authors').exists():
        authors_group.user_set.add(user)
    #при нажатии "стать автором" добавляется в модель Author
    if not Author.objects.filter(user=user).exists():
        Author.objects.create(user=user)
    return redirect('/news/')

class CategoryList(PostsList):
    model = Post
    template_name = 'flatpages/category_list.html'
    context_object_name = 'category_news_list'
    def get_queryset(self):
        self.category = get_object_or_404(Category, id=self.kwargs['pk'])
        queryset = Post.objects.filter(category=self.category).order_by('-date_in')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_subscriber'] = self.request.user not in self.category.subscribers.all()
        context['category'] = self.category
        return context

@login_required
def subscribe(request, pk):
    user = request.user
    category = Category.objects.get(id=pk)
    category.subscribers.add(user)

    message = 'Вы успешно подписались на рассылку новостей категории'
    return render(request, 'flatpages/subscribe.html', {'category' : category, 'message' : message})
