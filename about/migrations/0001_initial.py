# Generated by Django 5.0.4 on 2024-08-06 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('report', models.CharField(max_length=255)),
                ('date', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
