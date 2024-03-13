from django.urls import path
# Импортируем созданные нами представления
from .views import PostsList, PostDetail

urlpatterns = [
   path('', PostsList.as_view()),
   path('<int:id>', PostDetail.as_view()),
]