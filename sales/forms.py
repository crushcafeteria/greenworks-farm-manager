from django import forms
from sales.models import Sales, Product


class SalesForm(forms.ModelForm):
    product = forms.ModelChoiceField(
        empty_label='Choose a product',
        queryset=Product.objects.all(),
        to_field_name='name',
        required=True,
        widget=forms.Select()
    )
    date = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date'}))
    amount = forms.FloatField(required=True)
    quantity = forms.FloatField(required=False)
    description = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = Sales
        fields = ['product', 'date', 'amount', 'quantity', 'description']
