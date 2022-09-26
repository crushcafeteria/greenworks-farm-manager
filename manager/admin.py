from django.contrib import admin
from .models import Crop, Expense
from pprint import pprint


class CropAdmin(admin.ModelAdmin):
    list_display = ['name', 'scientific_name', 'description']
    list_filter = ['name']


class ExpenseAdmin(admin.ModelAdmin):
    fields = ['name', 'when', 'description', 'amount']
    date_hierarchy = 'when'
    list_display = ['name', 'when', 'amount_formatted', 'author']
    list_display_links = ['name']
    search_fields = ['name', 'description', 'amount']

    @admin.display(description='Amount')
    def amount_formatted(self, obj):
        return 'Ksh ' + str(obj.amount)

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Crop, CropAdmin)
admin.site.register(Expense, ExpenseAdmin)
