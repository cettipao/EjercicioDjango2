from django.contrib import admin
from .models import *

class TelefonoInLine(admin.TabularInline):#Para ver los telefonos del Cliente/Proveedor
    model = Telefono

class ClienteAdmin(admin.ModelAdmin):
    #exclude = ('direccion',)
    inlines = [TelefonoInLine,]

class ProductoAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    fieldsets = (
        ("Descripcion", {
            'fields':('id','nombre','categoria','proveedor',)#Agrego categoria y Proveedor para poder crear objetos
        }),
        ('Variables', {
            'fields':('precio','stock',)
        }),
    )

class ProductoInLine(admin.TabularInline):
    model = Producto
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('rut','nombre','web')
    list_display_links = ('rut','nombre',)
    list_filter = ('nombre',)
    inlines = [ProductoInLine,]

class VentaAdmin(admin.ModelAdmin):
    list_display = ('fecha','cliente','isDescuento')
    list_display_links = ('fecha','cliente',)
    actions = ['make_descuento']
    
    def make_descuento(self,request,queryset):
        return queryset.update(descuento = True)

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Telefono)
admin.site.register(Ciudad)
admin.site.register(Comuna)
admin.site.register(Direccion)
admin.site.register(Cliente,ClienteAdmin)
admin.site.register(Proveedor,ProveedorAdmin)
admin.site.register(Producto,ProductoAdmin)
admin.site.register(Detalle)
admin.site.register(Venta,VentaAdmin)