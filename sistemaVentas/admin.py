from django.contrib import admin
from .models import *

class ClienteAdmin(admin.ModelAdmin):
    exclude = ()

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Telefono)
admin.site.register(Ciudad)
admin.site.register(Comuna)
admin.site.register(Direccion)
admin.site.register(Cliente)
admin.site.register(Proveedor)
admin.site.register(Producto)
admin.site.register(Detalle)
admin.site.register(Venta)