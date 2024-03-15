from django.urls import path
# Импортируем созданные нами представления
from .views import *

urlpatterns = [
   path('', PostsList.as_view()),
   path('<int:id>', PostDetail.as_view(), name='post_detail'),
   path('search/', SearchPostsList.as_view(), name='post_search',),
   path('create/', PostCreate.as_view(), name='post_create')
]