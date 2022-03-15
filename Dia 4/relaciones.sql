USE PRUEBA;

create table vacunaciones(
id INT PRIMARY KEY AUTO_INCREMENT,
NOMBRE VARCHAR(100) UNIQUE NOT NULL, #NOMBRE NO SE PUEDE REPETIR Y QUE NO ADMITA VALORES VACIOS
estado BOOL DEFAULT TRUE, #ESTADO QUE SOLO ACEPTE BOOLS
fecha_vencimiento DATE, #FECHA_VENCIMIENTO FECHA
procedencia ENUM ('USA','CHINA', 'RUSIA' , 'UK'), #PROCEDENCIA SUS VALORES PUEDEN SER USA, CHINA,RUSIA,UK
lote VARCHAR(10) #LOTE NO PUEDE SUPERAR LOS 10 CARACTERES
);

CREATE TABLE vacunatorios (
id INT PRIMARY KEY AUTO_INCREMENT,
nombre varchar(100) NOT NULL,
latitud float,
longitud FLOAT,
direccion VARCHAR(200),
horario_atencion VARCHAR(100),
#la llave foranea (FK Foreing Key) es la representacion de la relacion entre la otra tabla e indicara todo su contenido
#representado solo por su id
vacuna_id INT,
FOREIGN KEY (vacuna_id) REFERENCES vacunaciones(id)
);

#DDL  Data Definition Languaje > se usara para la  definicion de donde se almacenan los datos en mi bd
#Para renombrar una tabla con un  nuevo nombre
#RENAME TABLE valor_antiguo TO nuevo_valor
#CREATE TABLES / CREATE DATABASE
# DROP ELIMINA la tabla ty su contenido a diferencia del delete que solo elimina el contenido
#DROP TABLE vacunatorios
#DROP DATABASE prueba

#Eliminara la columna de la tabla y perderemos todos los datos que hubiesen en ella
# ALTER TABLE vacunatorios DROP COLUMN latitud

#Agregara una nueva columna indicando el tipo de dato
ALTER TABLE vacunatorios ADD COLUMN imagen VARCHAR(100) DEFAULT 'imagen.png' AFTER horario_atencion;

ALTER TABLE vacunatorios RENAME COLUMN imagen TO foto;

#MODIFY COLUMN > CAMBIAR el tipo de dato y las configuraciones adicionales
#NO PODEMOS CAMBIAR EL TIPO DE DATO si ya hay informacion en esa columna y no corresponde con el nuevo tipo de dato
#ALTER TABLE vacunatorios MODIFY COLUMN imagen INT UNIQUE NOT NULL;

#Un vacunatorio podra tener una sola vacuna pero una vacuna puede estar presente en varios vacunatorios
# vacunas> vacunatorios

#SOLO FUNCIONA EN mysql
DESC CLIENTES;