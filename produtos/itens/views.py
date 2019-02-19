from django.shortcuts import render

# Create your views here.
class Produto(models.Model):
    nome = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    descricao = models.TextField()
