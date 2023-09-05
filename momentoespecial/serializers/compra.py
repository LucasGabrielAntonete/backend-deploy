from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer, CharField

from momentoespecial.models import Compra, ItensCompra, produto


class ItensCompraSerializer(ModelSerializer):
    capa_url = SerializerMethodField()

    tamanho = CharField()

    def get_tamanho(self, obj):
        return obj.produto.tamanho.tamanho

    def get_capa_url(self, obj):
        if obj.produto.capa:
            return self.context['request'].build_absolute_uri(obj.produto.capa.url)
        return None

    class Meta:
        model = ItensCompra
        fields = ['id', 'produto', 'quantidade', 'capa_url', 'tamanho']

    def get_total(self, obj):
     return obj.produto.preco

class CompraSerializer(ModelSerializer):
    usuario = CharField(source="usuario.email", read_only=True)
    status = CharField(source="get_status_display", read_only=True)
    itens = ItensCompraSerializer(many=True, read_only=True)
    

    class Meta:
        model = Compra
        fields = ("id", "usuario", "status", "total", "itens")
