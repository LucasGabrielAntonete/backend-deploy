from momentoespecial.models import produto 
from rest_framework.serializers import ModelSerializer, SlugRelatedField
from uploader.models import Image
from uploader.serializers import ImageSerializer


class produtoSerializer(ModelSerializer):
    class Meta:
        capa_attachment_key = SlugRelatedField(
        source="capa",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
        capa = ImageSerializer(required=False, read_only=True)
        
        model = produto
        fields = '__all__'
        depth = 1



