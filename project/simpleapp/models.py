from django.db import models
from datetime import datetime
from django.core.validators import MinValueValidator
from django.urls import reverse


class News(models.Model):
    name = models.CharField(
        max_length=128,
        unique=True,
    )
    text = models.TextField()
    amount_of_pages = models.IntegerField(
        validators=[MinValueValidator(0)],
    )

    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='posts'
    )
    date = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return f'{self.name.title()}: {self.text[:20]}'

    def get_absolute_url(self):
        return reverse('news_detail', args=[str(self.id)])


class Category(models.Model):

    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name.title()
