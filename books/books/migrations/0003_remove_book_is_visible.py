# Generated by Django 4.2 on 2023-04-22 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book_group_book_is_visible'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='is_visible',
        ),
    ]
