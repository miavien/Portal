from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from News.views import *
from .yasg import urlpatterns as doc_urls


router = routers.DefaultRouter()
router.register(r'users', AuthorViewset, basename='authors')
router.register(r'categories', CategoryViewset, basename='category')
router.register(r'posts', PostViewset, basename='posts')

urlpatterns = [
   path('admin/', admin.site.urls),
   path('pages/', include('django.contrib.flatpages.urls')),
   path('', include('News.urls')),
   path('sign/', include('sign.urls')),
   path('accounts/', include('allauth.urls')),
   path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
   path('api/', include(router.urls)),
]

urlpatterns += doc_urls