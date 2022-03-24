from config import conexion
from sqlalchemy import Column , types, orm 
from sqlalchemy.sql.schema import ForeignKey

class IngredientesRecetas(conexion.Model):
    id = Column(type_=types.Integer, autoincrement=True, primary_key=True)
    unidad_medida = Column(type_=types.String(length=45), nullable= False )
    #Hacer las demas columnas que serian las relaciones
    ingrediente_id = Column(ForeignKey(column='ingredientes.id'), type_=types.Integer)
    receta_id = Column(ForeignKey(column='recetas.id'), type_=types.Integer)

    ingrediente = orm.relationship('Ingrediente', backref='ingredientes_recetas')
    receta = orm.relationship('Receta', backref='receta_ingredientes')
    __tablename__ = 'ingredientes_recetas'