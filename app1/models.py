from django.db import models

class LaundryModel(models.Model):
    # Details of user with order id
    order_id = models.CharField(max_length=120, blank= True, null=True)
    name = models.CharField(max_length=200, blank=False, null=True)
    email = models.EmailField(max_length=255, blank=False, null=True)
    mobile = models.CharField( max_length=12, blank=False, null=True)
    landmark = models.CharField(max_length=180, blank=False, null=True)
    address = models.CharField(max_length=1024, blank=False, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=False, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=False, null=True)


    class Meta:
        db_table = 'LaundryWork'