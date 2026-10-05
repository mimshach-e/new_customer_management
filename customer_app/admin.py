from django.contrib import admin
from . models import Customer

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'address']
    search_fields = ['name', 'email', 'phone', 'address']

admin.site.register(Customer, CustomerAdmin)