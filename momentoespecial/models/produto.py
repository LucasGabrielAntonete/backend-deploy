from django.db import models
from uploader.models import Image
from .categorias import categoria
from .tamanho import tamanho

class produto(models.Model):
    id_produto = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=200)
    quantidade = models.IntegerField(default=1,  null=True, blank=True)
    preco = models.FloatField()
    categoriaNome = models.ForeignKey(categoria, on_delete=models.CASCADE)
    tamanho = models.ManyToManyField(tamanho, related_name="tamanhos")
    dataInicio = models.DateField(null=True, blank=True)
    dataFinal = models.DateField(null=True, blank=True)
    capa = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
    )

    def calcular_preco_total(self):
        if self.dataInicio and self.dataFinal:
          dias_aluguel = (self.dataFinal - self.dataInicio).days
          if dias_aluguel > 0:
            return self.preco * dias_aluguel
          return 'Período de aluguel inválido ou não definido.'

    def __str__(self):
        return self.nome