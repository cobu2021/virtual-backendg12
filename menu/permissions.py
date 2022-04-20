from rest_framework.permissions import BasePermission
from rest_framework.request import Request

class SoloAdminPuedeEscribir(BasePermission):
    def has_permission(self,request,view):
        #el request nos dara toda la informacion de los atributos de la peticion
        #en los custtom premission SIEMPRE hay que retomar True o False para
        #indicar si cumle o mo con los permisos detemoina
        print(request.user)
        return True