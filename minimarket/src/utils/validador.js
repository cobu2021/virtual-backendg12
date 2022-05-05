import prisma from "@prisma/client";
import jsonwebtoken from "jsonwebtoken";
import { Prisma } from "../prisma.js";

export async function verificarToken( req, res, next){


// middleware
// es un intermediario que sirve para hacer una validacion previa
// antes del controlador final
if (!req.headers.authorization) {
    return res.status(401).json({
        message:"Se necesita una token para realizar esta peticion",
    });
}
try {
    //recibire en el authorizacion lo siguiente : "Bearer asdfasd.asdfdasdf.asdfasd"
  const token = req.headers.authorization.split(" ")[1];
    // si la pwd es incorrecta, la token caduco o la token esta mal formate;
    const payload = jsonwebtoken.verify(token , process.env.JWT_SECRET);

    //si la tokem fue veridicxada correctamente nos devolvera el paylod en el cual
    // el id del usuario, ahora buscaremos en usuario de la ca


    const usuarioEncontrado = await Prisma.usuario.findUnique({
        where: { id : payload.id},
        rejectOnNotFound: true,
    });
    // ahora agregar el json el Request el usuario par que pueda ser utilizado por controladores
    req.user = usuarioEncontrado;
    next();
} catch (error) {
    return res.status(400).json({
      message: "Token invalida",
      content: error.message,
    });
  }
}

export const validarAdmin = async(req, res, next) => {
  // se ejecutara luego del middeleware de verificacion
  if (req.user.rol !== prisma.USUARIO_ROL.ADMINISTRADOR){
      return res.status(401).json({
        message:
        "El usuario no tiene los privilegios para realizar esta operacion",
      });   
  } else {
    next();
  }
}

export const validarCliente = async(req, res, next) => {
  // se ejecutara luego del middeleware de verificacion

  if (req.user.rol !== prisma.USUARIO_ROL.CLIENTE){
      return res.status(401).json({
        message:
        "El usuario no tiene los privilegios para realizar esta operacion",
      });   
  } else {
    next();
  }
}