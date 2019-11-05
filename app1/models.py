from django.db import models

class LaundryModel(models.Model):
    # Details of the user
    name = models.CharField(max_length=200, blank=False, null=True)
    email = models.EmailField(max_length=255, blank=False, null=True)
    mobile = models.CharField( max_length=12, blank=False, null=True)
    landmark = models.CharField(max_length=180, blank=True, null=True)
    address = models.CharField(max_length=1024, blank=False, null=True)

    class Meta:
        db_table = 'LaundryWork'