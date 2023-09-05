from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Compra, ItensCompra, produto
from rest_framework.permissions import AllowAny
from usuario.models import Usuario

@api_view(['POST'])
@permission_classes([AllowAny]) 
def remove_from_cart(request):
    produto_id = request.data.get('produto_id')
    usuario_id = request.data.get('usuario_id')

    usuario_instance = Usuario.objects.get(id=usuario_id)
    try:
        compra = Compra.objects.get(usuario=usuario_instance, status=Compra.StatusCompra.CARRINHO)
    except Compra.DoesNotExist:
        return Response({"message": "Carrinho vazio ou não encontrado."})

    try:
        produto_instance = produto.objects.get(id_produto=produto_id)
    except produto.DoesNotExist:
        return Response({"message": "Produto não encontrado."})

    try:
        item = ItensCompra.objects.get(compra=compra, produto=produto_instance)
        item.delete()
        return Response({"message": "Produto removido do carrinho com sucesso."})
    except ItensCompra.DoesNotExist:
        return Response({"message": "Produto não encontrado no carrinho."})
