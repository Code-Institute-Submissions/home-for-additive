# Generated by Django 4.2.13 on 2024-06-18 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prop_for_3d', '0005_alter_prop_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prop',
            name='slug',
            field=models.SlugField(max_length=200, unique=True),
        ),
    ]
