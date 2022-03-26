import string
from config import conexion
from sqlalchemy import Column, types
from bcrypt import hashpw, gensalt

class Usuario(conexion.Model):
    __tablename__ = 'usuarios'
    id = Column(type_=types.Integer, primary_key=True , autoincrement= True)
    nombre = Column(type_=types.String(length=45))
    apellido = Column(type_=types.String(length=45))
    correo = Column(type_=types.Text(), nullable=False)
    password = Column(type_=types.Text(), nullable=False)

    def encriptar_pwd(self):
        #primero el password lo convierto a bytes
        password_bytes = bytes(self.password, 'utf-8')
        #usamos el metodo gensalt para generar un hash aleatorio y este se combinara
        #con mi contraseñba para generar un nuevo hash que ese sera el que guardaremos
        #en la base de datos
        salt = gensalt(rounds=10)
        hash_password = hashpw(password_bytes, salt)
        #ahora lo convierto a string para poder guardarlos en la base de datos
        hash_pwd_string = hash_password.decode('utf-8')
        #sobre escribo el valor del password en la intancia por el generado
        self.password = hash_pwd_string