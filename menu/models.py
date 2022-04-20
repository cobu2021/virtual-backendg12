from django.db import models
from cloudinary import models as modelsCloudinary

# Create your models here.
class Plato(models.Model):
    #foto > ImageField()
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45, null=False)
    disponible = models.BooleanField(default=True, null=False)
    foto = modelsCloudinary.CloudinaryField(
        folder='plato')
    disponible=models.BooleanField(default=True, null=False)
    precio = models.FloatField(null=False)
# Welcome123!
    class Meta :
        db_table = 'platos'

class Stock(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField(null=False)
    cantidad = models.IntegerField(null=False)
    precio_diario = models.FloatField(null=False)

    #related_name > servira para ingresar desde el modelo del cual se esta
    #creando la relacion ( en este caso desde desde platos prodremos ingresar)
    #a todos sus stocks)

    #on_delete > que acccion tomara cuando se desee eliminar el padre (la PK)

    #CASCADE > eliminara el registro del plato y todos los stocks que tengan ese
    #registro tambien seran eliminados en cascada

    # PROTECT > impedira que se realice la eliminacion del plato si tiene stocks

    #SET_NULL > eliminara el plato y todos sus stocks colocando en su FK el valor 
    # de null

    # DO_NOTHING > eliminara el plato y no cambiara nada de los stocks
    # (seguira con el mismo valor ya elimindo)

    #RESTRICT > no permite la eliminacion y lanzara un error de tipo 
    #RestrictedError(hara un raise)

    platoId = models.ForeignKey (
        to=Plato, related_name='stocks' , on_delete=models.CASCADE,
         db_column='plato_id')

    class Meta :
        db_table = 'stocks'
    # unique_together > crea un indice de dos o mas columnas en el cual no se podran repetir
    #   fecha       Plato
    # 2022-04-18      1  si
    #2022-04-18       1  no
    #2022-04-18       2  si
    #2022-04-19       1  si


        unique_together = [['fecha' ,'platoId']]
    #https://docs.djangoproject.com/en/4.0/ref/models/options/#unique-together
   
    #https://docs.djangoproject.com/en/4.0/ref/models/fields/#django.db.models.ForeignKey.on_delete
    #https://www.postgresql.org/docs/current/indexes-unique.html#:~:text=PostgreSQL%20automatically%20creates%20a%20unique,mechanism%20that%20enforces%20the%20constraint.


