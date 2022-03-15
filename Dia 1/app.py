#from selectors import selectors
from flask import Flask , request
from datetime import datetime
from flask_cors import CORS,cross_origin

from jinja2 import pass_environment

app = Flask(__name__)
CORS(app=app, orgins=['http://127.0.0.1:5500' ,'http://127.0.0.1:5501' ,
                       'http://miapp.vercel.app'], methods='*' , 
                        allow_headers=['Content-Type'])


clientes = [
    {
    "nombre": "Luis",
    "pais": "PERU",
    "edad": 51,
    "id": 1,
    "organos": True,
    "casado": False
    }
]

@app.route('/')
def estado():
    hora_del_servidor = datetime.now()

    return {
        'status' : True,
        'hour'   : hora_del_servidor.strftime('%d/%m/%Y  %H:%M:%S')
    }
@app.route("/clientes" , methods=['POST','GET'])
#para modificar las reglas globales de la aplicacion (CORS) y que solamente se respeten
#estas nuevas reglas en este endpoint con sus metodos correspondientes
@cross_origin(origins='http://127.0.0.1:7000')
def obtener_clientes():

    print(request.method)
    
    print(request.get_json())

    if request.method == 'POST' :
       data = request.get_json()
       data['id'] = len(clientes) + 1
       clientes.append(data)
       data['nombre']
       return  {
        'message' : 'Cliente Agregado Exitosamente',
        'client' : data
    }
    else:
        return {
            'mesage' : 'lista de clientes',
            'clientes' : clientes
        }
    
def buscar_usuario(id):
      # for cliente in clientes:
       # if cliente.get('id') == id:
        #   return cliente
    for posicion in range(0, len(clientes)):
        if clientes[posicion].get('id') == id:
            return (clientes[posicion] , posicion )
   



@app.route('/cliente/<int:id>', methods=['PUT' , 'GET', 'DELETE'])
def gestion_usuario(id):
    if request.method == 'GET':
        print(id)
        usuario = buscar_usuario(id)
        if (usuario is not None) :
            return usuario
        else:
            return{
                    'message' : 'El Usuario a Buscar no se Encontro'
        }, 404

    elif request.method == 'PUT':
        resultado = buscar_usuario(id)
        if resultado:
            [cliente, posicion] = resultado
            data = request.get_json()
            data['id'] = id

            #data['id'] = resultado[0].get('id')
            #posicion = [resultado[1]]
            clientes[posicion] = data
            return clientes[posicion]
        else:
            return{
                'message' : 'El Cliente a Buscar no se Encontro'
            }, 404
    
    elif request.method == 'DELETE':
         resultado = buscar_usuario(id)
         if resultado:
            [cliente,posicion]= resultado
            cliente_eliminado = clientes.pop(posicion)
         return {
                'message': 'cliente eliminado exitosamente',
                'cliente':cliente_eliminado
            }

def gestion_usuario(id):
    resultado = None
    for cliente in clientes:
        if cliente.get('id') == id:
            resultado = cliente
            break
    if (resultado is not None) :
        return resultado



app.run(debug=True, port=8080)

