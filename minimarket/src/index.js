import express, { json } from "express";
import { detallePedidoRouter} from "./routes/detallePedido.routes.js";
import { pedidosRoutes } from "./routes/pedidos.routes.js";
import { productosRouter } from "./routes/productos.routes.js";
import { usuarioRouters } from "./routes/usuarios.routes.js";
import {pagosRouter } from "./routes/pagos.routes.js";

import mercadopago from "mercadopago";



const app= express();

// configuro las credenciales que van a servir para hacer la pasarela de pagos
// integrador_id > es el id del desarrollador que esta haciendo esta integracion
//(servira para que MP nos de bonificaciones a cambio de la integracion)
// access token > es la token que se creara al generar UNA NUEVA INTEGRACION y sera encargada
//de cuando se pague algo ese dinero sea redirijido a la cuenta de la empresa
mercadopago.configure({
    access_token: process.env.MP_ACCESS_TOKEN,
    integrator_id:process.env.MP_INTEGRATOR_ID,
});

app.use(json());

const PORT = process.env.PORT ?? 3000;

app.get("/", (req, res) =>  {
    res.json({
        message: "Bienvenido a mi Api de Minimarket",
    });
});

// agregar un bloque de rutas definidas en otro archivo
app.use(productosRouter);
app.use(usuarioRouters);
app.use(pedidosRoutes)
app.use(detallePedidoRouter)
app.use(pagosRouter);

app.listen(PORT, () => {
   console.log(`servidor corriendo exitosamente en el puerto ${PORT}`);
});