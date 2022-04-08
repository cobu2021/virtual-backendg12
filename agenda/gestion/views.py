from importlib.resources import contents
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.generics import ListAPIView, ListCreateAPIView
from .models import Etiqueta, Tareas 
from .serializers import PruebaSerializer, TareaSerializer , EtiquetaSerializer


@api_view(http_method_names=['GET' , 'POST'])
def inicio(request : Request ):
    #request sera toda la informacion enviada para el cliente
    #https://www.django-rest-framework.org/api-guide/requests/
    print(request.method)
    print(request)
    if request.method == 'GET':
        #comportamiento cuando sea get
        return Response(data={
        'message' : 'Bienvenido a mi API de agenda'
    })
    elif request.method == 'POST':
        #COMPORTAMIENTO CUANDO SEA POST 
        return Response(data={
            'message' : 'Hiciste un Post'
        } , status=201)


class PruebaApiView(ListAPIView):
    serializer_class = PruebaSerializer
    #queryset > encargado de hacer la busqueda para este
    #controlador(para todos sus metodos)
    queryset = [{
        'nombre':'Eduardo', 
        'apellido': 'De Rivero', 
        'correo':'ederiv@gmail.com',
        'dni':'73500746', 
        'estado_civil':'viudo'},
        {
        'nombre':'Maria', 
        'apellido': 'Gutierrez', 
        'correo':'Mgutierrezv@gmail.com',
        'dni':'09811230', 
        'estado_civil':'Casada'}]
        
    def get(self,request: Request):
        #dentro de las vistas genericas se puede sobre escribir la
        #logica inicial del controlador
        # Si modifico la logica original de cualquier generico en
        #base a su metodo a utilizar ya no sera necesario definir los
        #atributos serializer_class y queryset ya que estos se usan
        #para cuando no se modifica la logica original
        informacion = self.queryset
        #Uso el serializador par filtrar la informacion necesaria y no
        #mostrar alguna informacion de mas pero en este caso como le voy a pasar uno o mas
        #registros de usuario entonces entonces para que el serializador los pueda iterar
        #le coloco el parametro many=True que lo que hara sera iterar
        informacion_serializada = self.serializer_class(data=informacion,
        many=True)
        informacion_serializada.is_valid(raise_exception=True)
        #para utilizar la informacion serializada OBLIGATORIAMENTE ten que llamar al metodo
        #is:_valid() el cual internamnete hara la validacion de los campos y sus configuraciones
        #el parametro raise_exception hara la emision del error si es que hay indicando cual
        #es el error
        return Response(data={
            'message': 'HOLA', 
            'content': informacion_serializada.data
            })


class TareasApiView(ListCreateAPIView):
    queryset=Tareas.objects.all() # Select * from tareas
    serializer_class = TareaSerializer

class EtiquetasApiView(ListCreateAPIView):
    queryset = Etiqueta.objects.all()
    serializer_class = EtiquetaSerializer