from flask import Flask, render_template , request
from flask_jwt import JWT, jwt_required, current_identity
from flask_restful import Api
from controllers.usuarios import (LoginController,
                                  RegistroController,
                                  ResetPasswordController)
from config import validador, conexion
from os import environ
from dotenv import load_dotenv
from flask_cors import CORS
from dtos.registro_dto import UsuarioResponseDTO
from seguridad import autenticador, identificador
from datetime import timedelta
from models.usuarios import Usuario
from seed import categoriaSeed
from controllers.movimientos import MovimientoController
from cryptography.fernet import Fernet 
from datetime import datetime
import json

load_dotenv()

app = Flask(__name__)

CORS (app=app)

app.config['SECRET_KEY'] = environ.get('JWT_SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#para cambiar el endpoint de mi JWT
app.config['JWT_AUTH_URL_RULE'] = '/login-jwt'
#para cambiar la llave para solicitar el username
app.config['JWT_AUTH_USERNAME_KEY'] = 'correo'
#para cambiar la llave para solicitar el password
app.config['JWT_AUTH_PASSWORD_KEY'] = 'pass'
#para cambiar el tiempo de expiracion de mi jwt
app.config['JWT_EXPIRATION_DELTA'] = timedelta(hours=1 , minutes=5)
# Para indicar cual sera el prefijo de la token en los headers de authorizatio
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
    #render_template > renderiza un archivo .html o .jinja para flask lo que pueda leer e interpretar al cliete
    return render_template('inicio.jinja', nombre='Eduardo', dia='Jueves' , integrantes=[
    'Foca',
    'Lapagol',
    'Ruizdiaz'
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
        'nombre': 'Brasil',
        'clasificado': True
    },{
        'nombre': 'chile',
        'clasificado' : False
    },{
        'nombre': 'Peru',
        'Timado' : True 
    }])


@app.route('/status')
def estado():
    return {
        'status' : True,
        'hora_del_servidor' : datetime.now().strftime('%Y-%m-%d  %H:%M:%S')
    }, 200


# al colocar jwt_required estamos indicando que para ese controlador se debera de proveer una JWT valida
@app.route('/yo')
@jwt_required()
def perfil_usuario():
    print(current_identity)
    #serializar el usuario(current Identity)
    usuario = UsuarioResponseDTO().dump(current_identity)
    return {
        'message' : 'El usuario es',
        'content' : usuario
    }
@app.route('/validar-token', methods=['POST'])
def validar_token():
    # TODO : agregar el dto para solamente recibir la token en el body, la token tiene
    # que ser un string
    body = request.get_json()
    token = body.get('token')
    print(token)
    fernet = Fernet(environ.get('FERNET_SECRET_KEY'))
    try:
        #el metodo cecrypt se usa para decifar la token previamnte encriptada si no se
        #puede se emitira un error que sera capturado por el except
        #token laconv a bytes - el resultado de buytes lo conbvierto a str
        data = fernet.decrypt(bytes(token, 'utf-8')).decode('utf-8')
        print(data)
        diccionario = json.loads(data)
        fecha_caducidad =datetime.strptime(diccionario.get('fecha_caducidad'),'%Y-%m-%d %H:%M:%S.%f')
        print(fecha_caducidad)
        hora_actual = datetime.now()
        if hora_actual < fecha_caducidad:
              print(conexion.session.query(Usuario).with_entities(
                  Usuario.correo).filter_by(id=diccionario.get('id_usuario')))
              
              #buscar ese usuairo en la bd y retornar al front el nombre del usuario
              usuarioEncontrado = conexion.session.query(Usuario).with_entities(
                  Usuario.correo).filter_by(id=diccionario.get('id_usuario')).first()
              if usuarioEncontrado:
                  return {
                      'message':'correcto',
                      'content':{
                          'correo' : usuarioEncontrado.correo
                  }
                  }
             
              else:
                return {
                     'message' : 'Usuario no Existe'
               },400
        else:
             return {
            'message' : 'La token caduco'
        },400

    except Exception as e:
        print(e.args)
        return {
            'message' : 'Token Incorrecta'
        }, 400

@app.route('/change-password-token')
def post(self):
    body= request.get_json()
    try:
        #primero valido la informacion entrante del body
        data = ChangePasswordRequestDTO().load(body)
        fernet = Fernet(environ.get('FERNET_SECRET_KEY'))


        info_token = 







api.add_resource(RegistroController, '/registro')
api.add_resource(LoginController, '/Login')
api.add_resource(MovimientoController, '/movimiento', '/movimientos')
api.add_resource(ResetPasswordController, '/reset-password')


if(__name__ == '__main__'):
    app.run(debug=True , port=8080)