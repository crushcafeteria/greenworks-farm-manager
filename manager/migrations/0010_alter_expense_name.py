# Generated by Django 4.1 on 2022-09-11 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0009_expense_description_alter_expense_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Expense Name'),
        ),
    ]
