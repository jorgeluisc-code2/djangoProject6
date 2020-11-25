
from creacion.models import Detalle


#consulta=Usuario.objects.all()


#print(consulta)


objeto=Detalle(cant=1,precio=5, subtotal=5, idprod_id=6, idventa_id=3)

objeto.save()


#objeto=Venta(cliente="edmundo",fecha="10/10/10",importe=10,idemp=2)

#objeto.save()

#consulta=Venta.objects.get(id=2)

#consulta.delete()

#consulta=Venta.objects.filter(cliente__icontains='ed')
#print(consulta)