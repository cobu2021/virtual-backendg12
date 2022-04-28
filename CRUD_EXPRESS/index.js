//usando ECMAScript
import express from 'express';
import cors from "cors";
// usando CommonJS
//const express = require('express')

const servidor = express()
// middleware: intemediario que permite visualizar informacion adicional
// ahora podremos recibir y entender a un formato JSON
servidor.use(express.json())
// recibir  y enteder los bodys que sean puro texto
servidor.use(express.raw())
servidor.use(express.urlencoded({extended:true}));
// el metodo GET siempre va a poder ser accedido a pesar que solamente en el 
// methods le indicaremos otro
servidor.use(
    cors({
        origin: ["http://127.0.0.1:5501"],
        methods: ["POST","PUT","DELETE"],
        allowedHeaders: ["Content-Type","Authorization"],
    })
);

const productos = [
  {
    nombre : 'platano',
    precio : 1.80,
    disponible : true
  }
]
servidor.get('/',(req, res)=>{
    res.status(200).json({
        message: 'Bienvenido a mi API de productos'
    })

})

servidor.post('/productos',(req,res)=>{
    // mostrara todo el body enviado por el cliente
    console.log(req.body)
    const data =req.body

    productos.push(data)

    return res.status(201).json({
        message:'Producto agregado exitosamente'
    })
})

servidor.get('/productos', (req, res)=>{
    const data=productos
    return res.json({
        data // que la llave sera el mismo nombre que la variable y su valor sera
             // el contenido de esa variable
    })
})
servidor
.route("/producto/:id")
.get((req,res)=>{
    console.log(req.params);
    const{id} = req.params

    if (productos.leng < id){
        // 400 > Bad Request (Mala Solicitud)
        return res.status(400).json({
            message: ' El producto no existe'
        })
    }else {
        const data = productos[id-1]
        
        return res.json({
            data
        })
    }
})      
// PUT
.put((req, res)=>{
    // extraer el id
    const {id} = req.params
    // validar si existe esa posicion en el areglo
    if(productos.length < id){
 //si no existe, emitir un 400  indicando que el producto a actualizar no existe
       return res.status(400).json({
           message:'El producto a actualizar no existe'
       })
    }else{
        // si existe, modificar en el body
        productos[id-1] = req.body

        return res.json({
            message:'Producto actualiza exitoasmente',
            content: productos[id-1]
        })
    }
})
     .delete((req, res)=>{
       const {id} = req.params
       if(productos.length < id){
           return res.json({
               message: "Producto a eliminar no existe",
           });
       } else {
           // Metodo de los arreglos para elimiar una o mas elementos del arreglo
           // iniciando desde una posicion e indicando la cnatidad de elementos a eliminar
           productos.splice(id - 1,1);
           return res.json({
               message:'Producto eliminado exitosamente',
           });
        }
    });

servidor.listen(3000, () => {
   console.log("Servidor corriendo exitosamente en el puerto 3000")
})
