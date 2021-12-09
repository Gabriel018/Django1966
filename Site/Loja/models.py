from django.db import models
from django.urls import reverse
# Create your models here.


class Produto(models.Model):
    id = models.AutoField(primary_key=True,blank=True)
    titulo = models.CharField(max_length=200)
    desc = models.TextField(max_length=200)
    price = models.CharField(max_length=8)


    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse(f'{self.titulo}')