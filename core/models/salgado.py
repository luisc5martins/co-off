from django.db import models

class Salgado(models.Model):
    nome = models.CharField(max_length=20)
    preco = models.DecimalField(max_digits=4, decimal_places=2)
    descricao = models.CharField(max_length=100)