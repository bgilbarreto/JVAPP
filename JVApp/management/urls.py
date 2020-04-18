from django.contrib import admin
from django.urls import include, path
from management.views import Home, insertCiudad, listarProductos, insertarCliente
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',Home.as_view(), name= 'home'),
    path('login/',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='login.html'),name='logout'),
    path('insertar_producto/',insertCiudad.as_view(), name= 'insertar_producto'),
    path('listar_productos/',listarProductos.as_view(), name= 'listarProducto'),
    path('insertar_cliente/', insertarCliente.as_view(), name ='insertar_cliente'),
]