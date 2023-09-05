from rest_framework.viewsets import ModelViewSet

from momentoespecial.models import favoritos
from momentoespecial.serializers import favoritosSerializer


class favoritosViewSet(ModelViewSet):
    queryset = favoritos.objects.all()
    serializer_class = favoritosSerializer