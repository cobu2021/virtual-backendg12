import unittest
# por defecto el patron del nombre de los archivos es tesr*.py, si queremos modificar el patron
#usaremos la configuracion -p / --pattern

#si queremos ver el detalle de  nuestros  casos de test usaremos -v / --vervose

def numero_par(numero: int):
    #retorna verdadero si es par o falso se es impar
    return numero % 2 == 0

#todo escenario de testing (pruebas) sera basado en clases
class PruebaTest(unittest.TestCase):
    #la clase TestCase me permite hacer hacer varios tipos de
    #compraraciones y ademas le indcar a python que clase de testing
    #debe hacer

    # cada escenario de prueba sera un metodo
    def test_sumatoria(self):
        numero1 = 1
        numero2 = 2
        resultado = numero1  + numero2
        #comprobar si numero1 + numero2 = 3
        self.assertEqual(resultado, 3)

        #si estamos concientes qie el test va a fallar pero aun asi queremos
        #mantenerlo tal y como esta, entonces entonces podemos usar el decorador
        #expectedFailure que no nos indicara un fallo pero que se espera el fallo

    @unittest.expectedFailure
    def test_resta(self):
        numero1 = 1
        numero2 = 2
        resultado = numero1 - numero2
        #comprobar si numero1 - numero2 = 3
        self.assertEqual(resultado, 3)

class NumeroParTest(unittest.TestCase):
    # los metodos siempre deben de empezar con 'test_' por que si no
    # lo colocamos no lo considera al momento de hacer test
    def test_par(self):
        #pasare un numero
        resultado = numero_par(2)
        self.assertEqual(resultado, True)

    def test_impar(self):
        #pasare un numero
        resultado = numero_par(3)
        self.assertEqual(resultado, False)



    def test_error(self):
        '''Debera arrojar un error se se le pasa una letra en vez de un numero'''
        # pasare algo que no sea un numero
        #si se que el siguiente test fallara pero es parte del caso entonces
        #puedo usar el  assertRaises que lo que recibira sera el tipo de error que
        #va a generar para poder testearlo
        with self.assertRaises(TypeError , msg='Error al ingresar un caracter en vez de un numero_par') as error:
            numero_par('a')

            self.assertEqual(
                error.msg, "Error al ingresar un caracter en vez de un numero")

