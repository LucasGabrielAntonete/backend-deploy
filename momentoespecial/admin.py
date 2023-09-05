from django.contrib import admin

from .models import tamanho, categoria, produto, Compra, ItensCompra, favoritos


admin.site.register(tamanho)
admin.site.register(categoria)
admin.site.register(produto)
admin.site.register(ItensCompra)
admin.site.register(favoritos)



class ItensCompraInline(admin.TabularInline):
    model = ItensCompra

@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    inlines = [ItensCompraInline]

from rest_framework.routers import DefaultRouter
