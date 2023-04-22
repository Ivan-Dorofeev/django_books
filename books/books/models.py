from django.db import models


class BookGroupChoise(models.TextChoices):
    DETECTIVE = 'Детектив'
    ROMAN = 'Роман'


class Book(models.Model):
    group = models.CharField('Литературная группа', max_length=10, choices=BookGroupChoise.choices, blank=True)
    title = models.CharField('Название', max_length=30, blank=True, null=True)
    author = models.CharField('Автор', max_length=30, blank=True, null=True)
    description = models.CharField('Описание', max_length=512, blank=True, null=True)
    price = models.IntegerField('Цена', blank=True, null=True)

    class Meta:
        db_table = 'books'

    def __str__(self):
        return f'{self.title} - {self.author}'
