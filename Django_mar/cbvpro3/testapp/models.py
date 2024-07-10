from django.db import models

# Create your models here.
class Company(models.Model):
    name=models.CharField(max_length=21)
    location=models.CharField(max_length=21)
    ceo=models.CharField(max_length=21)

from django.urls import reverse
def get_absolute_url(self):
    return reverse('detail',kwargs={'pk':self.pk})

