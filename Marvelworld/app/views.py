from django.shortcuts import render, redirect,get_object_or_404
from .models import Productos
from .forms import  ProductoForm, UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import permission_required

def home(request):
    return render(request, 'app/home.html')

def productos(request):
    productos = Productos.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'app/productos.html', data)

@permission_required('app.view_producto')
def listar_productos(request):
    productos = Productos.objects.all()
    return render(request, 'app/productos/listar.html', {'productos': productos})

@permission_required('app.add_producto')
def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = ProductoForm()
    return render(request, 'app/productos/agregar.html', {'form': form})

@permission_required('app.change_producto')
def editar_producto(request, id):
    producto = get_object_or_404(Productos, id=id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'app/productos/modificar.html', {'form': form, 'producto': producto})

@permission_required('app.delete_producto')
def eliminar_producto(request, id):
    producto = get_object_or_404(Productos, id=id)
    producto.delete()
    messages.success(request, "Eliminado Correctamente")
    return redirect(to="listar_productos")

def registro(request):
    data={
        'form': UserCreationForm()
    }
    if request.method == 'POST':
        formulario = UserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username= formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado Correctamente")
            return redirect(to="home")
        data["form"] = formulario
    return render(request, 'app/registro/registro.html', data)

def acerca_de(request):
    return render(request, 'app/acerca_de.html')

