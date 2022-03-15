#sql > structure query language
#un registro es un conjunto de datos y unm dato es
#un valor que por si solo no dice nada
#las bd por buenas practicas tienen que estar en singular

CREATE DATABASE prueba;

#para indicar que bd vas a utilizar

use prueba;

#El nombre de la tabla siempre sera en plural
#definiremos las columnas de la tabla
#debe haber almenos una columna por tabla es decir no puede existir una tabla sin columna
# nombre_col tipo_dato [config adic]
#EL PRIMARY KEY me permitira idenficar este reisgtro con otros en relacion a sus tablas adyacentes
#char(n) > creara una columna qye siempre ocupara  n espacios de caracteres
#VARCHAR(n) > crea una columna que podra tener como maximo n caracteres y ocupara solo el espacio que necesita
#TEXT > RESERVARA EL ESPACIO DINAMICO segun sea necesario para el valor de esa columna pero no tendra limite
#TODAS LAS columnas que no se especifiquen su nulicidad aceptaran valores nulos
CREATE TABLE clientes(
id INT AUTO_INCREMENT PRIMARY KEY,
nombre VARCHAR(50) NOT NULL,
#dni CHAR(8) UNIQUE,
#carnet_extranjeria VARCHAR(10) UNIQUE,
documento varchar(10) unique,
tipo_documento ENUM('C.E.','DNI', 'RUC' , 'PASAPORTE' , 'C.M.' , 'OTRO'),
#BOOL > PODRA SR VERDADERO O FALSO
estado BOOL
);