from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from momentoespecial.models import produto
from momentoespecial.serializers import produtoSerializer

class produtoViewSet(ModelViewSet):
    queryset = produto.objects.all()
    serializer_class = produtoSerializer