from config import validador
from models.preparaciones import Preparacion
from models.recetas import Receta
from marshmallow import fields



class PreparacionRequestDTO(validador.SQLAlchemyAutoSchema):

    class RecetaResponseDTO(validador.SQLAlchemyAutoSchema):
        class Meta:
            model = Receta
    
    class Meta :
        model = Preparacion
        # si queremos que el DTO tambien valide el tipo de dato y algunas
        #propiedades que les hemos dado a nuestra relacion entonces tendremos que
        #agregar el atributo include_fk para que incluya en las validaciones a esa
        #llave foranea
        load_instance = True
        include_fk = True

class RecetaResponseDTO(validador.SQLAlchemyAutoSchema):
    class Meta:
        model = Receta
                
class PreparacionResponseDTO(validador.SQLAlchemyAutoSchema):
    # Nested > es un tipo de campo que sirve para relacionar un DTO 
        # con otro DTO y usamos el parametro nested para indicar a que DTO 
        # nos queremos relacionar, tiene que ser el mismo nombre que
        #  el relationship pero si quisieramos tener un nombre diferente
        #  entonces agregamos el parametro data_key en el cual indicaremos 
        # como se llamara nuestra llave en el resultado pero de igual forma 
        # tendremos que utilizar el nombre de nuestro relationship como 
        # atributo de la clase
    receta = fields.Nested(nested=RecetaResponseDTO, data_key= 'receta_relacion')
    class Meta:
        model = Preparacion
        #Cargara las instancias  relacionadas con la preparacion
        load_instance = True
        include_fk = True
        include_relationships = True