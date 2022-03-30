from models.categorias import Categoria
from config import conexion
# leer en la bd si no existe categorias : 'ocio'. 'comida'.
#'educacion' , 'viajes'

def categoriaSeed():
    #si existe la categoria ya no se ingresa
    conexion.session.query(Categoria).filter(
        Categoria.nombre.like=='%OCIO', Categoria.nombre == 'COMIDA',
        Categoria.nombre =='EDUCACION', Categoria.nombre =='VIAJES').first()
    if categorias is not None:
        #creacion de esas categorias
        nombres = ['OCIO' , 'COMIDA' , 'EDUCACION', 'VIAJES']
        try:
            for categoria in nombres:
                nuevaCategoria = Categoria(nombre=categoria)
                conexion.session.add(nuevaCategoria)

            conexion.session.commit
            print('categorias creadas exitosamente')
        except Exception as e:
                conexion.session.rollback()
                print('Error al alimentar la base de datos')
