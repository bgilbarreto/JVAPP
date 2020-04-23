from django.contrib import admin
from django.urls import include, path
from management.views import Home, listarProductos, insertarCliente, borrarCliente, editarCliente, insertarProducto, insertarCategoria
from management.views import editarProducto, eliminarProducto, insertarTiendas, seacrhByProduct
from management.views import listaEnvios, seacrhByName
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path's de clientes
    path('',Home.as_view(), name= 'home'),
    path('insertar_cliente/', insertarCliente.as_view(), name ='insertar_cliente'),
    path('editar/cliente<int:pk>',editarCliente.as_view(), name='editar_cliente'),
    path('delete/client/<int:pk>', borrarCliente.as_view(), name= 'delete_client'),
    path('searchClient/', seacrhByName.as_view(), name='buscarNombre'),
    #path's de login/logout
    path('login/',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='login.html'),name='logout'),
    #path's de Productos
    path('insertar_producto/',insertarProducto.as_view(), name= 'insertar_producto'),
    path('listar_productos/',listarProductos.as_view(), name= 'listarProducto'),
    path('editar/producto<int:pk>', editarProducto.as_view(), name='editar_producto'),
    path('delete/product<int:pk>', eliminarProducto.as_view(), name= 'delete_product'),
    path('searchProduct/', seacrhByProduct.as_view(), name='search_product'),
    #path's de Categorias, Tiendas y Envios
    path('lst_package/', listaEnvios.as_view(), name='lst_pckg'),
    path('add_store/', insertarTiendas.as_view(), name= 'insert_store'),
    path('add_cathegory/', insertarCategoria.as_view(), name= 'insert_cathegory'),
]
