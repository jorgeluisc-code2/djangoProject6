from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render, redirect, HttpResponse
from .models import Categoria,Producto, Empleado, Usuario, Venta, Detalle
from .form import  CategoriaForm,ProductoForm

#def inicioCategoria(request):
#    categoria = Categoria.objects.all()
#    contexto = {
#        'categorias':categoria
#    }
#    return render(request, 'index.html',contexto)

def inicio(request):
    producto = Producto.objects.all()
    categoria = Categoria.objects.all()
    empleado = Empleado.objects.all()
    usuario = Usuario.objects.all()
    venta = Venta.objects.all()
    detalle = Detalle.objects.all()
    contexto = {
        'productos':  producto,
        'categorias': categoria,
        'empleados': empleado,
        'usuarios': usuario,
        'ventas': venta,
        'detalles': detalle
    } 
    return render(request, 'index.html',contexto)

def crearCategoria(request):
    if request.method == 'GET':
        form = CategoriaForm()
        contexto = {
            'form': form
        }
    else:
        form = CategoriaForm(request.POST)
        contexto = {
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'crear_categoria.html', contexto)

def editarCategoria(request,id):
    categoria = Categoria.objects.get(id = id )
    if request.method == 'GET':
        form = CategoriaForm(instance= categoria)
        contexto = {
            'form': form
        }
    else:
        form = CategoriaForm(request.POST, instance=categoria)
        contexto = {
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'crear_categoria.html', contexto)

def elimimnarCategoria(request,id):
    categoria = Categoria.objects.get(id =id)
    categoria.delete()
    return redirect('index')



def crearProducto(request):
    if request.method == 'GET':
        form = ProductoForm()
        contexto = {
            'form': form
        }
    else:
        form = ProductoForm(request.POST)
        contexto = {
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'crear_producto.html', contexto)

def editarProducto(request,id):
    producto = Producto.objects.get(id = id)
    if request.method == 'GET':
        form = ProductoForm(instance= producto)
        contexto = {
            'form': form
        }
    else:
        form = ProductoForm(request.POST, instance=producto)
        contexto = {
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'crear_producto.html', contexto)

def elimimnarProducto(request,id):
    producto = Producto.objects.get(id = id)
    producto.delete()
    return redirect('index')


def Probando(request):
    producto = Categoria.objects.all()
    producto_obj=serializers.serialize('python', producto)
    return JsonResponse(producto_obj, safe=False)