"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from momentoespecial import adicionarCarrinho, buscarProdutos, removerCarrinho, buscarPesquisa
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from momentoespecial.views import produtoViewSet, CompraViewSet, categoriaViewSet, tamanhoViewSet, favoritosViewSet, ProdutosPorCategoriaView
from rest_framework.views import APIView
from usuario.router import router as usuario_router
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path
from usuario import cadastro
from django.conf import settings
from django.conf.urls.static import static

from uploader.router import router as uploader_router

router = DefaultRouter()
router.register(r"produtos", produtoViewSet)
router.register(r"compras", CompraViewSet)
router.register(r"categorias", categoriaViewSet)
router.register(r"tamanhos", tamanhoViewSet)
router.register(r"favoritos", favoritosViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/", include(usuario_router.urls)),
    path("api/media/", include(uploader_router.urls)),
    path('api/signup/', cadastro.create_user, name='create_user'),
    path('api/adicionar/', adicionarCarrinho.add_to_cart, name='add_to_cart'),
    path('api/get_cart/', buscarProdutos.get_cart, name='get_cart'),
    path('api/produtos/por-categoria/<int:categoria_id>/', ProdutosPorCategoriaView.as_view(), name='produtos-por-categoria'),
    path('api/remove_from_cart/', removerCarrinho.remove_from_cart, name='remove_from_cart'),
    path('api/produtos/search/', buscarPesquisa.ProdutoSearchView.as_view(), name='produto-search'),
]
urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)