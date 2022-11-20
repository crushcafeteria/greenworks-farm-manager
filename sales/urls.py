from django.urls import path
from django.contrib import admin
from sales.views import SalesCreateView, SalesDetailView, SalesListView, SalesUpdateView, SalesValidate, SalesDeleteView

urlpatterns = [
    path('', SalesListView.as_view(), name='sales_list'),
    path('create', SalesCreateView.as_view(), name='sales_create'),
    path('<int:pk>/', SalesDetailView.as_view(), name='sales_details'),

    path('<int:pk>/delete', SalesDeleteView.as_view(), name='sales_delete'),
    path('<int:pk>/edit', SalesUpdateView.as_view(), name='sales_update'),
    path('<int:pk>/validate', SalesValidate.as_view(), name='sales_validate'),
]
