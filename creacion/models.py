from django.db import models


class Empleado (models.Model):

    nombre=models.CharField(max_length=50, blank=False)
    apellido=models.CharField(max_length=50, blank=False)
    email = models.CharField(max_length=50, blank=False)
    telefono=models.CharField(max_length=12, blank=True)



class Usuario (models.Model):
    idempleado = models.ForeignKey(Empleado, null=True, on_delete=models.CASCADE)
    usuario=models.CharField(max_length=20, blank=False)
    clave=models.CharField(max_length=40, blank=False)
    estado = models.DecimalField(max_digits=2, decimal_places=0)


class Categoria (models.Model):

    nombre = models.CharField(max_length=50,  blank=False)




class Producto (models.Model):

    idcat = models.ForeignKey(Categoria, null=True, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100, blank=False)
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    stock =  models.IntegerField(blank=False)



class Venta (models.Model):

    idemp = models.ForeignKey(Empleado, null=True, on_delete=models.CASCADE)
    cliente = models.CharField(max_length=50)
    fecha =  models.DateTimeField(auto_now=True)
    importe = models.DecimalField(max_digits=10, decimal_places=2, blank=False)

class Detalle (models.Model):

    idventa = models.ForeignKey(Venta, null=True, on_delete=models.CASCADE)
    idprod = models.ForeignKey(Producto, null=True, on_delete=models.CASCADE)
    cant = models.DecimalField(max_digits=2, decimal_places=0, blank=False)
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    subtotal = models.DecimalField(max_digits=2, decimal_places=0, blank=True)
