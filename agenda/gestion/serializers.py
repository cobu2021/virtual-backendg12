from rest_framework import serializers


class PruebaSerializer(serializers.Serializer):
    nombre= serializers.CharField(max_length=40 , trim_whitespace = True)
    apellido = serializers.CharField()
    correo = serializers.EmailField()
    dni = serializers.IntegerField(min_value= 8, min_length= 8, regex="[0-9]")
#dni serializers. IntegerField(min_value=10000000, max:value=99999999)
    