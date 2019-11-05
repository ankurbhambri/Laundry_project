from django.contrib import admin
from app1.models import LaundryModel


class LaundryAdmin(admin.ModelAdmin):

    list_display = ('email', 'name', 'mobile', 'landmark',
                    'address', )
    search_fields = ('email', 'mobile', 'name', )

admin.site.register(LaundryModel, LaundryAdmin)

