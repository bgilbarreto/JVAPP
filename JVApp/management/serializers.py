from rest_framework import serializers
from management.models import Productos

class EstudianteSerializado (serializers.ModelSerializer):
    class Meta:
        model = Productos
        #fields = ('tienda','tipo_producto','nombre','precio','cantidad','precio_venta','caracteristicas','imagen')
        fields = '__all__'