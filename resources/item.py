from flask_restful import Resource
from flask import request
from flask_jwt_extended import jwt_required

from models.item import ItemModel
from schemas.item import ItemSchema
from libs.strings import gettext

item_schema = ItemSchema()
item_list_schema = ItemSchema(many=True)

class Item(Resource):
    @classmethod
    def get(cls, product_name: str):
        item = ItemModel.find_by_name(product_name)
        if item:
            return item_schema.dump(item),200

        return {"message": gettext('item_not_found')}, 404

    @classmethod
    @jwt_required(fresh=True)
    def post(cls, product_name: str):
