from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField('Product Name', max_length=100)

    def __str__(self):
        return self.name


class Sales(models.Model):
    VALIDATION = [
        ('YES', 'Yes'),
        ('NO', 'No'),
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=None, verbose_name='Product Name')
    date = models.DateField('Sale Date')
    amount = models.FloatField('Amount')
    quantity = models.FloatField('Quantity (in kg)', null=True)
    description = models.TextField('Description', null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None, verbose_name='Recorded By')
    valid = models.CharField('Is Valid?', max_length=100, choices=VALIDATION, default='NO')

    class Meta:
        verbose_name = ('Sale')
        verbose_name_plural = ('Sales')

    def get_absolute_url(self):
        return reverse('sales_details', kwargs={'pk': self.pk})

    def __str__(self):
        return self.product.name + ' - Ksh '+ str(self.amount)
