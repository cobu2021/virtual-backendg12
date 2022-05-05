import mercadopago from "mercadopago";
import {Prisma} from "../prisma.js";

export const crearPreferencia = async (req, res) =>{
    try {
        //
        const {pedidoId } = req.body;
        
        const pedidoEncontrado = await Prisma.pedido.findUnique({
            where: { id: pedidoId},
            rejectOnNotFound: true,
            include: {
                cliente:true,
                detallePedidos: { include : { producto: true}},
            },
        });
        console.log(pedidoEncontrado);

        //https://www.mercadopago.com.pe/developers/es/reference/preferences/_checkout_preferences/post
               
        const preferencia = await mercadopago.preferences.create({
            auto_return : "approved",
            back_urls: {
                failure: "http://localhost:3000/pago-fallido",
                pending:"http://localhost:3000/pago-pendiente",
                success: "http://localhost:3000/pago-exitoso",
            },
            metadata: {
                nombre:"Prueba",
            },
            payer: {
                name: pedidoEncontrado.cliente.nombre,
               // surname: "De Rivero",
                //address: {
                //    zip_code: "04002",
                 //   street_name: "Calle los Girasoles",
                //    street_number: 105,
                //},
                email: "test_user_45542185@testuser.com",
            },
            items: pedidoEncontrado.detallePedidos.map((detallePedido) => ({
              
                id: detallePedido.productoId,
                currency_id: "PEN",
                title: detallePedido.producto.nombre,
                quantity: detallePedido.cantidad,
                unit_price: detallePedido.producto.precio, 
            })),
                // detallePedido.subTotal / detallePedido.cantidad
    
                 // id: "1234",
                 // category_id: "456",
                 // currency_id: "PEN",
                 // description: "Zapatillas de Outdoor",
                 // picture_url: "https://imagenes.com",
                 // quantity: 1,
                  //title: "Zapatillas edicion Otoño",
                 // unit_price: 75.2,
              //  },
            //  ],
       // });
            // 
            notification_url:   "https://8f61-181-64-255-96.ngrok.io/mp-webhooks",
        });
        
        await Prisma.pedido.update({
            data: { process_id: preferencia.body.id, estado:"CREADO"},
            where:  {id: pedidoId},
        });
        
        console.log(preferencia);
        return res.json({
            message: "Preferencia generada exitosamente",
            conten: preferencia,
        });
    } catch (error) {
        return res.json({
            message: "Error al crear la preferencia",
            content: error.message,
        });
    }
};

export const MercadoPagoWebhooks = async (req, res) =>{
    console.log ('-----body----')
    console.log(req.body);

    console.log('----params----');
    console.log(req.params);

    console.log('----headers----');
    console.log(req.headers);

    console.log('----queryparams----');
    console.log(req.query);

    if (req.query.topic === "merchant_order"){
        const { id } = req.query;
        const orden_comercial = await mercadopago.merchant_orders.get(id);
        console.log("La orden es:");
        console.log(orden_comercial);

        const pedido = await Prisma.pedido.findFirst({
            where: { process_id : orden_comercial.body.preference_id},
        });

        if (!pedido) {
            // enviara un correo al area de ventas para ralizar una validacion manual del 
            // por que no se encuentra ese pago que me esta enviando mercadoPago
            console.log("Pedido Incorrecto");
        }
        if (orden_comercial.body.order_status === "paid"){
            
            // cambiamos el estado de nuestro pedido a pagado
            await Prisma.pedido.updateMany({
                where : {process_id: orden_comercial.body.preference_id },
                data : {estado : "PAGADO"},
            });
        }
    };

    
    return res.status(201).json({
        message:"Webhook recibido exitosamente",
    });
};