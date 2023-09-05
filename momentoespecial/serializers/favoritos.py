from rest_framework.serializers import ModelSerializer
from momentoespecial.models import favoritos

class favoritosSerializer(ModelSerializer):
    class Meta:
        model = favoritos
        fields = "__all__"
        depth = 1