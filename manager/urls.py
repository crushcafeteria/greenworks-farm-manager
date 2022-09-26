from django.urls import path
from django.contrib import admin
from .views import expenses

urlpatterns = [
    path('expenses/', expenses.list, name='list_expenses'),
    path('expenses/<int:id>', expenses.view, name='view_expense'),
    path('expenses/<int:id>/edit', expenses.update, name='edit_expense'),
    path('expenses/create', expenses.create, name='expense_create'),
    path('expenses/<int:id>/delete', expenses.delete, name='delete_expense'),
]

admin.site.site_header = 'Greenworks Farm Manager'
admin.site.index_title = 'Farm Manager'
