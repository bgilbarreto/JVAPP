from django import forms
from management.models import Ciudades, Departamentos, Clientes, Actividad

class FKdept (forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "{}".format(obj.nombre)

class ciudadForm (forms.ModelForm):
    departamento_id = FKdept(queryset=Departamentos.objects.order_by('id'))
    class Meta:
        model = Ciudades
        fields = ['nombre','departamento_id']
        labels = {'nombre':'nombre de ciudad'}
        widget = {'nombre':forms.TextInput()}

    def __init__(self,*args,**kwargs):
       super().__init__ (*args,**kwargs)
       for field in iter(self.fields):
           self.fields[field].widget.attrs.update({
               'class':'from-control'
           }) 
           self.fields['departamento_id'].label = 'Departamento de Ubicacion'

#class FKActivy (forms.ModelChoiceField):
    #def label_from_instance(self, obj):
        #return "{}".format(obj.estado)

class ClientForm (forms.ModelForm):
    class Meta:
        model = Clientes
        fields = ['cedula','nombre','apellido','correo','edad','peso','estatura','estado_id']
        labels = {'cedula':'Cedula','nombre':'Nombre','apellido':'Apellido','correo':'Correo','edad':'Edad','peso':'Peso','estatura':'Estatura'}
        widget = {'cedula':forms.TextInput(),'nombre':forms.TextInput(),'apellido':forms.TextInput(),'correo':forms.TextInput(),'edad':forms.TextInput(),'peso':forms.TextInput(),'estatura':forms.TextInput()}

    def __init__(self,*args,**kwargs):
       super().__init__ (*args,**kwargs)
       for field in iter(self.fields):
           self.fields[field].widget.attrs.update({
               'class':'from-control'
           }) 