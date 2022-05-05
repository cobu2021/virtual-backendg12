import {Router} from "express";
import { confirmarCuenta, crearUsuario, login, perfil 
} from "../controllers/usuarios.controller.js";
import { verificarToken } from "../utils/validador.js";


export const usuarioRouters = Router();

usuarioRouters.post("/registro", crearUsuario);
usuarioRouters.post("/login",login);
usuarioRouters.post("/confirmar-cuenta",confirmarCuenta);
usuarioRouters.get("/perfil",verificarToken, perfil);