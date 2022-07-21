from db import db


class SalesModel(db.Model):
    __tablename__ ='sales'
    id=db.Column(db.Integer, primary_key=True)
    user_id=db.Column(db.Integer, db.ForeignKey('customers.id'))
    product_id=db.Column(db.Integer,db.ForeignKey('products.product_id'))
    sale_amount=db.Column(db.Integer)
    sale_date=db.Column(db.Date)

    def __init__(self,user_id,product_id,sale_amount,sale_date):
        self.user_id=user_id
        self.product_id=product_id
        self.sale_amount=sale_amount
        self.sale_date=sale_date
        # login time implementation
        # logout time implementation

    def json(self):
        return {"user_id":self.user_id,"price":self.sale_amount}

    @classmethod
    def find_by_date(cls,date):
        return cls.query.filter_by(sale_date=date)


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
