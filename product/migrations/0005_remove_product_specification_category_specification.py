# Generated by Django 5.0.4 on 2024-08-05 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_category_image_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='specification',
        ),
        migrations.AddField(
            model_name='category',
            name='specification',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
