from django.shortcuts import render, redirect
from django.http import HttpResponse
from appModelos.forms import *
# Create your views here.
def menu(request):
    opciones = {'menu': 'Menú Principal','venta': 'Ventas', 'producto': 'Productos',
                'cliente': 'Clientes', 'administrar': 'Administrador'}

    return render(request, 'paginaPrincipal.html', opciones)




def producto(request):
    opciones = {'menu': 'Menú Principal','venta': 'Ventas', 'producto': 'Productos',
                'cliente': 'Clientes', 'administrar': 'Administrador', 'accion':'crear'}
    if request.method == 'POST':
      
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listarProducto')
    else:
        form = ProductoForm()
        opciones['form'] = form

    return render(request, 'formularioProducto.html', opciones)

def editarProducto(request, id):
    opciones = {'menu': 'Menú Principal','venta': 'Ventas', 'producto': 'Productos',
                'cliente': 'Clientes', 'administrar': 'Administrador', 'accion': 'Actualizar'}
    producto = Producto.objects.get(id=id)
    if request.method == 'GET':
        form = ProductoForm(instance=producto)
        opciones['form'] = form
    else:
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('listarProducto')

    return render(request, 'formularioProducto.html', opciones)

def listarProducto(request):
    producto = Producto.objects.all()
    opciones = {'menu': 'Menú Principal', 'venta': 'Ventas', 'producto': 'Productos',
                'cliente': 'Clientes', 'administrar': 'Administrador', 'productos': producto}
    return render(request, 'consultaProducto.html', opciones)

def eliminarProducto(request, id):
    producto = Producto.objects.get(id=id)
    if request.method == 'POST':
        producto.delete()
        return redirect('listarProducto')
    return render(request, 'eliminarProducto.html', {'producto': producto})








def cliente(request):
    opciones = {'menu': 'Menú Principal','venta': 'Ventas', 'producto': 'Productos',
                'cliente': 'Clientes', 'administrar': 'Administrador', 'accion':'crear'}
    if request.method == 'POST':
        # pass
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listarCliente')
    else:
        form = ClienteForm()
        opciones['form'] = form

    return render(request, 'formularioCliente.html', opciones)

def editarCliente(request, id):
    opciones = {'menu': 'Menú Principal','venta': 'Ventas', 'producto': 'Productos',
                'cliente': 'Clientes', 'administrar': 'Administrador', 'accion': 'Actualizar'}
    cliente = Cliente.objects.get(id=id)
    if request.method == 'GET':
        form = ClienteForm(instance=cliente)
        opciones['form'] = form
    else:
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('listarCliente')

    return render(request, 'formularioCliente.html', opciones)

def listarCliente(request):
    cliente = Cliente.objects.all()
    opciones = {'menu': 'Menú Principal', 'venta': 'Ventas', 'producto': 'Productos',
                'cliente': 'Clientes', 'administrar': 'Administrador', 'listarCliente': cliente}
    return render(request, 'consultarCliente.html', opciones)

def eliminarCliente(request, id):
    cliente = Cliente.objects.get(id=id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('listarCliente')
    return render(request, 'eliminarCliente.html', {'cliente': cliente})



def listarVenta(request):
    factura = Factura.objects.all()
    opciones = {'menu': 'Menú Principal', 'venta': 'Ventas', 'producto': 'Productos',
                'cliente': 'Clientes', 'administrar': 'Administrador', 'listarVenta': factura}
    return render(request, 'consultaVenta.html', opciones)