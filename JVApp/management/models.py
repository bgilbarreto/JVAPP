from django.db import models

class Departamentos (models.Model):
    nombre = models.CharField(max_length=40)

class Tipo_Producto (models.Model):
    nombre = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=100)

class Entidades_Bancarias (models.Model):
    nombre = models.CharField(max_length=40)

class Tipos_Envio (models.Model):
    nombre = models.CharField(max_length=40)
    precio = models.IntegerField(max_length=6)

class Ciudades (models.Model):
    departamento = models.ForeignKey(Departamentos, on_delete = models.CASCADE)
    nombre = models.CharField(max_length=50)

class Tiendas (models.Model):
    nombre = models.CharField(max_length=40)
    caracteristicas = models.CharField(max_length=100)
    ciudad = models.ForeignKey(Ciudades, on_delete = models.CASCADE)
    direccion = models.CharField(max_length=100)

class Actividad (models.Model):
    estado = models.CharField(max_length=20)

class Clientes (models.Model):
    cedula = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    correo = models.CharField(max_length=70)
    edad = models.IntegerField(max_length=2)
    peso = models.IntegerField(max_length=3)
    estatura = models.IntegerField(max_length=3)
    numero = models.CharField(max_length=10)
    estado = models.ForeignKey(Actividad, on_delete = models.CASCADE)

class Ubicaciones (models.Model):
    cedula = models.ForeignKey(Clientes, on_delete = models.CASCADE)
    direccion = models.CharField(max_length=70)

class Telefonos (models.Model):
    cedula = models.ForeignKey(Clientes, on_delete = models.CASCADE)
    numero = models.IntegerField(max_length=10)

class Credenciales (models.Model):
    cedula = models.ForeignKey(Clientes, on_delete = models.CASCADE, unique = True)
    usuario = models.CharField(max_length=40)
    contraseña = models.CharField(max_length=100)

class Productos (models.Model):
    tienda = models.ForeignKey(Tiendas, on_delete = models.CASCADE)
    tipo_producto = models.ForeignKey(Tipo_Producto, on_delete = models.CASCADE)
    nombre = models.CharField(max_length=40)
    precio = models.IntegerField(max_length=6)
    cantidad = models.IntegerField(max_length=3)
    precio_venta = models.IntegerField(max_length=6)
    caracteristicas = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to="productos", null=True)

class Compras_Envios (models.Model):
    cliente = models.ForeignKey(Clientes, on_delete = models.CASCADE)
    entidad_bancaria = models.ForeignKey(Entidades_Bancarias, on_delete = models.CASCADE)
    tipo_envio = models.ForeignKey(Tipos_Envio, on_delete = models.CASCADE)
    num_referencia = models.IntegerField(max_length=12)
    fech_pedido = models.DateField
    fech_envio = models.DateField
    costo_total = models.IntegerField(max_length=7)

class Producto_X_Compra (models.Model):
    producto =models.ForeignKey(Productos, on_delete = models.CASCADE)
    compra_envio = models.ForeignKey(Compras_Envios, on_delete = models.CASCADE)
