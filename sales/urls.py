from django.urls import path
from django.contrib import admin
from sales.views import SalesCreateView, SalesDetailView, SalesListView

urlpatterns = [
    path('', SalesListView.as_view(), name='sales_list'),
    path('create', SalesCreateView.as_view(), name='sales_create'),
    path('<int:pk>/', SalesDetailView.as_view(), name='sales_details'),
]
