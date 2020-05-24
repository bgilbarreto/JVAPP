from rest_framework import serializers
from management.models import Productos, Compras_Envios, Clientes

class ProductoSerializado (serializers.ModelSerializer):
    class Meta:
        model = Productos
        #fields = ('tienda','tipo_producto','nombre','precio','cantidad','precio_venta','caracteristicas','imagen')
        fields = '__all__'

class EnvioSerializado (serializers.ModelSerializer):
    class Meta:
        model = Compras_Envios
        fields = '__all__'

class ClienteSerializado (serializers.ModelSerializer):
    class Meta:
        model = Clientes
        fields = '__all__'