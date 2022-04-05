from flask_restful import Resource , request 
from dtos.registro_dto import RegistroDTO , UsuarioResponseDTO , LoginDTO
from dtos.usuario_dto import ResetPasswordRequestDTO
from models.usuarios import Usuario
from config import conexion, sendgrid
from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from  os import environ
from cryptography.fernet import Fernet
from datetime import datetime, timedelta
import json
#from sendgrid.helpers.mail import Email, To, Content, Mail



class RegistroController(Resource):
    def post(self):
        #me da todo el body convertido en un diccionario
        body = request.get_json()
        try:
            data = RegistroDTO().load(body)
            nuevoUsuario = Usuario(**data)
            ## generar un hash de la contraseña
            nuevoUsuario.encriptar_pwd()
            conexion.session.add(nuevoUsuario)
            conexion.session.commit()
            respuesta = UsuarioResponseDTO().dump(nuevoUsuario)
            return {
            'message' : 'Usuario registrado exitosamente',
            'content' : respuesta
            },201
        except Exception as e:
            conexion.session.rollback()
            return {
                'message' : 'Error al registrar usuario',
                'content': e.args
            }, 400

class LoginController(Resource):
    def post(Self):
        body = request.get_json()
        #HAcer un dto que solamente recibaun correo y un pasword,el correo debe ser
        #email, no es necesario usar un SQLAlchemyAutoSchema
        try:
            data = LoginDTO().load(body)
            return {
                'message' : 'Bienvenido'
            }
        except Exception as e:
            return{
                'message' : 'Credenciales incorrectas',
                'content' : e.args
            }


class ResetPasswordController(Resource):
    def post(self):
        body = request.get_json()
        #------- UTILIZANDO LA LIBRERIA DE PYTHON DE MENSAJERIA-----
        mensaje = MIMEMultipart()
        email_emisor = environ.get('EMAIL_EMISOR')
        email_password = environ.get('EMAIL_PASSWORD')
        try:
            data = ResetPasswordRequestDTO().load(body)
            # validar si existe ese usuario en mi bd
            usuarioEncontrado = conexion.session.query(
                Usuario).filter_by(correo=data.get('correo')).first()
            if usuarioEncontrado is not None:
                texto= "Hola Luis, este es un mensaje de prueba"
                mensaje['Subject'] = 'Reiniciar Contraseña Monedero APP'

                #encriptacion de informacion
                Fernet.generate_key()
                fernet = Fernet(environ.get('FERNET_SECRET_KEY'))

                mensaje_secreto = {
                    'fecha_caducidad':str(datetime.now()+timedelta(hours=1)),
                    'id_usuario': usuarioEncontrado.id
                }
                mensaje_secreto_str = json.dumps(mensaje_secreto)
                mensaje_encriptado = fernet.encrypt(
                     bytes(mensaje_secreto_str, 'utf-8'))
                # FIN DE ENCRIPTACION

                #si queremos un generador de correos son diseño: https://beefree.io/
                html = open('./email_templates/joshua_template.html').read().format(
                    usuarioEncontrado.nombre, environ.get('URL_FRONT')+'/reset-password?token='+mensaje_encriptado.decode('utf-8'))
                   #  usuarioEncontrado.correo,            
                    #'/reset-password?token='+mensaje_encriptado.decode('utf-8'))
                # siempre que queremos agregar un HTML como texto del mensaje tiene que ir despues del texto ya que
                # primero tratara de enviar el ultimo
                #mensaje.attach(MIMEText(texto,'plain'))
                mensaje.attach(MIMEText(html,'html'))
                # Inicio el envio del correo 
                #                   SERVIDOR     PUERTO
                #ouloot > outlook.office365.com / 587
                #hotmail > smtp.live.com       / 587
                #gmail > smtp.mail.com         / 587
                #icloud > smtp.mail.me.com    / 587
                #yahoo > smtp.mail.yahoo.com /587
                emisorSMTP= SMTP('smtp-mail.outlook.com', 587)
                emisorSMTP.starttls()
                #se hace el login de mi servidor de correo
                emisorSMTP.login(email_emisor, email_password)
                #envio de correo
                emisorSMTP.sendmail(
                    from_addr=email_emisor,
                    to_addrs=usuarioEncontrado.correo,
                    msg=mensaje.as_string()
                )


            return{
                'message' : 'Luis Correo enviado exitosamente 8'
            }
        except Exception as e:
            return{
                'message' : 'Error al enviar correo',
                'content' : e.args
            }
        # try:
        #     data = ResetPasswordRequestDTO().load(body)
        #     # validar si existe ese usuario en mi bd
        #     usuarioEncontrado = conexion.session.query(
        #         Usuario).filter_by(correo=data.get('correo')).first()
        #     if usuarioEncontrado is not None:
        #         # tengo que utilizar los correos verificados en sendgrid ya que si uso uno que no esta verificado entonces el correo nunca llegara
        #         from_email = Email('ederiveroman@outlook.com')
        #         print(usuarioEncontrado.correo)
        #         from_email = Email('ederiveroman@gmail.com')
        #         to_email = To(usuarioEncontrado.correo)
        #         subject = 'Reinicia tu contraseña del Monedero App'
        #         content = Content(
        #             'text/plain', 'Hola, has solicitado el reinicio de tu contraseña, haz click en el siguiente link para cambiar, sino has sido tu ignora este mensaje: ....')
        #         mail = Mail(from_email, to_email, subject, content)
        #         envia_correo = sendgrid.client.mail.send.post(
        #             request_body=mail.get())
        #         # el estado de la respuesta de sendgrid
        #         print(envia_correo.status_code)
        #         # el cuerpo de la respuesta de sendgrid
        #         print(envia_correo.body)
        #         # las cabeceras de la respuesta de sendgrid
        #         print(envia_correo.headers)
        #     return {
        #         'message': 'Correo enviado exitosamente'
        #     }
        # except Exception as e:
        #     return {
        #         'message': 'Error al resetear la password',
        #         'content': e.args
        #     }