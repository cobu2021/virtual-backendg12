def sumar (a,b):
    return a+b

print(sumar(10,5))
print(sumar(a=10, b=5))
parametros = {
    'a' : 10,
    'b' : 5
}
#al momento de nosotros queremos pasar los parametros pero en forma de un diccionario
#se puede hacer la destructuracion usando los ** antes del diccionario
print(sumar(**parametros))
print(sumar(**{'a' : 10 , 'b':5}))

def restar(**kwargs):
    return(kwargs)

def multiplicar(*args):
    return(args)

print(multiplicar(5,4))
print(restar(x=1,y=2,z=3))