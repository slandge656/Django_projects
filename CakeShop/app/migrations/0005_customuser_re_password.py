# Generated by Django 5.0.7 on 2024-07-30 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_customuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='RE_Password',
            field=models.CharField(default='', max_length=255),
        ),
    ]