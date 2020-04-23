from django import forms
from management.models import Clientes, Actividad, Tipo_Producto, Tiendas, Productos, Ciudades

# Form para Transacciondes de clientes

class FKactivy (forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "{}".format(obj.estado)

class insertClientForm (forms.ModelForm):
    estado = FKactivy(queryset=Actividad.objects.order_by('id'))
    class Meta:
        model = Clientes
        fields = ['cedula','nombre','apellido','correo','edad','peso','estatura','numero','estado']
        labels = {'cedula':'Cedula','nombre':'Nombre','apellido':'Apellido','correo':'Correo','edad':'Edad','peso':'Peso','numero':'Numero','estatura':'Estatura'}
        widget = {'cedula':forms.TextInput(),'nombre':forms.TextInput(),'apellido':forms.TextInput(),'correo':forms.TextInput(),'edad':forms.TextInput(),'peso':forms.TextInput(),'numero':forms.TextInput(),'estatura':forms.TextInput()}

    def __init__(self,*args,**kwargs):
       super().__init__ (*args,**kwargs)
       for field in iter(self.fields):
           self.fields[field].widget.attrs.update({
               'class':'from-control'
           }) 
           self.fields['estado'].label = 'Condicion Fisica del cliente'

# Form para transacciones de Inventario

class FKstore (forms.ModelChoiceField):
    def label_from_instance(self,obj):
        return "{}".format(obj.nombre)

class FKt_product (forms.ModelChoiceField):
    def label_from_instance(self,obj):
        return "{}".format(obj.nombre)

class insertProductForm (forms.ModelForm):
    tienda = FKstore(queryset=Tiendas.objects.order_by('id'))
    tipo_producto = FKt_product(queryset= Tipo_Producto.objects.order_by('id'))
    class Meta:
        model = Productos
        fields = ['nombre','precio','cantidad','precio_venta','caracteristicas','tienda','tipo_producto','imagen']
        labels = {'nombre':'Nombre','precio':'Precio','cantidad':'Cantidad','precio_venta':'precio_Venta','caracteristicas':'Caracteristicas'}
        widget = {'nombre':forms.TextInput(),'precio':forms.TextInput(),'cantidad':forms.TextInput(),'precio_venta':forms.TextInput(),'caracteristicas':forms.TextInput()}

    def __init__(self,*args,**kwargs):
       super().__init__ (*args,**kwargs)
       for field in iter(self.fields):
           self.fields[field].widget.attrs.update({
               'class':'from-control'
           }) 
           self.fields['tienda'].label = 'Ubicacion actual del producto'
           self.fields['tipo_producto'].label = 'Categoria del producto'

#Form para Añadir nuevas sucursales

class FKCity (forms.ModelChoiceField):
    def label_from_instance(self,obj):
        return "{}".format(obj.nombre)

class insertStore (forms.ModelForm):
    ciudad = FKCity(queryset=Ciudades.objects.order_by('id'))
    class Meta:
        model = Tiendas
        fields = ['nombre','caracteristicas','direccion','ciudad']
        labels = {'nombre':'Nombre','caracteristicas':'Caracteristicas','direccion':'Direccion','ciudad':'Ciudad'}
        widget = {'nombre':forms.TextInput(),'caracteristicas':forms.TextInput(),'direccion':forms.TextInput,'ciudad':forms.TextInput()}

    def __init__(self,*args,**kwargs):
       super().__init__ (*args,**kwargs)
       for field in iter(self.fields):
           self.fields[field].widget.attrs.update({
               'class':'from-control'
           })
           self.fields['ciudad'].label = 'Ciudad de Ubicacion' 

# Form para Añadir nuevas categorias

class insertCathegory (forms.ModelForm):
    class Meta:
        model = Tipo_Producto
        fields = ['nombre','descripcion']
        labels = {'nombre':'Nombre','descripcion':'Descripcion'}
        widget = {'nombre':forms.TextInput(),'descripcion':forms.TextInput()}

    def __init__(self,*args,**kwargs):
       super().__init__ (*args,**kwargs)
       for field in iter(self.fields):
           self.fields[field].widget.attrs.update({
               'class':'from-control'
           })
           