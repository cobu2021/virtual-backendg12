from rest_framework.permissions import BasePermission , SAFE_METHODS
from rest_framework.request import Request

class SoloAdminPuedeEscribir(BasePermission):
    def has_permission(self,request,view):
        # view > es la vista a la cual intenta acceder el usuario,esto 
        #dependera de donde se coloque el middleware

        #Middlewares > es un intermediario entre la peticion del front y la 
        #logica final(Se encargara de validar si cumple o no cumple determinados
        # reqs y si no cumple no podra continuar)

        #el request nos dara toda la informacion de los atributos de la peticion
        #en los custtom premission SIEMPRE hay que retomar True o False para
        #indicar si cumle o mo con los permisos determinados
        print(request.user)
        print(request.user.nombre)
        print(request.user.rol)
        #auth > imprimira la token de autenticacion que se usa para esta solicitud(request)
        print(request.auth)
        #SAFE_METHODS > son los metodos que el usuario no podra modificar la
        #informacion del backend , son GET, HEAD, OPTIONS
        print(request.method)

        print(SAFE_METHODS)
        print(type(view))
        #print(str(type(view))) == "<ctolass 'menu.views.StockApiview>"
        #hacemos determinada validacion si solamente queremos hacer una validacion
        #para una determinada vista
        # if str(type(view))  == "<class 'menu.views.StockApiView"
        #     return request.user.rol == 'ADMINISTRADOR'
        # METODO LARGO (semana 1)

        # si ES GET, HEAD, OPTIONS NO necesito validar si es ADMINISTRADOR O MOZO
        if request.method in SAFE_METHODS:
            return  True
        # SI es POST necesitara validar si es ADMINISTRADOR
        else:
            return request.user.rol == 'ADMINISTRADOR'

        #return True if request.method in SAFE_METHODS else request.user.rol == 'ADMINISTRADOR'

        
        
       # return request.user.rol == 'ADMINISTRADOR'
       # if request.user.rol == 'ADMINISTRADOR':
        #    return True
        #else:
         #   return False
class SoloMozoPuedeEscribir(BasePermission):
    def has_permission(self,request: Request, view):
        if request.method == SAFE_METHODS:
            return True
        else:
            return request.user.rol == 'MOZO'