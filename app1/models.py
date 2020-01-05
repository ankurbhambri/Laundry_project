from django.db import models
from django.contrib.postgres.fields import JSONField


class Customer(models.Model):
    name = models.CharField(max_length=200, blank=False, null=True)
    email = models.EmailField(max_length=255, blank=False, null=True, unique=True)
    mobile = models.CharField( max_length=12, blank=False, null=True)
    landmark = models.CharField(max_length=180, blank=False, null=True)
    address = models.CharField(max_length=1024, blank=False, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=False, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=False, null=True)

    
class Product(models.Model):
    product_name = models.CharField(max_length=50)
    product_price = models.IntegerField()
    product_image = models.ImageField(upload_to='product_images/')
    created_at = models.DateTimeField(auto_now_add=True, blank=False, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=False, null=True)


class Order(models.Model):
    customer_id = models.IntegerField()
    product_quantity = JSONField()
    total_price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, blank=False, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=False, null=True)

