from django.db import models
from django.contrib.auth.models import User


class Crop(models.Model):
    name = models.CharField(max_length=200)
    scientific_name = models.CharField(max_length=200)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ('Crop')
        verbose_name_plural = ('Crops')

    def __str__(self):
        return self.name
