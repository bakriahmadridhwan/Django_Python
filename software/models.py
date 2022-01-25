import os
from django.db import models

# Create your models here.

class Software(models.Model):
    judul = models.CharField(max_length=50)
    deskripsi = models.CharField(max_length=100)
    os = models.CharField(max_length=40)

    def __str__(self):
        return self.judul
