from django.contrib import admin
from .models import *

class TelefonoInLine(admin.TabularInline):#Para ver los telefonos del Cliente/Proveedor
    model = Telefono

class ClienteAdmin(admin.ModelAdmin):
    exclude = ('direccion',)
    inlines = [TelefonoInLine,]

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Telefono)
admin.site.register(Ciudad)
admin.site.register(Comuna)
admin.site.register(Direccion)
admin.site.register(Cliente,ClienteAdmin)
admin.site.register(Proveedor)
admin.site.register(Producto)
admin.site.register(Detalle)
admin.site.register(Venta)