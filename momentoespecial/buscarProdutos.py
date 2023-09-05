from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Compra, ItensCompra, produto
from rest_framework.permissions import AllowAny

@api_view(['GET'])
@permission_classes([IsAuthenticated]) 
def get_cart(request):
    user = request.user
    try:
        compra = Compra.objects.get(usuario=user, status=Compra.StatusCompra.CARRINHO)
        itens = ItensCompra.objects.filter(compra=compra)
        cart_data = []
        for item in itens:
            cart_data.append({
                'produto_id': item.produto.id_produto,
                'nome': item.produto.nome,
                'capa': item.produto.capa.url,
                'preco': item.produto.preco,
                'descricao': item.produto.descricao,
                'id': item.produto.id_produto,
            })
        return Response(cart_data)
    except Compra.DoesNotExist:
        return Response({"message": "Carrinho não encontrado para este usuário."})
