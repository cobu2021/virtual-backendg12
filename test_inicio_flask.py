import unittest
from app import app
from datetime import datetime

class TestInicioFlask(unittest.TestCase):
    def setUp(self):
        self.aplicacion_flask = app.test_client()
        # en vez del constructor en las clases comun y corrientes, en los tesr se usa
        #el metodo setup que servira para configurar todos los atributos y demas cosas
        #que vayamos a utilizar en los escenarios de tesr de esta clase (metodos)
        self.nombre = 'Eduardo'
    @unittest.skip('era prueba de funcionamiento setup')
    def testNombre(self):
        self.assertEqual(self.nombre,'Eduardo')
        #inicia mi apliacion de flash usando un cliente de test, aceptara periciones http para
        #probar los endpoints y toda la aplicacion en general, esto levantara los modelos
        #y hara la conexion a la bd entre otras cosas
        self.aplicacion_flask = app.test_client()
    
    @unittest.skip('lo salte porque solamente queria ver el funcionamiento del metodo setup')
    def testNombre(self):
        self.assertEqual(self.nombre, 'Eduardo')
    
    def testEndpointStatus(self):
        '''deberia retornar la hora del servidor y su estado'''
        respuesta = self.aplicacion_flask.get('/status')
        print(respuesta)
        #el body de la respuesta lo obtenemos de repuesta.json en cual nos devolvera un
        #diccionario con el json de la rpta
        #print(respueta.json)
        # https://strftime.org/
        self.assertEqual(respuesta.status_code, 200)
        self.assertEqual(respuesta.json.get('status'),True)
        self.assertEqual(respuesta.json.get('hora_del_servidor'),
                          datetime.now().strftime('%Y-%m-%d  %H:%M:%S'))

    def testLoginJWTExitoso(self):
        '''deberia retornar una token para poder ingresar a las rutas protejidas'''
        #Mocks
        body = {
            'correo' : 'luis-carbajal@hotmail.es',
            'pass': 'cobu'
        }

        respuesta = self.aplicacion_flask.post('/login-jwt',json=body)
        self.assertEqual(respuesta.status_code, 200)
        #respuesta.json.get('access_token') != None
        self.assertNotEqual(respuesta.json.get('access_token'),None)
    
    def testLoginJWTCredencialesIncorrectas(self):
        ''' deberia retornar un error si las credenciales son incorrectas'''
        body = {
                'correo' : 'luis-carbajal@hotmail.es',
                    'pass': 'noescobu'
        }
        respuesta = self.aplicacion_flask.post('/login-jwt', json=body)
        #hacer las suposiciones correspondientes
        self.assertEqual(respuesta.status_code, 401)
        self.assertEqual(respuesta.json.get('access_token'), None)
        self.assertEqual(respuesta.json.get(
            'description'), 'Invalid credentials')

# una clase por cada endpoint
class TestYo(unittest.TestCase):
    def setUp(self):
        self.aplicacion_flask = app.test_client()
        body = {
             'correo' : 'luis-carbajal@hotmail.es',
             'pass': 'cobu'
        }
        respuesta = self.aplicacion_flask.post('/login-jwt', json=body)
        self.token = respuesta.json.get('access_token')
    
    
    def testNoHayjwt(self):
        pass

    def testPerfil(self):
        respuesta= self.aplicacion_flask.get(
            '/yo' , headers={'Authorization': 'Bearer {}'.format(self.token)})
        
        self.assertEqual(respuesta.status_code, 200)
        self.assertEqual(respuesta.json.get('message'), 'El usuario es')

##class TestMovimientos(unittest.Testcasa):
    # TODO : hacer los test para extraer los movimientos creados del usuario
    # TODO: hacer este test con todas las suposiciones
class TestMovimientos(unittest.TestCase):
    # TODO: hacer los test para extraer los movimientos creados del usuario, hacer el caso cuando se pase una JWT, cuando no se pase una token, cuando no tenga movimientos y cuando tenga movimientos
    pass