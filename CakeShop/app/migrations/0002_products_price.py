# Generated by Django 5.0.7 on 2024-07-29 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='price',
            field=models.CharField(default='', max_length=30),
        ),
    ]
