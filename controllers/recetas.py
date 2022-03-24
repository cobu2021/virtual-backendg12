from ast import excepthandler
from flask_restful import Resource , request
from models.recetas import Receta
from dtos.receta_dto import (RecetaRequestDTO, 
                            RecetaResponseDTO, 
                            BuscarRecetaResquesDto,
                            RecetaPreparacionesResponseDTO)
from dtos.paginacion_dto import PaginacionRequestDTO
from config import conexion
from math import ceil

# CREATE, GET ALL (PAGINATED), UPDATE,FIND por like de nombre , DELETE

class RecetasController(Resource):
    def post(self):
        recetas = conexion.session.query(Receta).all()
        respuesta = RecetaResponseDTO(many=True).dump(recetas)
        body = request.get_json()
        try :
            data=RecetaRequestDTO().load(body)
            #creamos la instancia de la nueva receta pero nola agregamos a la base de datos
            nuevaReceta = Receta(
                nombre = data.get('nombre'),
                estado = data.get('estado'),
                comensales=data.get('comensales'),
                duracion=data.get('duracion'),
                dificultad = data.get('dificultad')
                )
            
            conexion.session.add(nuevaReceta)
            #https://docs.sqlalchemy.org/en/14/orm/session_api.html#sqlalchemy.orm.Session.commit
            # recien al hace commit asignara el id correspondiente
            conexion.session.commit()
            respuesta = RecetaResponseDTO().dump(nuevaReceta)
            return{
                'message' : 'Receta creada exitosamente',
                'content':respuesta
            }, 201
        except Exception as e:
            #https://docs.sqlalchemy.org/en/14/orm/session_api.html#sqlalchemy.orm.Session.rollback
            conexion.session.rollback()
            return {
                'message' : 'Error al Crear la Receta',
                'content' : e.args
            }
    def get(self):
        # TODO: agregar paginacion
        #page > que pagina queremos
        # perPage
        query_params = request.args
        paginacion = PaginacionRequestDTO().load(query_params)
        perPage = paginacion.get('perPage')
        page = paginacion.get('page')
        if(perPage < 1 or page < 1):
            return {
                'mesagge' : 'Los parametros no pueden recibir valores negativos'
            }, 400

        skip = perPage * (page -1)
        recetas = conexion.session.query(Receta).limit(perPage).offset(skip).all()
        total = conexion.session.query(Receta).count()
        itemsXPage= perPage if total >= perPage else total
        totalPages = total / itemsXPage if itemsXPage > 0 else None
        prevPage = page - 1 if page > 1 and page <=totalPages else None
        nextPage = page + 1 if totalPages > 1 and page <totalPages else None         
        respuesta = RecetaResponseDTO(many=True).dump(recetas)
        return {
            'message' : 'Las recetas son:',
            'pagination':{
                'total':total,
                'itemsXPage' : itemsXPage,
                'totalPages' : totalPages,
                'prevPage' : prevPage,
                'nextPage' : nextPage
            },
            'content' : respuesta
        }

class BuscarRecetaController(Resource):
    def get(self):
        query_params = request.args
        try :
            parametros = BuscarRecetaResquesDto().load(query_params)
            
            # si es que no me dan a comocer el nombe entonces hare la busqueda de todas las recetas
            #el filter a comparacion del filter_by se se utiliza para comrparar valores
            #pero utilizando su atributo de la clase y se usa doble igual
            #si queremos usar algin filtro especifico del orm (de la BD) entonces usaremos
            #el atributo de la clase el cual nos devolvera metodos para hacer esa busqueda 
            #especifica
            recetas2= conexion.session.query(Receta).filter(Receta.nombre.like('%a%')).all()
           
            nombre = parametros.get('nombre', '')

            if parametros.get('nombre') is not None:
                del parametros['nombre']
            #hare la busqueda de todas lasrecetas y si me pasa el nombre hare una 
            #busqueda con su like y para las  demas columnas hare la busqueda normal
            recetas = conexion.session.query(Receta).filter(Receta.nombre.like('%{}%'.format(nombre))).filter_by(**parametros).all()
            resultado = RecetaResponseDTO(many=True).dump(recetas)
        
            return {
                'message':'',
                'content' : resultado
            }
        except Exception as e:
            return{
                'message' : 'error al crear receta',
                'content' : e.args
            }, 400

class RecetaController(Resource):
    def get(self, id):
        # buscar la receta segun su id
        receta : Receta | None = conexion.session.query(Receta).filter(Receta.id == id).first()
        # si nohay la receta devolverun message : 'REceta no encontrada' con un estado
        #NOT FOUND
        if receta is None:
            return{
                'message' : 'Receta no encontrada'
            }, 404
        # si hay la receta devolver message : 'receta encontrada' con un estado ok
        else :
            print (receta.preparaciones)
            respuesta = RecetaPreparacionesResponseDTO().dump(receta)
            return {
                'message' : 'Receta Encontrada',
                'content' : respuesta
            } , 200
        return{
            'id' : id
        }



    