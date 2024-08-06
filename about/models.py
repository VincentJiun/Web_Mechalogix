from django.db import models

# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=255)
    report = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    image_url = models.CharField(max_length=255)
