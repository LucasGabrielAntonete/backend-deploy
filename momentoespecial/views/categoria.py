from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from momentoespecial.models import categoria
from momentoespecial.serializers import categoriaSerializer


class categoriaViewSet(ModelViewSet):
    queryset = categoria.objects.all()
    serializer_class = categoriaSerializer
