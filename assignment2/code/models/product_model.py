from db import db
from flask_restful import Resource


class ProductModel(db.Model):
    __tablename__ ='products'
    id=db.Column(db.Integer, primary_key=True)
    product_id=db.Column(db.Integer)
    prod_des=db.Column(db.String(80))

    def __init__(self,product_id, prod_des):

        self.product_id=product_id
        self.prod_des=prod_des


    def json(self):
        return {"prod_id":self.product_id,"prod_des":self.prod_des}


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()




