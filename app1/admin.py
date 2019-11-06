from django.contrib import admin
from app1.models import LaundryModel


class LaundryAdmin(admin.ModelAdmin):

    list_display = ( 'order_id', 'email', 'name', 'mobile', 'landmark',
                    'address', )
    search_fields = ( 'order_id', 'email', 'mobile', 'name', )

admin.site.register(LaundryModel, LaundryAdmin)

