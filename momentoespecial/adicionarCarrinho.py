from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Compra, ItensCompra, produto
from rest_framework.permissions import AllowAny
from usuario.models import Usuario

@api_view(['POST'])
@permission_classes([AllowAny]) 
def add_to_cart(request):
    print(request.data)
    produto_id = request.data.get('produto_id')
    quantidade = request.data.get('quantidade', 1)
    usuario = request.data.get('usuario')

    usuario_instance = Usuario.objects.get(id=usuario)
    compra, _ = Compra.objects.get_or_create(usuario=usuario_instance, status=Compra.StatusCompra.CARRINHO)    

    if(ItensCompra.objects.filter(produto=produto_id).exists()):
        return Response({"message": "Produto já adicionado ao carrinho."})
    
    else:
        compra = Compra.objects.filter(usuario=usuario).first()

        try:
            produto_instance = produto.objects.get(id_produto=produto_id)
        except produto.DoesNotExist:
            return Response({"message": "Produto não encontrado."})
        
        
       

        itensCompra = ItensCompra.objects.create(produto=produto_instance, quantidade=quantidade, compra=compra)

        itensCompra.save()

    
        return Response({"message": "Produto adicionado ao carrinho com sucesso."})
