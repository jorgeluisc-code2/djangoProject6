"""djangoProject6 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.urls import path
from creacion.views import crearCategoria, editarCategoria, elimimnarCategoria
from creacion.views import crearProducto, inicio, editarProducto, elimimnarProducto
from creacion.views import Probando
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='index'),
    path('crear_categoria/', crearCategoria, name='crear_categoria'),
    path('crear_producto/', crearProducto, name='crear_producto'),
    path('editar_persona/<int:id>', editarCategoria, name='editar_categoria'),
    path('editar_producto/<int:id>', editarProducto, name='editar_producto'),
    path('eliminar_persona/<int:id>', elimimnarCategoria, name='eliminar_categoria'),
    path('eliminar_producto/<int:id>', elimimnarProducto, name='eliminar_producto'),
    path('prueba', Probando, name='probando'),

]
