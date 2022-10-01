from django.urls import path
from expenses.views import ExpenseCreateView, ExpensesListView, ExpenseDetailView, ExpensesDeleteView, ExpensesUpdateView

urlpatterns = [
    path('', ExpensesListView.as_view(), name='expenses_list'),
    path('create', ExpenseCreateView.as_view(), name='expenses_create'),
    path('<int:pk>', ExpenseDetailView.as_view(), name='expenses_details'),
    path('<int:pk>/delete', ExpensesDeleteView.as_view(), name='expenses_delete'),
    path('<int:pk>/edit', ExpensesUpdateView.as_view(), name='expenses_update'),
]
