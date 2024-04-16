from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['user', 'rating']
    list_filter = ['user', 'rating']

class PostAdmin(admin.ModelAdmin):
    list_display = ['author', 'title_of_news', 'rating', 'get_categories']
    list_filter = ['author', 'title_of_news', 'rating', 'category__name_category']

    def get_categories(self, obj):
        return ", ".join([category.name_category for category in obj.category.all()])

    get_categories.short_description = 'Categories'

class PostTransAdmin(PostAdmin, TranslationAdmin):
    model = Post

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name_category']
    list_filter = ['name_category']

class CategoryTransAdmin(CategoryAdmin, TranslationAdmin):
    model = Category

class PostCategoryAdmin(admin.ModelAdmin):
    list_display = ['get_post_title', 'get_category_name']
    list_filter = ['post__title_of_news', 'category__name_category']

    def get_post_title(self, obj):
        return obj.post.title_of_news

    def get_category_name(self, obj):
        return obj.category.name_category

class CommentAdmin(admin.ModelAdmin):
    list_display = ['get_post', 'get_user', 'text']
    list_filter = ['post__title_of_news', 'user', 'text']

    def get_post(self, obj):
        return obj.post.title_of_news

    def get_user(self, obj):
        return obj.user.username


# Register your models here.
admin.site.register(Post, PostTransAdmin)
admin.site.register(Category, CategoryTransAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(PostCategory, PostCategoryAdmin)
