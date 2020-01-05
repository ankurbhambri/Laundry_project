from django.contrib import admin
from app1.models import Customer, Order, Product


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):

    list_display = ('id', 'email', 'name', 'mobile', 'landmark',
                    'address', 'created_at', 'updated_at')
    search_fields = ( 'id', 'email', 'mobile', 'name', )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = ('product_name', 'product_price', 'created_at', 'updated_at')
    search_fields = ('product_name',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    list_display = ('customer_id', 'product_quantity', 'total_price', 'created_at', 'updated_at')
    search_fields = ('customer_id',)