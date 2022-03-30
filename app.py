from datetime import timedelta
from flask import Flask , render_template
from flask_restful import Api
from controllers.usuarios import RegistroController ,LoginController 
from controllers.movimientos import MovimientoController

from config import validador, conexion
from os import environ
from dotenv import load_dotenv
from flask_cors import CORS
from flask_jwt import JWT , jwt_required , current_identity
from seed import categoriaSeed
from seguridad import autenticador, identificador 
from dto.registro_dto import UsuarioResponseDTO


load_dotenv()

app = Flask(__name__)

CORS (app=app)
app.config['SECRET_KEY'] = environ.get('JWT_SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL')
#para cambiar el endpoint de mi JWT
app.config['JWT_AUTH_URL_RULE'] = '/login-jwt'
#para cambiar la llave para solicitar el username
app.config['JWT_AUTH_USERNAME_KEY'] = 'correo'
#para cambiar la llave para solicitar el password
app.config['JWT_AUTH_PASSWORD_KEY'] = 'pass'
#para cambiar el tiempo de expiracion de mi jwt
app.config['JWT_EXPIRATION_DELTA'] = timedelta(hours=1 , minutes=5)
app.config['JWT_AUTH_HEADER_PREFIX'] = 'Bearer'


jsonwebtoken = JWT(app=app, authentication_handler=autenticador,
                    identity_handler=identificador)

api = Api(app=app)
validador.init_app(app)
conexion.init_app(app)
# conexion.drop_all(app=app)
conexion.create_all(app=app)

#ingresara antes de hacer el primer request a nuestra funcion, toda la logica que queramos
#que se haga antes de la primera solicitud la deberemos de colocar aqui

@app.before_first_request
def seed():
    # ahora hacemos el seed de las tablas respectivas
    categoriaSeed()

@app.route('/')
def inicio():
    pass
@app.route('/yo')
@jwt_required()
def perfil_usuario():
    print(current_identity)
    #serializar el usuario(current Identity)
    usuario = UsuarioResponseDTO().dump(current_identity)
    return {
        'messge' : ' El usuario es',
        'content' : usuario
    }


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