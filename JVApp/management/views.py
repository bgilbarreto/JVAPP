from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from management.forms import ciudadForm, ClientForm
from django.urls import reverse_lazy
from management.models import Ciudades, Productos
from management.models import Clientes

# Create your views here.

class Home (LoginRequiredMixin, generic.ListView):
    model = Clientes
    template_name = 'home.html'
    context_object_name="obj"
    login_url = 'management:login'

class Login (LoginRequiredMixin, generic.TemplateView):
    template_name = 'login.html'
    login_url = 'management:login'

class insertCiudad (LoginRequiredMixin, generic.CreateView):
    model = Ciudades
    template_name = 'insertar_producto.html'
    context_object_name = 'obj'
    form_class = ciudadForm
    success_url = reverse_lazy('management:home')
    login_url = 'management:login'

class listarProductos (LoginRequiredMixin, generic.ListView):
    model = Productos
    template_name = 'listar_productos.html'
    context_object_name = 'obj'
    login_url = 'management:login'

class insertarCliente (LoginRequiredMixin, generic.CreateView):
    model = Clientes
    template_name = 'insert_client.html'
    context_object_name = 'obj'
    login_url = 'management:login'
    success_url = reverse_lazy('management:home')
