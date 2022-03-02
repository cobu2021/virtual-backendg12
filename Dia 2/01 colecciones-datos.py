#coleccion de datos es una variable que puede almacenar varios valores

#Listas
#ordenadas o pueden ser modificadas

from mailbox import NoSuchMailboxError
from site import execsitecustomize


nombre = ['Pedro' , 'Luis' , 'Danny' , 'Cesar' , 'Magaly' , 'Anahi']

combinada = [ 'Eduardo' , 80 , False , 15.8 , [1,2,3]]

#las listas siempre empiezan en la posicion 0
print(nombre[0])

# cuando hacemos el uso de valores negativos en una lista internamnete python le dara vuelta
print(nombre[-1])

print(nombre)
# si queremos ingresar a una posicion inexistente nos lanzara un error de 'indice fuera de rango'
#print(nombre[10])

#pop()> remueve el ultimo elemento de la lista y se puede alamacenar en otra varable

resultado = nombre.pop()
print(resultado)
print(nombre)

# append() > ingresa un nuevo elemento a la ultima posicion de la lista
nombre.append('Juana')

#elimina el contenido de una posicion de la lista pero no lo podemos almacenar en otra variable
del nombre[0]
print(nombre)

#clear() > limpia toda la lista y la deja como nueva
nombre.clear()  # >[]
print(nombre)
                # =1 <3
x = combinada[:] # .copy()
y = combinada

# indicar una sub eleccion de la lista
print(combinada[1:3])
print(combinada[1:4])

#indicando el contenido de la lista y esto es muy util para hacer una copia de la lista sin
#usar su misma posicion de memoria

print(combinada[:])

print(id(x))
print(id(combinada))
print(id(y))

# desde el incio hasta >2 (posicion 2)
print(combinada[:2])

# desde la posicion 2 hasta el final
print(combinada[2:])

meses_dscto = ['Enero' , 'Marzo' , 'Julio']
mes = 'Setiemmbre'
mes2 = 'Enero'

#indicara si el valor se encuentra dentro de la lista
print(mes not in meses_dscto)

#indicar si el valor se encuentra en la lista
print(mes2 in meses_dscto)

seccion_a=['Roxana','Juan']
seccion_b=['Julieta','Martin']
# si hacemos una sumatoria en las listas estas se combinan en la cual 
# la segunda lista ira despues de la primera
print(seccion_a + seccion_b)

#sirve para esperar un dato ingresado por el usuario
dato = input('Ingresa tu nombre:')
print(dato)

#Tuplas
#muy similar a la lista a excepcion que no se puede modificar
cursos = ('backend','frontend',1,True)

print(cursos)
print(cursos[0])
print(cursos[0:1])
#cursos.append('otra cosa')

#curso[0] = 'mobile desing'
#en la tupla no podemos alterar los valores pertenecientes a ella pero 
# si dentro de esta hay una lista u otra colleccion de datos que si se puede
#modificar entonces si podremos alterar esta sub coleccion sin problemas

variada = (1,2,3, [4,5,6])

variada[3][0] = 'Hola'

print(variada)

print('2' in variada)

#creamos una nueva lista a raiz de un atupla llanando a la clase list en la cual
#en el constructor e esa clase le pasamos los valores que contendra la nueva lista
variada_lista = list(variada)

#no se puede crear una lista a raiz de otra lista eso lanzara un error, solo se pede crear una 
#lista mediante su constructor mediante una tupla
list((1,2,3)) #[1,2,3]

#para ver la cantidad de elementos que conforman una tupla o una lista
#Nota: la longitud siempre sera la cantidad de elementos y esta siempre empezara
#en 1 mientras que la posicion siempre empezara en 0,es por eso que siempre longitud = posicion +1
print(len(variada))

#Conjuntos (Set)
#Colleccion de datos Desordenada, una vez que se crea ya no se acceder
#a las posiciones de sus elementos
estaciones = {'Verano' , 'Otonio' , 'Primavera' ,'Invierno'}

print('Invierno' in estaciones)
#se agrega de forma aleatoria
estaciones.add('Otro')
#al ser desordenada el moneto de retirar el ultimo elemento este sera completmente
#aleatorio y retirara el ultimo elelmento agreadado de forma aleatoria
#pop() > quita el ultimo elemento de la collecion de datos (list,tuples,set)
estacion = estaciones.pop()
print(estacion)

#Diccionarios
#una collecion de doatos Desordenada pero cada elemento obedece a una llave definida

persona={
    'nombre' : 'Eduardo',
    'Apellido' : 'De Rivero',
    'Correo' : 'ediriveroman@gmail.com'
}
#hacemos la busqueda de una determinda llave y si no la encuentra nos retornara opcionalmente none

print(persona['Apellido'])
print(persona.get('Apellido','No existe'))
#print(persona['apellidos'])
#devuelve todas las llaves de mi diccionario
print(persona.keys())

#devuelve todos los contenidos de mi diccionario
print(persona.values())

#devuelve todas las llaves y su contenido en forma de tuplas dentro de una lista
print(persona.items())

#si definimos una llave que no existe la creara, caso contratio modificara su valor
persona['edad'] = 28
#nota : si la llave no es exactamente igual creara una nueva(tiene que coincidir minusculas)
persona['nombre']='Ximena'
print(persona)

#eliminar una llave de un dicionario
persona.pop('Apellido')
#sadf








