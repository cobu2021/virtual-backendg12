from rest_framework import serializers

from .models import Etiqueta, Tareas


class PruebaSerializer(serializers.Serializer):
    nombre= serializers.CharField(max_length=40 , trim_whitespace = True)
    apellido = serializers.CharField()
    correo = serializers.EmailField()
    dni = serializers.RegexField(min_length= 8, max_length= 8, regex="[0-9]")
#dni serializers. IntegerField(min_value=10000000, max:value=99999999)

class TareasSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tareas
        fields = '__all__' #estare indicando que estare utilizando todas las columnas de mi tabla
        #exclude = ['importancia'] # indicara que columnas NO QUIERO utilizar
        # nota : no se puede utilizar los dos a la vez, es decir o bien se usa fiels o exclude
        extra_kwargs = {
            'etiquetas':{
                'write_only' : True
            }
        }

        #depth = 2 # en el caso que querramos devolver la informacion de una relacion
                  # entre este modelo podemos indicar hasta que grado de profundidad
                  #queremos que nos devuelva la informacion, la profundidad maxima
                  # es hasta 10

                  # la profundidad solamante funcionara cuando el modelo en el cual lo
                  #estamos utilizando sea el modelo en el cual 

class TareaSerializer(serializers.ModelSerializer):
        class Meta:
            model = Tareas
            fields = '__all__'
            depth = 1
class EtiquetaSerializer(serializers.ModelSerializer):
    #indicare que este atributo solamente funcionara para cuando vamos a serializar
    #la data antes de devolverla mas no cuando querramos usarla para escritura
    #se tiene que llamar igual que related_name para poder ingresar a esa relacion o 
    #podremos definir el parametro source en el cual colocaremos el nombre  del related_name
    #Nota : no podemos utilizar el parametro source si es que tambien colocaremos el mismo valor
    #como nombre de atributo
    tareas= TareasSerializer(many=True, read_only=True) #, source='tareas')
    class Meta :
        model = Etiqueta
        fields = '__all__'
        #extra_kwargs y read_only_fields solamente funcionaran para cuando
        #nosotros queramos modificar el comportamiento de los atributos 
        #que no los hemos modificado manualmente dentro del serializador
        #extra_kwargs y read_only_fields solamente funcionara para cuando nosotros querramos
        #modificar el comportamiento de los atriburos qie no los hemos modificado manualmente dentro
        #del serializador
        extra_kwargs={
            #'nombre' : {
            #    'write_only': True
            #    },
              'id': {
                  'read_only': True
                  }
        }
        #los campos del modelo que solamente quiero que sean lectura los podre definir en una lista

        read_only_fields=['createAt']