from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from management.forms import insertClientForm, insertProductForm, insertStore, insertCathegory
from django.urls import reverse_lazy
from management.models import Productos, Compras_Envios, Tiendas
from management.models import Clientes, Tipo_Producto
from django.views.generic import TemplateView

# Create your views here.

# Vistas de Clientes
class Home (LoginRequiredMixin, generic.ListView):
    model = Clientes
    template_name = 'home.html'
    context_object_name="obj"
    login_url = 'management:login'

class insertarCliente (LoginRequiredMixin, generic.CreateView):
    model = Clientes
    template_name = 'insert_client.html'
    context_object_name = 'obj'
    form_class = insertClientForm
    login_url = 'management:login'
    success_url = reverse_lazy('management:home')

class borrarCliente (LoginRequiredMixin, generic.DeleteView):
    model = Clientes
    template_name = 'delete_client.html'
    context_object_name = 'obj'
    form_class = insertClientForm
    login_url = 'management:login'
    success_url = reverse_lazy('management:home')

class editarCliente (LoginRequiredMixin, generic.UpdateView):
    model = Clientes
    template_name = 'insert_client.html'
    context_object_name = 'obj'
    form_class = insertClientForm
    login_url = 'management:login'
    success_url = reverse_lazy('management:home')

class seacrhByName (LoginRequiredMixin, TemplateView):
    def post(self, request, *args, **kwargs):
        nombre = request.POST['datoBusqueda']
        nombres = Clientes.objects.filter(nombre__contains=nombre)
        apellidos = Clientes.objects.filter(apellido__contains=nombre)
        documentos = Clientes.objects.filter(cedula__contains=nombre)
        if nombres:
            return render(request, 'buscar.html', {'nombres':nombres, 'nombre':True})
        elif apellidos:
            return render(request, 'buscar.html', {'apellidos':apellidos, 'apellido':True})
        else:
            return render(request, 'buscar.html', {'documentos':documentos, 'documento':True})

# Vista de Login

class Login (LoginRequiredMixin, generic.TemplateView):
    template_name = 'login.html'
    login_url = 'management:login'

# Vistas de Productos

class listarProductos (LoginRequiredMixin, generic.ListView):
    model = Productos
    template_name = 'listar_productos.html'
    context_object_name = 'obj'
    login_url = 'management:login'

class insertarProducto (LoginRequiredMixin, generic.CreateView):
    model = Productos
    template_name = 'insertar_producto.html'
    context_object_name = 'obj'
    login_url = 'management:login'
    form_class = insertProductForm
    success_url = reverse_lazy('management:listarProducto')

class editarProducto (LoginRequiredMixin, generic.UpdateView):
    model = Productos
    template_name = 'insertar_producto.html'
    context_object_name = 'obj'
    login_url = 'management:login'
    form_class = insertProductForm
    success_url = reverse_lazy('management:listarProducto')

class eliminarProducto (LoginRequiredMixin, generic.DeleteView):
    model = Productos
    template_name = 'delete_product.html'
    context_object_name = 'obj'
    login_url = 'management:login'
    form_class = insertProductForm
    success_url = reverse_lazy('management:listarProducto')

# Vistas de Envios

class listaEnvios (LoginRequiredMixin, generic.ListView):
    model = Compras_Envios
    template_name = 'list_packages.html'
    context_object_name = 'obj'
    login_url = 'management:login'

# Vistas de Tiendas

class insertarTiendas (LoginRequiredMixin, generic.CreateView):
    model = Tiendas
    template_name = 'insert_store.html'
    context_object_name = 'obj'
    login_url = 'management:login'
    form_class = insertStore
    success_url = reverse_lazy('management:listarProducto')

# Vistas de Categorias
class insertarCategoria (LoginRequiredMixin, generic.CreateView):
    model = Tipo_Producto
    template_name = 'insert_cath.html'
    context_object_name = 'obj'
    login_url = 'management:login'
    form_class = insertCathegory
    success_url = reverse_lazy('management:listarProducto')