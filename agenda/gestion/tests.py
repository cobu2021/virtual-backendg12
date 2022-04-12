from django.test import TestCase
from rest_framework.test import APITestCase

# la clase APITestCase sirve para hacer caso ade test como unittest

class EtiquetasTestCase(APITestCase):
    def test_crear_etiqueta_success(self):
        request = self.client.post('/gestion/etiquetas', data={
            'nombre': 'Fronted'
        })
        self.assertEqual(request.status_code, 201)
        # asserEqual > afirmamos que el primer parametro debera ser igual que el 
        #segundo
        self.assertEqual(1, 1)

def test_listar_etiquetas_success(self):
    request = self.client.get('/gestion/etiquetas')
    print(request.data)
    self.assertEqual(1, 1)
