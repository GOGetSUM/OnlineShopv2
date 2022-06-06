from flask_restful import Resource
from flask import request
from flask_jwt_extended import jwt_required
from models.cart import CartModel
from schemas.cart import CartSchema
from libs.strings import gettext

cart_schema = CartSchema()
cart_list_schema = CartSchema(many=True)


class Cart(Resource):
    @classmethod
    @jwt_required()
    def post(cls, name: str):
        item_json = request.get_json()
        item_json["name"] = name
        item = cart_schema.load(item_json)

        try:
            item.save_to_db()
        except:
            return {"message": gettext("cart_error_inserting")}, 500

        return cart_schema.dump(item), 201

    @classmethod
    @jwt_required()
    def delete(cls, name: str):
        item = CartModel.find_by_name(name)
        if item:
            item.delete_from_db()
            return {"message": gettext("item_deleted")}, 200

        return {"message": gettext("item_not_found")}, 404


class CartList(Resource):
    @classmethod
    def get(cls, username: str):
        cart = CartModel.find_cart_by_username(username)
        if cart:
            return cart_schema.dump(cart), 200

        return {"message": gettext("cart_not_found")}, 404