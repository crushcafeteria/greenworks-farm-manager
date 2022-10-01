from django import forms
from expenses.models import Expenses


class ExpenseForm(forms.ModelForm):
    name = forms.CharField(label='Expense Name', required=True)
    when = forms.DateField(label='Date', required=True, widget=forms.DateInput(attrs={'type': 'date'}))
    description = forms.CharField(widget=forms.Textarea)
    amount = forms.FloatField(label='Amount', required=True)

    class Meta:
        model = Expenses
        fields = ['name', 'type', 'when', 'description', 'amount']
