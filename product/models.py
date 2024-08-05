from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    image_url = models.CharField(max_length=255, blank=True, null=True)
    specification = models.TextField(max_length=500, blank=True, null=True)

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    name_tag = models.CharField(max_length=255)
    price = models.FloatField(default=0)
    subscription = models.FloatField(default=0)
    total = models.FloatField()
    image_url = models.CharField(max_length=255, blank=True, null=True)
    propose = models.CharField(max_length=255, blank=True, null=True)
    describe = models.TextField(max_length=500, blank=True, null=True)
    applicable_for = models.CharField(max_length=255, blank=True, null=True)
    

