# Generated by Django 4.2.3 on 2023-07-17 06:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simpleapp', '0004_alter_news_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 17, 15, 15, 27, 505157)),
        ),
    ]