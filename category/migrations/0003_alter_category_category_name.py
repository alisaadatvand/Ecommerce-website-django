# Generated by Django 4.1.5 on 2023-08-24 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_remove_category_cat_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(max_length=50, unique=True, verbose_name=' نام دسته بندی '),
        ),
    ]