from django.db import models
from django.contrib.auth.models import AbstractBaseUser , PermissionsMixin

from .authManager import UserManager
#Create your models here.
#con la cual se usara en la bd y se mostrara la que se usuara en los formularios
class Usuario(AbstractBaseUser , PermissionsMixin):
        id = models.AutoField(primary_key=True)
        correo = models.EmailField(unique=True, null=False)
        password = models.TextField(null=False)
        nombre =  models.CharField(max_length=45 , null=False)
        rol = models.CharField(choices=(
            ['ADMINISTRADOR' , 'ADMINISTRADOR'],
            ['MOZO' , 'MOZO']), max_length=40)

        is_staff = models.BooleanField(default=False)

        is_active = models.BooleanField(default=True)

        createdAt = models.DateTimeField(auto_now_add=True, db_column='created_at')
   
        #comportamiento que tendra el modelo cuando se realice el comando createsuperuser
        objects = UserManager()

        #sera el campo que pedira aparte del password en el panel administrativo para hacer
        #el login

        USERNAME_FIELD = 'correo'

        #seran los atributos que me solicitaran por la consola al crear el superusuario
        #no van los campos especificos en el USERNAME_FIELD Y EL password
        REQUIRED_FIELDS = ['nombre', 'rol']

        class Meta :
            db_table = 'usuarios'
    
    

