# Generated by Django 4.1.5 on 2023-08-24 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='cat_image',
        ),
        migrations.RemoveField(
            model_name='category',
            name='description',
        ),
    ]