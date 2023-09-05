from momentoespecial.models import categoria
from rest_framework.serializers import ModelSerializer

class categoriaSerializer(ModelSerializer):
    class Meta:
        model = categoria
        fields = '__all__'
