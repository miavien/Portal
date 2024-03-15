from django_filters import FilterSet, ModelChoiceFilter, DateFilter
from django.forms import DateInput
from .models import *

class PostFilter(FilterSet):
    category = ModelChoiceFilter(
        field_name='postcategory__category',
        queryset=Category.objects.all(),
        label='Категория',
    )

    date_in = DateFilter(
        field_name='date_in',
        widget=DateInput(attrs={'type': 'date'}),
        label='Дата',
        lookup_expr='date__gt',
    )
    class Meta:
        model = Post
        fields = {
            'title_of_news': ['icontains'],
            'author__user__username': ['icontains'],
        }

