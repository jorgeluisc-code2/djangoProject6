
from creacion.models import Categoria


consulta=Categoria.objects.all()


print(consulta)


#objeto=Categoria(nombre="Categoria autonoma")


#objeto.save()


#hacer para todos los modelos

#consulta=Categoria.objects.filter(nombre__icontains='Dulces')
#print(consulta)