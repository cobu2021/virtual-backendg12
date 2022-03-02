#IF - ELSE
#python al no utilizar las llaves para definiir bloque de un comportamiento diferente
#tenemos que utilizar tabulaciones(tab)
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
        