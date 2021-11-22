from django.db import models

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=200)
    idade = models.CharField(max_length=200)

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.nome