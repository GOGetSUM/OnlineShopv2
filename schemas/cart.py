from ma import ma
from models.cart import CartModel



class CartSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = CartModel
        load_instance = True
        load_only = ("username",)
        dump_only = ("id",)
        include_fk = True
