from typing import List

from db import db

class ItemModel(db.Model):
    __tablename__ = "Inventory"

    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(250), unique=True, nullable=False)
    size = db.Column(db.String(250), nullable=False)
    price = db.Column(db.Float, nullable=False)
    product_desc = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(250), nullable=False)
    inventory = db.Column(db.Integer, nullable=False)

    @classmethod
    def find_by_name(cls, product_name: str) -> "ItemModel":
        return cls.query.filter_by(name=product_name).first()

    @classmethod
    def find_all(cls) -> List["ItemModel"]:
        return cls.query.order_by(cls.inventory.desc()).all()

    def save_to_db(self) -> None:
        db.session.add(self)
        deb.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()

