from .models import *
from modeltranslation.translator import register, TranslationOptions  # импортируем декоратор для перевода и класс настроек, от которого будем наследоваться

# регистрируем наши модели для перевода

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name_category',)  # указываем, какие именно поля надо переводить в виде кортежа


@register(Post)
class PostTranslationOptions(TranslationOptions):
    fields = ('title_of_news', 'text',)