"""ProyectoFacturacion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from appModelos.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',menu,name='index'),#PAGINA PRINCIPAL DEL PROYECTO
    path('producto/',listarProducto, name='listarProducto'),#LSITAR LOS PRODUCTO
    path('nuevoProducto/',producto, name='crearProducto'),#CREAR UN NUEVO PRODUCTP
    path('editarProducto/<int:id>/',editarProducto, name='editarProducto'),#EDITAR PRODUCTO
    path('eliminarProducto/<int:id>/',eliminarProducto,name='eliminarProducto'),#ELIMINAR PRODUCTO
    path('cliente/', listarCliente, name='listarCliente'),    # LISTAR TODOS LOS CLIENTES
    path('nuevoCliente/', cliente, name='crearCliente'),  # CREAR NUEVO CLIENTE
    path('editarCliente/<int:id>/', editarCliente, name='editarCliente'),    # EDITAR CLIENTE
    path('eliminarCliente/<int:id>/', eliminarCliente, name='eliminarCliente'),  # ELIMINAR CLIENTE
    path('venta/',listarVenta, name='venta'),#LISTAR TODAS LAS VENTAS

]
