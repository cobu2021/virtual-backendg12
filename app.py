from pickle import FALSE
from flask import Flask , render_template
from flask_restful import Api
from controllers.usuarios import RegistroController ,LoginController
from config import validador, conexion
from os import environ
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL')

api = Api(app=app)
validador.init_app(app)
conexion.init_app(app)
# conexion.drop_all(app=app)
conexion.create_all(app=app)

@app.route('/')
def inicio():
    #render_template > renderiza un archivo .html o .jinja para flask lo que pueda leer e
    #interpretar al cliete
    return render_template('inicio.jinja', nombre='Eduardo', dia='Jueves' , integrantes=[
    'Foca',
    'Lapagol',
    'Paolin',
    'Rayo Advincula',
    ],usuario= {
        'nombre': 'juan',
        'direccion': ' las piedritas 105',
        'edad': '40'
    }, selecciones= [{
        'nombre' :'Bolivia',
        'Clasificado' : True
    },{
        'nombre': 'chile',
        'clasificado' : False
    },{
        'nombre': 'Peru',
        'Timado' : True 
    }])

api.add_resource(RegistroController, '/registro')
api.add_resource(LoginController, '/Login')
if(__name__ == '__main__'):
    app.run(debug=True , port=8080)