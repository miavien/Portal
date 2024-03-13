from django_filters import FilterSet
from .models import Post

class PostFilter(FilterSet):
    class Meta:
        model = Post
        fields = {
            'title_of_news': ['icontains'],
            'author__user__username': ['icontains'],
            'date_in': ['gt']
        }