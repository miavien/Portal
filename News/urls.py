from django.urls import path
# Импортируем созданные нами представления
from .views import *
from django.views.decorators.cache import cache_page
from django.views.i18n import set_language

urlpatterns = [
   path('news/', cache_page(60)(PostsList.as_view()), name='post_list'),
   path('news/<int:id>', cache_page(300)(PostDetail.as_view()), name='post_detail'),
   path('news/search/', SearchPostsList.as_view(), name='post_search',),
   path('news/create/', PostCreate.as_view(), name='post_create'),
   path('news/<int:pk>/edit/', PostUpdate.as_view(), name='post_update'),
   path('news/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('articles/create/', ArticleCreate.as_view(), name='article_create'),
   path('articles/<int:pk>/edit/', ArticleUpdate.as_view(), name='article_update'),
   path('articles/<int:pk>/delete/', ArticleDelete.as_view(), name='article_delete'),
   path('upgrade/', upgrade_me, name='upgrade'),
   path('news/categories/<int:pk>', CategoryList.as_view(), name='category_list'),
   path('news/categories/<int:pk>/subscribe', subscribe, name='subscribe'),
   path('set-language/', set_language, name='set_language'),
   path('swagger-ui/', TemplateView.as_view(
      template_name='swagger-ui.html',
      extra_context={'schema_url': 'openapi-schema'}
   ), name='swagger-ui'),
]