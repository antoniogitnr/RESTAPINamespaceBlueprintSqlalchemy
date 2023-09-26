from APP.namespace.namespace import api
from APP.tablas.tablas import producto
from flask_restx import Resource
from flask import request
from APP.modelos.clases import crud

class Endpoints:
    @api.route("/products")
    class listarproductos(Resource):
        def get(self):
            return crud().all()
    
    @api.route("/addproducts", methods=["POST"])
    class addProductos(Resource):
        @api.expect(producto,validate=True)
        def post(self):
            product = request.json
            return crud().post(product)

        
    @api.route("/oneproducto/<int:id_producto>")
    class getproducto(Resource):
        def get(self,id_producto):
            return crud().one(id_producto)
            
    @api.route("/deleteproducto/<int:id_producto>", methods=["DELETE"])
    class deleteproducto(Resource):
        def delete(self,id_producto):
            return crud().dell(id_producto)
        
    @api.route("/updateproducto/<int:id_producto>", methods=["PUT"])
    class updateproducto(Resource):
        @api.expect(producto, validate=True)
        def put(self, id_producto):
            product = request.json
            return crud().update(id_producto,product)
                    