from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField('Product Name', max_length=100)

    def __str__(self):
        return self.name


class Sales(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=None, verbose_name='Product Name')
    date = models.DateField('Sale Date')
    amount = models.FloatField('Amount')
    quantity = models.FloatField('Quantity (in kg)')
    description = models.TextField('Description')
    author_id = models.ForeignKey(User, on_delete=models.CASCADE, default=None, verbose_name='Recorded By')

    class Meta:
        verbose_name = ('Sale')
        verbose_name_plural = ('Sales')

    def get_absolute_url(self):
        return reverse('sales_details', kwargs={'pk': self.pk})
