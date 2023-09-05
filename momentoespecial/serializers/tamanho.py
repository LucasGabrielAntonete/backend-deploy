from momentoespecial.models import tamanho
from rest_framework.serializers import ModelSerializer

class tamanhoSerializer(ModelSerializer):
    class Meta:
        model = tamanho
        fields = '__all__'
