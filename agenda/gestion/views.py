from importlib.resources import contents
from telnetlib import STATUS
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.generics import (ListAPIView, 
                                    ListCreateAPIView,
                                    RetrieveUpdateDestroyAPIView,
                                    CreateAPIView,
                                    DestroyAPIView)
                                    
from .models import Etiqueta, Tareas 
from .serializers import (PruebaSerializer, 
                          TareasSerializer ,
                           EtiquetaSerializer,
                           TareaSerializer,
                           TareaPersonalizableSerializer,
                           ArchivoSerializer,
                           EliminarArchivoSerializer)
from rest_framework import status
# son un conjunto de librerias que django nos provee para poder utilizar de una manera
#mas rapida ciertas configuraciones.
#timezone sirve oara que en base a la configuracion que colocamos en el settings.py
from django.utils import timezone
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from os import remove
from django.conf import settings 


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
    serializer_class = TareasSerializer

    def post(self,request: Request):
        serializador = self.serializer_class(data=request.data)
        if serializador.is_valid():
            #serializador.initial_data> data inicial sin la validacion
            #serializador.validated_data > data ya validada (solo se puede llamar
            # luego de llamar al metodo is_valid())
            #validare que la fecha_caducidad no sea menor que hoy
            fechaCaducidad = serializador.validated_data.get('fechaCaducidad')
            print(type(serializador.validated_data.get('fechacaducidad')))
            #validar que la importancia se entre 0 y 10
            importancia = serializador.validated_data.get('importancia')
            if importancia < 0 or importancia > 10:
                return Response(data={
                    'message' : 'La importancia puede ser entre 0 y 10'
                }, status=status.HTTP_400_BAD_REQUEST)
            if timezone.now() > fechaCaducidad:
                return Response(data={
                'message' : 'La fecha no puede ser menor que la fecha actual'
                 }, status=status.HTTP_400_BAD_REQUEST)
            #El metodo save() se podra llamar siempre que el serializado sea un ModelSerializador
            
            serializador.save()

            return Response(data=serializador.data, status=status.HTTP_201_CREATED)
        else:
            # mostrara todos los errores que hicieron que el is_valid() no cumpla la condicion
            #serializador.errors
            return Response(data={
                'message' : 'La data no es valida', 
                'content' : serializador.errors},
                status=status.HTTP_400_BAD_REQUEST)


class EtiquetasApiView(ListCreateAPIView):
    queryset = Etiqueta.objects.all()
    serializer_class = EtiquetaSerializer

class TareaApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = TareaSerializer #TAreaPersonalizableSerializer
    queryset = Tareas.objects.all()


class ArchivosApiView(CreateAPIView):
    serializer_class = ArchivoSerializer

    def post(self,request:Request):
        print(request.FILES)
        queryParams = request.query_params
        carpetaDestino = queryParams.get('carpeta')

        data= self.serializer_class(data=request.FILES)
        if data.is_valid():
            print(data.validated_data.get('archivo'))
            #https://docs.djangoproject.com/es/4.0/_modules/django/core/files/uploadedfile/
            archivo:InMemoryUploadedFile = data.validated_data.get('archivo')
            print(archivo.size)
            #solamente subir imagenes de hasta 5mb
            #5(bytes) * 1024 > (kb) * 1024 > (mb)
            #5 * 1024 * 1024
            if archivo.size > (5* 1024 * 1024):
                return Response(data={
                    'message' : ' Archivo muy grande, no se puede ser masde 5MB'
                } , status= status.HTTP_400_BAD_REQUEST)

            #https://docs.djangoproject.com/en/4.0/topics/files/#storage-objects
            resultado = default_storage.save(
                (carpetaDestino+'/' if carpetaDestino is not None else'')+archivo.name, ContentFile(archivo.read()))
            print(resultado)
            return Response(data={
                'message': 'archivo guardado exitosamente',
                'content' :{
                    'ubicacion' : resultado
                      #'ubicacion' : archivo.name
                }
                },status=status.HTTP_201_CREATED)
        else:
            return Response(data={
               'message': 'Error al subir imagen',
               'content' : data.errors
             }, status=status.HTTP_400_BAD_REQUEST)

class EliminaArchivoApiView(DestroyAPIView):
    # El generico DestroyAPIView solicita un pk como parametro de la url para eliminar
    #un detetminado registro de unmodelopero se personalizara para no recibir ello
    serializer_class = EliminarArchivoSerializer
    

    def delete(self, request: Request):
        data = self.serializer_class(data=request.data)
        try :
                data.is_valid(raise_exception=True)
                ubicacion = data.validated_data.get('archivo')
                remove(settings.MEDIA_ROOT/ ubicacion)
                return Response(data={
                    'message' : 'Archivo elimido exitosamente'
                })   
        except Exception as e:
            return Response(data={
                'message': 'No se encontro el archivo a eliminar',
                'content' : e.args
            }, status=status.HTTP_404_NOT_FOUND)

