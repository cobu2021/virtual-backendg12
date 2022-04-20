from .models import Plato , Stock
from rest_framework.generics import CreateAPIView, ListCreateAPIView
from .serializers import PlatoSerializer, StockSerializer
from rest_framework.permissions import (AllowAny, 
IsAuthenticated,IsAuthenticatedOrReadOnly,
IsAdminUser)
from rest_framework.response import Response
from rest_framework.request import Request
from cloudinary import CloudinaryImage
from .permissions import SoloAdminPuedeEscribir

# AllowAny > sirve para que el contralador sea publico(no se necesita
#  una token)

# IsAuthenticated Solamente para los metodos GET no sera necesaria 
# la token pero para los demas metodos (POST,PUT,DELETE,PATCH) 
# si sera requerido

# IsAuthenticatedOrReadOnly)  > Verifica que en la token de acceso buscara
#al usuario y vera si es superuser (is_superuser)
class PlatoApiView(ListCreateAPIView):
    serializer_class = PlatoSerializer
    queryset = Plato.objects.all()
    # que tipo de permisos necesita el cliente para realizar la peticion
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request: Request):
        data = self.serializer_class(instance=self.get_queryset(), many=True)
        #hacer una iteracion para modificar la foto de cada plato y devolver el link de la foto
        
        print(data.data[1])
        print(data.data[1].get('foto'))
        #del contenido de la foto solamente extraer el nombre del archivo o si esta
        #en una carperta extraer la carpeta y el archivo
        link = CloudinaryImage('plato/x1kdxvg5jexercpudtuc.jpgsourvesou').image(secure=True)

        print(link)
        return Response(data=data.data)

class StockApiView(ListCreateAPIView):
    serializer_class = StockSerializer
    queryset = Stock.objects.all()
    permission_classes = [IsAuthenticated, SoloAdminPuedeEscribir]





