# Generated by Django 5.0.4 on 2024-08-05 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_remove_product_specification_category_specification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='specification',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]