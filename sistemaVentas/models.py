from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length = 20)
    descripcion = models.CharField(max_length = 40)

    def __str__(self):
        return str(self.nombre)

class Telefono(models.Model):#Puede haber varios Telefonos
    numero = models.CharField(max_length = 20)
    cliente = models.ForeignKey(
        'Cliente',
        on_delete=models.CASCADE,
        null=False
    )
    def __str__(self):
        return str(self.numero)

class Ciudad(models.Model):
    nombre = models.CharField(max_length = 20)
    def __str__(self):
        return str(self.nombre)
class Comuna(models.Model):
    nombre = models.CharField(max_length = 20)
    ciudad = models.ForeignKey(
        'Ciudad',
        on_delete=models.CASCADE,
        null=False
    )
    def __str__(self):
        return str(self.nombre)

class Direccion(models.Model): #Foreign key alrevez (Cliente tiene Dir o Dir tiene Cliente)
    numero = models.CharField(max_length = 5)
    calle = models.CharField(max_length = 20) 
    comuna = models.ForeignKey(
        'Comuna',
        on_delete=models.CASCADE,
        null=False
    )
    def __str__(self):
        return str("{}, {}".format(self.calle,self.numero))

class Cliente(models.Model):
    rut = models.CharField(max_length = 20)
    nombre = models.CharField(max_length = 20)
    direccion = models.ForeignKey(
        'Direccion',
        on_delete=models.CASCADE,
        null=False
    )
    def __str__(self):
        return str(self.nombre)

class Proveedor(models.Model):
    rut = models.CharField(max_length = 20)
    nombre = models.CharField(max_length = 20)
    web = models.CharField(max_length = 30)
    direccion = models.ForeignKey(
        'Direccion',
        on_delete=models.CASCADE,
        null=False
    )
    def __str__(self):
        return str(self.nombre)

class Producto(models.Model):
    nombre = models.CharField(max_length = 20)
    precio = models.IntegerField()
    stock = models.IntegerField()
    categoria = models.ForeignKey(
        'Categoria',
        on_delete=models.CASCADE,
        null=False
    )
    proveedor = models.ForeignKey(
        'Proveedor',
        on_delete=models.CASCADE,
        null=False
    )
    def __str__(self):
        return str("{} (${})".format(self.nombre,self.precio))

class Detalle(models.Model):
    producto = models.ForeignKey(
        'Producto',
        on_delete=models.CASCADE,
        null=False
    )
    cantidad = models.SmallIntegerField()
    venta = models.ForeignKey(
        'Venta',
        on_delete=models.CASCADE,
        null=False
    )
    def __str__(self):
        return str("({}) {} a {}".format(self.cantidad,self.producto.nombre,self.venta.cliente.nombre))

class Venta(models.Model):
    fecha = models.DateField()
    descuento = models.BooleanField()
    montoFinal = models.IntegerField()
    cliente = models.ForeignKey(
        'Cliente',
        on_delete=models.CASCADE,
        null=False
    )
    def isDescuento(self):
        return self.descuento
    isDescuento.boolean = descuento
    isDescuento.short_description = 'Tiene Descuento'

    def __str__(self):
        return str("{}: {} (${})".format(self.fecha, self.cliente.nombre,self.montoFinal))

