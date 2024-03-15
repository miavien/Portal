from django import forms
from .models import *
from django.core.exceptions import ValidationError

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

    def clean(self):
        cleaned_data = super().clean()
        text = cleaned_data.get('text')
        title_of_news = cleaned_data.get('title_of_news')

        if title_of_news == text:
            raise ValidationError('Текст новости не должен быть индентичным названию')

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

    def clean(self):
        cleaned_data = super().clean()
        text = cleaned_data.get('text')
        title_of_news = cleaned_data.get('title_of_news')

        if title_of_news == text:
            raise ValidationError('Текст статьи не должен быть индентичным названию')

        return cleaned_data