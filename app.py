from pickle import FALSE
from flask import Flask , render_template

app = Flask(__name__)

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
if(__name__ == '__main__'):
    app.run(debug=True)