from rest_framework.viewsets import ModelViewSet

from momentoespecial.models import Compra
from momentoespecial.serializers import CompraSerializer


class CompraViewSet(ModelViewSet):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer