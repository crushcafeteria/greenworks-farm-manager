from django.db import models
from django.contrib.auth.models import User


class Expense(models.Model):
    EXPENSE_TYPES = [
        ('OTHER', 'Other'),
        ('TRAVEL', 'Travelling'),
        ('WAGES', 'Labour and wages'),
        ('FOOD', 'Food and drinks'),
        ('FUEL', 'Fuel'),
        ('MARKETING', 'Marketing'),
        ('INPUTS', 'Farm Inputs (Fertilizer, pesticides e.t.c'),
    ]

    name = models.CharField('Expense Name', max_length=100)
    type = models.CharField('Category', max_length=100, choices=EXPENSE_TYPES, default='OTHER')
    when = models.DateField('Date of expenditure')
    description = models.TextField('Describe how you spent the funds')
    amount = models.FloatField('Amount (in KES)')
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None, verbose_name='Recorded By')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ('Expense')
        verbose_name_plural = ('Expenses')
        ordering = ['-when']

    def amount_formatted(self):
        return 'Ksh ' + str(self.amount)
