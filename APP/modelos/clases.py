from flask import request,jsonify
from APP.dataBase import db 
class crud:
    @staticmethod
    def post(producto):
        product = (producto.values())
        db.addProducto(product)
        return 'Producto agregado'
        
    @staticmethod
    def all():
        productos = db.all()
        lista_json = []
        for tupla in productos:
            producto = {
                "id": tupla[0],
                "nombre": tupla[1],
                "precio": tupla[2],
                "cantidad": tupla[3]
            }
            lista_json.append(producto)
        return lista_json

    @staticmethod 
    def one(id_producto):
        result  = db.one(id_producto)
        if result:
            result = {
                "id":result[0],
                "nombre":result[1],
                "price":result[2],
                "quantity":result[3],
            }
            print('result',result)
            return result
        else:
            return 'producto no encontrado'
        
        
    @staticmethod
    def dell(id_producto):
        respudelet = db.deleteProducto(id_producto)     
        return respudelet
    
    @staticmethod
    def update(id,modificar):
        tupla = tuple(modificar.values())
        respu = db.updateProducto(id,tupla)
        return respu
    