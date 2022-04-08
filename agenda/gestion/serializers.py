from rest_framework import serializers

from .models import Etiqueta, Tareas


class PruebaSerializer(serializers.Serializer):
    nombre= serializers.CharField(max_length=40 , trim_whitespace = True)
    apellido = serializers.CharField()
    correo = serializers.EmailField()
    dni = serializers.RegexField(min_length= 8, max_length= 8, regex="[0-9]")
#dni serializers. IntegerField(min_value=10000000, max:value=99999999)

class TareaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tareas
        fields = '__all__' #estare indicando que estare utilizando todas las columnas de mi tabla
        #exclude = ['importancia'] # indicara que columnas NO QUIERO utilizar
        # nota : no se puede utilizar los dos a la vez, es decir o bien se usa fiels o exclude

class EtiquetaSerializer(serializers.ModelSerializer):

    class Meta :
        model = Etiqueta
        fields = '__all__'