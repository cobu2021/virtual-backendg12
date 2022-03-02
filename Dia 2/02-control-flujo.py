#IF - ELSE
#python al no utilizar las llaves para definiir bloque de un comportamiento diferente
#tenemos que utilizar tabulaciones(tab)
from wsgiref.validate import validator


edad = int(input('ingresa tu edad'))
if (edad > 18) :
    #Todo lo que se escriba aca adentro
    print('La persona es mayor de edad')
    #la alineacion nunca dene de variar si estamos en el mismo bloque de codigo
    print('otra impresion')
#se utiliza si la primera condicion fallo pero queremos hacer una segunda condicion
elif edad > 15 :
    print('puedes ingresar a la preparatoria')
elif edad > 10 :
    print ('debes vacunarte')

# el else es completamente opcional y no siempre se debe utilizar con un if
else :
        #todo los demas
        print('eres muy niño')
        print('finalizo el programa')
# Validar si un numero (ingresos de una persona) ingresado por teclado es :
# * mayor a 500: indicar que no recibe el bono yanapay
# * entre 500 y mayor o igual que 250: indicar que si recibe el bono
# * es menor que 250: indicar que recibe el bono y un balon de gas
# RESOLUCION DEL EJERCICIO

valor = int(input('ingresa valor'))
if (valor > 500) :
    #Todo lo que se escriba aca adentro
    print('No recibe bono Yanapay')

elif valor >= 250 and valor <=500:
    print ('Si recibe el bono')

else :
        
        print('Si recibe el bono y BAlon de Gas')
        
#sdfsdf
