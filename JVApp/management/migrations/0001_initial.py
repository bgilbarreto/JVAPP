# Generated by Django 3.0.5 on 2020-04-18 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Ciudades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('apellido', models.CharField(max_length=60)),
                ('correo', models.CharField(max_length=70)),
                ('edad', models.IntegerField(max_length=2)),
                ('peso', models.IntegerField(max_length=3)),
                ('estatura', models.IntegerField(max_length=3)),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.Actividad')),
            ],
        ),
        migrations.CreateModel(
            name='Compras_Envios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_referencia', models.IntegerField(max_length=12)),
                ('costo_total', models.IntegerField(max_length=7)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.Clientes')),
            ],
        ),
        migrations.CreateModel(
            name='Departamentos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Entidades_Bancarias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Tiendas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('caracteristicas', models.CharField(max_length=100)),
                ('ciudad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.Ciudades')),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tipos_Envio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('precio', models.IntegerField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Ubicaciones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(max_length=70)),
                ('cedula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.Clientes')),
                ('tienda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.Tiendas', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Telefonos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField(max_length=10)),
                ('cedula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.Clientes')),
            ],
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('precio', models.IntegerField(max_length=6)),
                ('cantidad', models.IntegerField(max_length=3)),
                ('precio_venta', models.IntegerField(max_length=6)),
                ('caracteristicas', models.CharField(max_length=100)),
                ('tienda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.Tiendas')),
                ('tipo_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.Tipo_Producto')),
            ],
        ),
        migrations.CreateModel(
            name='Producto_X_Compra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('compra_envio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.Compras_Envios')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.Productos')),
            ],
        ),
        migrations.CreateModel(
            name='Credenciales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=40)),
                ('contraseña', models.CharField(max_length=100)),
                ('cedula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.Clientes', unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='compras_envios',
            name='entidad_bancaria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.Entidades_Bancarias'),
        ),
        migrations.AddField(
            model_name='compras_envios',
            name='tipo_envio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.Tipos_Envio'),
        ),
        migrations.AddField(
            model_name='ciudades',
            name='departamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.Departamentos'),
        ),
        migrations.CreateModel(
            name='Celulares',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField(max_length=10)),
                ('cedula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.Clientes')),
            ],
        ),
    ]