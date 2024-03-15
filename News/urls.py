from django.urls import path
# Импортируем созданные нами представления
from .views import *

urlpatterns = [
   path('news/', PostsList.as_view(), name='post_list'),
   path('news/<int:id>', PostDetail.as_view(), name='post_detail'),
   path('news/search/', SearchPostsList.as_view(), name='post_search',),
   path('news/create/', PostCreate.as_view(), name='post_create'),
   path('news/<int:pk>/edit/', PostUpdate.as_view(), name='post_update'),
   path('news/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('articles/create/', ArticleCreate.as_view(), name='article_create'),
   path('articles/<int:pk>/edit/', ArticleUpdate.as_view(), name='article_update'),
   path('articles/<int:pk>/delete/', ArticleDelete.as_view(), name='article_delete'),
]