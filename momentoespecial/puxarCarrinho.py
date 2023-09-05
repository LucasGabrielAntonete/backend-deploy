# views.py (no app que lida com o carrinho)
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import ItensCompra
from usuario.models import Usuario  # Importe o modelo do usuário

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def obter_itens_carrinho(request, usuario_id):
    usuario = Usuario.objects.get(id=usuario_id)
    itens_carrinho = ItensCompra.objects.filter(compra__usuario=usuario)
    return Response(itens_carrinho)
