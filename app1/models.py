from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=200, blank=False, null=True)
    email = models.EmailField(max_length=255, blank=False, null=True, unique=True)
    mobile = models.CharField( max_length=12, blank=False, null=True)
    landmark = models.CharField(max_length=180, blank=False, null=True)
    address = models.CharField(max_length=1024, blank=False, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=False, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=False, null=True)

    class Meta:
        db_table = 'Customers'


class Order(models.Model):
    cust_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True, blank=False, null=True)


class Product(models.Model):
    product_name = models.CharField(max_length=50)
    product_price = models.IntegerField()


class OrderItem(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_id = models.OneToOneField(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
