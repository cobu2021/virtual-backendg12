from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.generics import ListAPIView

@api_view(http_method_names=['GET' , 'POST'])
def inicio(request):
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
    seralizer_class = None