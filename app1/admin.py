from django.contrib import admin
from app1.models import Customer, Order, Product, OrderItem


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):

    list_display = ('id', 'email', 'name', 'mobile', 'landmark',
                    'address', )
    search_fields = ( 'id', 'email', 'mobile', 'name', )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    list_display = ('cust_id', 'order_date')
    search_fields = ('cust_id', 'order_date')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = ('product_name', 'product_price')
    search_fields = ('product_name', 'product_price')


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):

    list_display = ('order_id', 'product_id', 'quantity')
    search_fields = ('order_id', 'product_id', 'quantity')
