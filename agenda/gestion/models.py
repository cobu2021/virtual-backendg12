from django.db import models

class Etiqueta(models.Model):
# Tipos de Columnas > https://docs.djangoproject.com/en/4.0/ref/models/fields/#field-types
#Opciones de las Columnas > https://docs.djangoproject.com/en/4.0/ref/models/fields/#field-options

    id=models.AutoField (primary_key=True, unique=True , null=False)
    nombre=models.CharField(max_length=20 ,unique=True , null=False)

    #columnas de Auditoria
    #son las columnas que podran ayudar al seguimiento de la creacion de registros
    #createdAT > es la fecha en la que se creo el regisgtro
    createdAT=models.DateTimeField(auto_now_add=True, db_column='created_at')
    #updatedAT= es la fecha en la cual se modifico algun campo del registro
    updatedAT=models.DateTimeField(auto_now_add=True, db_column='updated_at')

    #todas las configuraciones propias de la tabla se haran mediante la definicion de sus
    #atributos en la clase meta

    #https://docs.djangoproject.com/en/4.0/ref/models/options/
    
    class Meta:
        #cambiar el nombre de la tabla en la bd (a diferencia del nombre de la clase)
        db_table = 'etiquetas'

        # modigicar el ordenamiento para el id imponiendo el propio que sea ASC del
        #nombre, solamente funcionara para cuando hagamos el get usando el ORM
        ordering = ['-nombre']

class Tareas(models.Model):

    class CategoriaOpciones(models.TextChoices):

        # Cada opcion le pordemos pasar dos parametros en la cual el primero
        #sera su abreviatura para que se guarde en la bd y el segundo completo
        #que se mostrara cuando queramos utilizar los valores en un formulario
        #usando TEmplates(Jinja) o dentro del formulario de DRF
        TODO= 'TODO', 'TO_DO'
        IN_PROGRESS = 'IP' , 'IN_PROGRESS'
        DONE = 'DONE' , 'DONE'
        CANCELLED = 'CANCELLED' ,'CANCELLED'


    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45, null=False)
    categoria = models.CharField(max_length=45 , choices=CategoriaOpciones.choices,
    default=CategoriaOpciones.TODO)
    



    # Forma 2 usando una lista de tuplas
    # categoria = models.CharField(max_length=45 , choices=[
    # ('TODO', 'TO_DO'),
    # ('IP', 'IN_PROGRESS'),
    # ('DONE', 'DONE'),
    # ('CANCELLED', 'CANCELLED')
    # ],default='TODO')

    fechaCaducidad= models.DateTimeField(db_column='fecha_caducidad')
    importancia= models.IntegerField(null=False)
    descripcion = models.TextField(null=True)

    createdAT = models.DateTimeField(auto_now_add=True , db_column='create_at')
    updatedAT = models.DateTimeField(auto_now_add=True , db_column='update_at')

    # En Django se puede utilizar las relaciones one-to-one. pne-to-many o
    #many-to-many para crear las relaciones entre tablas, aca ya no es necesario
    #usar las relarionships porque ya estan integradas dentro de la relacion
    etiquetas = models.ManyToManyField(to=Etiqueta, related_name='tareas')

    foto=models.ImageField(
        upload_to='multimedia', # servirta para indicar donde se guarda las imagenes y si
         null=True                        # no existe, creara la carpeta
    )
    class Meta:
        db_table = 'tareas'

# Si la tabla tareas_etiquetas no fuese una tabla pivote, detalle entonces tendria
#que crear la tabla como si fuese uan tabla comun y corriente

#class TAreasEtiquetas(models.Model) :
#
#       etiquetaFK = models.ForeingnKey(to=Etiqueta)
#       tareaFK = models.ForeignKey(to=Tareas)
#       las demas tareas