import { Router} from "express"
import { 
    actualizarProducto,
    crearProducto, 
    eliminarProducto,
    listarProductos,
 } from "../controllers/productos.controllers.js"
 import { validarAdmin, verificarToken} from "../utils/validador.js";

export const productosRouter = Router();

productosRouter.route("/productos")
.post(verificarToken, validarAdmin,crearProducto)
.get(listarProductos);
productosRouter
.route("/producto/:id")
// el .all sirve para indicar todos los middlewares que se tienen que llamar al controlador
// final (actualizar producto en caso de Put y a elimnar prodcto en caso de get)
.all(verificarToken, validarAdmin)
.put(actualizarProducto)
.delete(eliminarProducto);
