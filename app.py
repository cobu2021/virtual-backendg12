from flask import Flask
from datetime import datetime
from flask_restful import Api
from  controllers.ingredientes import (
                                        IngredientesController,
                                        PruebaController,
                                        IngredienteController
                                      )
from controllers.recetas import (RecetasController, 
                                  BuscarRecetaController,
                                  RecetaController)
from controllers.preparaciones import PreparacionesController
from controllers.ingredientes_recetas import IngredientesRecetasController
from config import conexion , validador
from dotenv import load_dotenv
from os import environ

# carga todas las variables definidas en el archvo .env para que sean tratadas como
# variables de entono sin la necedidad
load_dotenv()

print(environ.get('NOMBRE'))


app = Flask(__name__)
#creamos la instantancia de flask:resful.api y le indicamos que toda la configuracion
#que haremos se agrege a nuestra instancia de Flask
api = Api(app=app)



# se almacenaran todas las variables de configuracion de mi proyecto Flask, en ella
#se podran encontrar algunas variables como DEBUG Y ENV, entre otras
#app.config > es un diccionrio en el cual se almacenaran las variables por Llave:Valor
#  print(app.config)

#Ahora asignaremos la cadena de conexion a nuestra base de datos
#tipo://usuario:password@dominio:puerto/base_de_datos
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:cobu@127.0.0.1:3306/recetario'
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL')
#cion de mi flask y extraer su conexion a la base de datos
conexion.init_app(app)

#con el siguiente comando indicaremos la creacion de todas las tablas en la bd
#emitara un error si que no hay una tabla a crear
#emitira un error si no le hemos instalado el conector correctamente
conexion.create_all(app=app)



@app.route('/status', methods=['GET'])
def status() :
    return {
        'status' : True,
        'date':   datetime.now() .strftime('%Y-%m-%d %H:%M:%S')
         }

@app.route('/')
def inicio():
    return 'Bienvenido a mi Api de recetas'
#ahora definiremos una ruta que van a ser utilizados con un determinado
#controlador
api.add_resource(IngredientesController, '/ingredientes','/ingrediente')
api.add_resource(PruebaController, '/pruebas')
api.add_resource(IngredienteController, '/ingrediente/<int:id>')
api.add_resource(RecetasController, '/recetas','/receta')
api.add_resource(BuscarRecetaController, '/buscar_receta')
api.add_resource(PreparacionesController, '/preparacion')
api.add_resource(RecetaController, '/receta/<int:id>')
api.add_resource(IngredientesRecetasController, '/ingrediente_receta')
#comprobara que la instancia de la clase Flask se este ejecutando en el archivo 
#principal del proyecto,esto se usa para no crear multiples instancias y bgenerar
#un posible error de Flask

if __name__=='__main__':
    app.run(debug=True)

