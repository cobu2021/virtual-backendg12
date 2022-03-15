-- 1. Todas los alumnos que tienen correo GMAIL
-- 2. Todos los alumnos (nombre, ap_pat, ap_mat) que hayan cursado en el 2002
-- 3. Todos los grados donde su ubicacion sea el sotano o segundo piso
-- 4. Todos los grados (Seccion y el nombre ) que han tenidos alumnos en el año 2003

SELECT * FROM ALUMNOS WHERE CORREO LIKE '%gmail%';
select nombre,apellido_paterno,apellido_materno from alumnos INNER JOIN alumnos_niveles ON alumnos_id = alumnos_niveles.alumno.id
WHERE fecha_cursada = 2002;

select * from alumnos_niveles;