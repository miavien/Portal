# Generated by Django 5.0.3 on 2024-03-15 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0002_alter_post_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='type',
            field=models.CharField(choices=[('NW', 'Новость'), ('AR', 'Статья')], default='NW', max_length=2),
        ),
    ]
