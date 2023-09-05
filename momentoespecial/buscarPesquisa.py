from rest_framework import generics
from rest_framework import filters
from rest_framework.decorators import api_view, permission_classes
from .models import produto
from .serializers import produtos
from rest_framework.permissions import AllowAny

@permission_classes([AllowAny]) 
class ProdutoSearchView(generics.ListAPIView):
    queryset = produto.objects.all()
    serializer_class = produtos
    filter_backends = [filters.SearchFilter]
    search_fields = ['nome'] 
