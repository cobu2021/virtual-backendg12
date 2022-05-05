import {Prisma} from "../prisma.js";
import {crearDetallePedidoRequestDTO} from '../dtos/detallePedido.dto.js'
export const crearDetallePedido = async (req, res) => {

    try {

      const data = crearDetallePedidoRequestDTO(req.body);
      // lUEGO DE CREAR EL DETALLE PEDIDO ACTULIZAR EL PEDIDO  PARA MODIFICAR ELTOTAL
      // DEL PEDIDO
      // LO HAREMOS MEDIANTE TRANSACCIONES
      await Prisma.$transaction(async ()=> {
        //https://www.prisma.io/docs/concepts/components/prisma-client/transactions#interactive-transactions-in-preview
          //ahora puedo usar dentro de la transaccion una secuencia de codigo
          const { precio} = await  Prisma.producto.findUnique({
              where : { id: data.productoId},
              rejectOnNotFound: true,
              select: { precio: true},
          });
          // hago la busqueda de pedido
          const { id, total } = await Prisma.pedido.findUnique({
              where: { id: data.pedidoId},
              select: { id: true, total : true},
              rejectOnNotFound: true,
          });
          
      //creo el detalle de ese pedido con la modificacion del subtotal
      const {subtotal} = await Prisma.detallePedido.create({
           data : {... data, subtotal:precio*data.cantidad },
           select: { subtotal: true},
           });
           
     // ahora actualizo el total del pedido
       await Prisma.pedido.update({
           data: { total: total + subtotal},
           where: {id },
       });
    });
      return res.status(201).json({
          message: "Detalle Creado exitosamente",
      });
    } catch (error) {
        return res.status(400).json({
            message: "Error al crear el datalle del pedido",
            content : error.message,
        });
    }
};