# Generated by Django 3.2.4 on 2021-11-08 12:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='date',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
        migrations.AddField(
            model_name='product',
            name='total_products',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
