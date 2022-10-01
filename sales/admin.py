from django.contrib import admin
from sales.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']


admin.site.register(Product, ProductAdmin)
