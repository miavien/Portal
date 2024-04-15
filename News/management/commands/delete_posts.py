from django.core.management.base import BaseCommand, CommandError
from News.models import *

class Command(BaseCommand):
    # показывает подсказку при вводе "python manage.py <ваша команда> --help"
    help = 'Удаляет все посты из категории'
    """ Напоминать ли о миграциях. Если true — то будет напоминание о том, 
    что не сделаны все миграции (если такие есть)"""
    requires_migrations_checks = True

    def add_arguments(self, parser):
        parser.add_argument('category', type=str)

    def handle(self, *args, **options):
        answer = input(f'Вы правда хотите удалить все статьи в категории {options["category"]}? yes/no')

        if answer != 'yes':
            self.stdout.write(self.style.ERROR('Отменено'))
            return
        try:
            category = Category.objects.get(name_category=options['category'])
            Post.objects.filter(category=category).delete()
            self.stdout.write(self.style.SUCCESS(f'Все посты в категории {category.name_category} удалены'))
        except Post.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Невозможно найти категорию'))