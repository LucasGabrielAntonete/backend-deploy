from django.db import models


class categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    categoriaNome = models.CharField(max_length=50)

    def __str__(self):
        return self.categoriaNome