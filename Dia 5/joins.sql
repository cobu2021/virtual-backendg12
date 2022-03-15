-- JOINS
-- es la menera de ingresar hacia una tabla mediante una columna comun
USE prueba;

SELECT * FROM VACUNATORIOS WHERE VACUNA_ID = 1;

SELECT *
FROM VACUNATORIOS INNER JOIN VACUNACIONES ON VACUNATORIOS.vacuna_id = vacunaciones.id
WHERE vacuna_id =1;

SELECT * FROM VACUNACIONES;

SELECT * FROM VACUNATORIOS;

SELECT *
FROM VACUNATORIOS LEFT JOIN VACUNACIONES ON VACUNATORIOS.vacuna_id = vacunaciones.id
WHERE vacuna_id =1;

INSERT INTO vacunatorios (nombre, latitud, longitud, direccion, horario_atencion, foto, vacuna_id) VALUES
                         ('POSTA JOSE GALVEZ', 14.26598, 32.2569, 'AV. EL SOL 755', 'LUN-VIE 15:00 22:00', null, null);

SELECT *
FROM VACUNATORIOS RIGHT JOIN VACUNACIONES ON VACUNATORIOS.vacuna_id = vacunaciones.id
WHERE vacuna_id =1;


-- FULL OURTER JOIN
-- TRAERA TODA LA INFORMACION TANTO DE LA TABLA DE LA IZQUIERDA COMO DE LA DERECHA Y OPCIONALMENTE SI HAY ALGUNA
-- INTERSECCION LO HARA SINO NO IMPORTA

SELECT *
FROM VACUNATORIOS LEFT JOIN VACUNACIONES ON VACUNATORIOS.vacuna_id = vacunaciones.id UNION
SELECT *
FROM VACUNATORIOS RIGHT JOIN VACUNACIONES ON VACUNATORIOS.vacuna_id = vacunaciones.id;


-- Si se usa en la clausula where o en el select una columna ambigua(que se repite el mismo nombre) hay que especificar
-- de que tabla estamos hablando
SELECT *
FROM VACUNATORIOS JOIN VACUNACIONES ON VACUNATORIOS.vacuna_id = vacunaciones.id
WHERE VACUNACIONES.nombre = 'Pfizer';

-- Tambien se puede colocar alias a las tablas para evitar escribir su nombre en su totalidad o escribir un nombre
-- mas entendible con las palabras AS

SELECT vacu.nombre, vac.nombre
FROM vacunatorios AS vac JOIN  VACUNACIONES AS VACU ON vac.vacuna_id = vacu.id
where vacu.nombre= 'Pfizer';

-- 1. Devolver todos los vacunatorios en los cuales la vacuna sea Sinopharm y su horario de atencion sea de LUN-VIE
      SELECT * 
      FROM VACUNATORIOS JOIN  VACUNACIONES ON VACUNATORIOS.vacuna_id = vacunaciones.id
      where vacunaciones.nombre='SINOFARM' AND horario_atencion like '%LUN-VIE%';
      
      SELECT * FROM VACUNATORIOS;
      SELECT * FROM VACUNACIONES;
      
      
-- 2. Devolver solamente las vacunas cuyo vacunatorio este ubicado entre la latitud -5.00 y 10.00 IN() 

SELECT vacunaciones.nombre
FROM vacunatorios JOIN vacunaciones on vacunatorios.vacuna_id = vacunaciones.id
where latitud BETWEEN -5 AND 10 ; 

SELECT vacunaciones.nombre
FROM vacunatorios JOIN vacunaciones on vacunatorios.vacuna_id = vacunaciones.id
where latitud > -5 AND  latitud < 10 ; 

-- 3. Devolver todas las vacunas que no tengan vacunatorio y solamente su procedencia y nombre

select procedencia, vacunaciones.nombre
FROM vacunatorios right JOIN vacunaciones on vacunatorios.vacuna_id = vacunaciones.id
where vacuna_id is null;

