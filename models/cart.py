from typing import List

from db import db

class CartModel (db.Model):
    __tablename__ ="cart"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Integer, db.ForeignKey("user.username"), nullable=False)
    name = db.relationship(
        "ItemModel",lazy='dynamic', cascade='all, delete-orphan'
    )
    price =db.relationship(
        "ItemModel",lazy='dynamic', cascade='all, delete-orphan'
    )
    product_desc = db.relationship(
        "ItemModel", lazy="dynamic", cascade="all, delete-orphan"
    )

    @classmethod
    def find_cart_by_username(cls,username:str) ->"CartModel":
        cart_ = cls.query.filter_by(username=username).all()

        product_id = []
        name = []
        price = []
        tot_ = 0
        # Convert query into list
        for item in cart_:
            if item.profile_id == id:
                product_id.append(item.product_id)
        # remove duplicates from list
        seen = set()
        uniq_item = [x for x in product_id if x not in seen and not seen.add(x)]
        for item in uniq_item:
            catalog = cls.query.get(item)
            tot_ = float(tot_) + catalog.price
            price.append(catalog.price)
            name.append(catalog.product_name)
        total = round(tot_, 2)
        cart_dictionary = {i: [j, k] for i, j, k in zip(uniq_item, name, price)}

        return cart_dictionary, total

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()

