from .models import *
from rest_framework import serializers

class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    user_email = serializers.EmailField(source='user.email', read_only=True)
    user_name = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Author
        fields = ['id', 'user_name', 'user_email',]

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name_category',]

class PostSerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), many=True
    )

    class Meta:
        model = Post
        fields = ['id', 'type', 'date_in', 'category', 'title_of_news', 'text']