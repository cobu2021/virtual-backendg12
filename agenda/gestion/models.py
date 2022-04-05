from django.db import models

class Etiqueta(models.Model):
# Tipos de Columnas > https://docs.djangoproject.com/en/4.0/ref/models/fields/#field-types
#Opciones de las Columnas > https://docs.djangoproject.com/en/4.0/ref/models/fields/#field-options

    id=models.AutoField (primary_key=True, unique=True , null=False)
    nombre=models.Charfield(max_length=20 ,unique=True , null=False)

    #columnas de Auditoria
    #son las columnas que podran ayudar al seguimiento de la creacion de registros
    #createdAT > es la fecha en la que se creo el regisgtro
    createdAT=models.DateTimeField(auto_now_add=True, db_colunm='created_at')
    #updatedAT= es la fecha en la cual se modifico algun campo del registro
    updatedAT=models.DateTimeField(auto_now_add=True, db_colunm='updated_at')

    #todas las configuraciones propias de la tabla se haran mediante la definicion de sus
    #atributos en la clase meta

    #https://docs.djangoproject.com/en/4.0/ref/models/options/
    
    class Meta:
        #cambiar el nombre de la tabla en la bd (a diferencia del nombre de la clase)
        db_table = 'etiquetas'

        # modigicar el ordenamiento para el id imponiendo el propio
        ordering = ['-nombre']
