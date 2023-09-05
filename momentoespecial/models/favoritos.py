from django.db import models
from .produto import produto
from usuario.models import Usuario

class favoritos(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, related_name="favoritos")
    produto = models.ForeignKey(produto, on_delete=models.PROTECT, related_name="+")
    quantidade = models.IntegerField(default=1)