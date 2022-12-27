from django.db import models

# Create your models here.
class Random(models.Model):
    nama = models.CharField(max_length=50)
    organisasi = models.CharField(max_length=100)
    kampus = models.TextField()
    agama = models.CharField(max_length=50)

    def __str__(self):
        return self.nama
    