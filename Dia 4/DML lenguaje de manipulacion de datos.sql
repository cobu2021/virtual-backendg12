USE prueba;
# sub parte del sql:
#DML : Data Manipulation Languaje (Lenguaje de Manipulacion de Datos)
#Se utilizapara la manipulacion de la informacion dentro de una base de datos
#INSERT,SELECT,UPDATE,DELETE
INSERT INTO CLIENTES(nombre, documento, tipo_documento,estado) values
					('Eduardo','09711361', 'DNI' , true);
INSERT INTO clientes(nombre, documento, tipo_documento,estado) values
					('Estefani', '09811361', 'DNI' , true), 
                    ('Juan', '09511371', 'DNI' , false);
                    
                    
# select col1,col2 from tabla
SELECT nombre, documento FROM clientes;
SELECT * FROM clientes;

SELECT * FROM CLIENTES WHERE documento='09811361' AND NOMBRE = 'Estefani' or nombre='Eduardo';

SELECT * FROM CLIENTES WHERE documento='09811361' AND (NOMBRE = 'Estefani' OR NOMBRE= 'Eduardo');



#SELECCIONAR A TODAS LAS PERSONAS QUE TIENEN DNI Y ESTADO TRUE

SELECT * FROM CLIENTES WHERE TIPO_DOCUMENTO='DNI' AND ESTADO=TRUE;

#LIKE en columnas de string para hacer una similitud y ademas usaremos los '%'para indicar si no se sabe
#en que parte exactamente esta esa letra o letras

SELECT * FROM CLIENTES WHERE NOMBRE LIKE '%Edu';

# sirve  para actualizar uno o varios registros de una determinada tabla
UPDATE CLIENTES SET nombre= 'Ramiro' , documento = '33333333' WHERE id =1 AND nombre= 'Eduardo';

#MODO SERGURO> es el modo que nos impide hacer actualizaciones(UPDATE) y eliminaciones (DELETE) sin usar
#una columna que sea indice (o PK)
#Para desactivar el modo seguro;
SET SQL_SAFE_UPDATES = false;

#otra forma deacceder mediante el workbench es en el menu EDIt> preference > SQL Editor y al final estara la opcion para modificar

#DELETE sirve para eliminar REGISGTROS de una determinada tabla
delete  from clientes where id=1;

                    
                    