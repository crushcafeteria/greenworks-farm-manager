# Generated by Django 4.1 on 2022-09-11 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0004_alter_crop_staff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='crop',
            name='staff',
        ),
    ]
