# Generated by Django 4.2.1 on 2023-07-31 05:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='author',
        ),
    ]