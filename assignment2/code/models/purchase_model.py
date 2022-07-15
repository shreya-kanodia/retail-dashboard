from db import db


class PurchaseModel(db.Model):
    __tablename__ ='sales'
    id=db.Column(db.Integer, primary_key=True)
    cust_name=db.Column(db.String(80))
    product_id=db.Column(db.Integer)
    prod_name=db.Column(db.String(80))
    prod_des=db.Column(db.String(80))
    prod_cost=db.Column(db.Integer)


    def json(self):
        return {"prod_id":self.product_id,"prod_name":self.prod_name,"price":self.prod_cost}



    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
