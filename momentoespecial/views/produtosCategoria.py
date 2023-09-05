from rest_framework.viewsets import ModelViewSet
from momentoespecial.models import produto
from rest_framework.views import APIView
from momentoespecial.serializers import produtoSerializer
from rest_framework.response import Response


class ProdutosPorCategoriaView(APIView):
    def get(self, request, categoria_id):
        produtos = produto.objects.filter(categoriaNome=categoria_id)
        serializer = produtoSerializer(produtos, many=True)
        return Response(serializer.data)
    def get_queryset(self):

        return produto.objects.all()