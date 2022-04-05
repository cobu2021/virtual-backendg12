from config import conexion
from models.usuarios import Usuario
from bcrypt import checkpw

def autenticador(username, password):
    """Funcion encargada de valiadar si las credenciales son correctas o no, si 
    no son no pasara pero si si lo son retornara una jwt"""
    #priemro valido si los datos son correctos
    if username and password:
        #buscare el usuario en la bd
        usuarioEncontrado = conexion.session.query(
            Usuario).filter_by(correo=username).first()
        if usuarioEncontrado:
            print('se encontro el usuario')
            # ahora valido si  el password es el correct
            validacion = checkpw(bytes(password, 'utf-8'),
                         bytes(usuarioEncontrado.password,'utf-8'))
            if validacion is True:
                print('si es la contraseña')
                #si todas las validadciones son correctas entonces deneremos de retormar
                #un objeto con atributo id
                return usuarioEncontrado
            else:
                return None
        else:
            return None
    else:
        return None
    

def identificador(payload):
    """ Sirve para validar al usuario previamente autenticado"""
    usuarioEncontrado : Usuario | None = conexion.session.query(
        Usuario).filter_by(id=payload['identity']).first()
    if usuarioEncontrado:
        return {
            'id' : usuarioEncontrado.id,
            'nombre' : usuarioEncontrado.nombre,
            'correo' : usuarioEncontrado.correo
           }
    else:
        return None
    


        