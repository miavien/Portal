from django import forms
from .models import *
from django.core.exceptions import ValidationError
import datetime

class PostForm(forms.ModelForm):
    text = forms.CharField(min_length=20)

    class Meta:
        model = Post
        fields = [
            'category',
            'title_of_news',
            'text',
            'author',
        ]

    def clean_text(self):
        text = self.cleaned_data.get('text')
        title_of_news = self.cleaned_data.get('title_of_news')

        if title_of_news == text:
            raise ValidationError('Текст статьи не должен быть индентичным названию')

        return text

    def clean(self):
        cleaned_data = super().clean()
        author = cleaned_data.get('author')
        today = datetime.date.today()
        posts_limit = Post.objects.filter(author=author, date_in__date=today).count()
        if posts_limit > 10:
            raise ValidationError('Превышено максимальное количество постов в день!')
        return cleaned_data

class ArticleForm(forms.ModelForm):
    text = forms.CharField(min_length=20)

    class Meta:
        model = Post
        fields = [
            'category',
            'title_of_news',
            'text',
            'author',
        ]

    def clean_text(self):
        text = self.cleaned_data.get('text')
        title_of_news = self.cleaned_data.get('title_of_news')

        if title_of_news == text:
            raise ValidationError('Текст статьи не должен быть индентичным названию')

        return text

    def clean(self):
        cleaned_data = super().clean()
        author = cleaned_data.get('author')
        today = datetime.date.today()
        posts_limit = Post.objects.filter(author=author, date_in__date=today).count()
        if posts_limit > 10:
            raise ValidationError('Превышено максимальное количество постов в день!')
        return cleaned_data