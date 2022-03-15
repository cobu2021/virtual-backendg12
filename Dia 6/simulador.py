# factory
from optparse import Values
from faker import Faker
from faker.providers import internet
from random import randint, choice
fake = Faker()
#le agregamos un provider adicional a nuestro faker para que ahora pueda utilizar los
#tradicionales y los de internet
fake.add_provider(internet)

print('Nombre',fake.name())
print('Ap. Paterno',fake.first_name_female())
print('Ap. Materno',fake.last_name_female())
print('Correo',fake.ascii_free_email())
print('Telefono',fake.phone_number())

#usando un provider de person hace que me imprima un nombre,
#ape_pat, ape_mat, correo (internet),num_telefonico (phone_number)

def generar_alumnos(limite):

    for persona in range(limite):
        Nombre = fake.name()
        apepat = fake.first_name()
        apemat = fake.last_name()
        correo = fake.ascii_free_email()
        telefono =fake.bothify(text='9########')
        #telefono =fake.phone.number()
        #utilizamos faker para generar un numero aleatorio entre 91111111 hasta 999999
        #telefono = fake.random_int(min=911111111, max=999999999)
        #fake.bothify(text='asd####??', letters='9999999')
        sql= '''INSERT INTO alumnos(nombre ,apellido_paterno, apellido_materno, correo, numero_emergencia)Values
                            ('%s', '%s', '%s', '%s', '%s'); ''' % (Nombre, apepat, apemat, correo, telefono)

        #INSERT INTO alumnos(nombre ,apellido_paterno, apellido_materno, correo, numero_emergencia)Values
        #                   ('{}', '{}', '{}', '{}', '{}');''',format (Nombre, apepat, apemat, correo, telefono)
        print(sql)

def generar_niveles():
    secciones = ['A' , 'B' ,'C']
    ubicaciones = ['Sotano' , 'Primer Piso' , 'Segundo Piso' ,'Tercer Piso']
    niveles =['Primero' ,'Segundo' ,'Tercero' ,'Cuarto' ,'Quinto','Sexto']
    #iterar los niveles y en cada nivel colocar como minimodos secciones y como maximo 3
    #(ramdom_int) y luego agreegar aleatoriamente la ubicacion a ese nivel
    #Primer A Segundo Piso
    #Primero B Tercer Piso
    #Segundo A Sotano
    for nivel in niveles:
                        # entre 1 hasta <=3 (0!1!2)
        pos_secciones = randint(2,3)
        ##pos_secciones = fake.random_int(min=1, max=3)
        for posicion in range(0, pos_secciones):
           # pos_ubicacion = fake.random_int(min=0, max=3)
           ubicacion = choice(ubicaciones)
           seccion = secciones[posicion]
           nombre = nivel
           sql =''' INSERT INTO niveles (seccion, ubicacion, nombre)VALUES
                                    ('%s', '%s', '%s');''' % (seccion, ubicacion,nombre)
            #print('Nivel' , nivel)
            #print('Seccion',secciones[posicion])
            #print('Ubicacion',ubicaciones[pos_ubicacion])
           print(sql)
generar_niveles()
