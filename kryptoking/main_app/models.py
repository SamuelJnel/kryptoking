from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Krypto(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    information = models.CharField(max_length=250)
    symbol = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'krypto_id': self.id})