from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from News import views

router = routers.DefaultRouter()
router.register(r'authors', views.AuthorViewset)
router.register(r'categorys', views.CategoryViewset)
router.register(r'posts', views.PostViewset)

urlpatterns = [
   path('admin/', admin.site.urls),
   path('pages/', include('django.contrib.flatpages.urls')),
   path('', include('News.urls')),
   path('sign/', include('sign.urls')),
   path('accounts/', include('allauth.urls')),
   path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
