from django import forms
from .models import Categoria,Empleado,Usuario,Producto,Venta,Detalle

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'


class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = '__all__'

class DetalleForm(forms.ModelForm):
    class Meta:
        model = Detalle
        fields = '__all__'

