from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from momentoespecial.models import tamanho
from momentoespecial.serializers import tamanhoSerializer

class tamanhoViewSet(ModelViewSet):
    queryset = tamanho.objects.all()
    serializer_class = tamanhoSerializer
