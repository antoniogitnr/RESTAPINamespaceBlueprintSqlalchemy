from flask_restx import fields
from APP.namespace.namespace import api


producto = api.model(
    "Producto", 
    {
        "name": fields.String(required=True, description="nombre producto"),
        "price": fields.Integer(required=True, description="precio producto"),
        "quantity": fields.Integer(required=True, description="cantidad producto")
        }
    )