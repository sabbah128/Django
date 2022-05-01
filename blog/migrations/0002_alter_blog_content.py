# Generated by Django 3.2.13 on 2022-04-23 16:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=models.TextField(validators=[django.core.validators.MinLengthValidator(limit_value=100, message='Content should be atleast 100 characters long!')]),
        ),
    ]