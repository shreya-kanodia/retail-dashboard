from db import db


class CustomerModel(db.Model):
    __tablename__ ='customers'
    id=db.Column(db.Integer, primary_key=True)
    firstname=db.Column(db.String(80))
    lastname=db.Column(db.String(80))
    username=db.Column(db.String(80))
    password=db.Column(db.String(80))

    def __init__(self,firstname,lastname,username, password):
        self.firstname=firstname
        self.lastname=lastname
        self.username=username
        self.password=password

    @classmethod
    def find_by_username(cls,username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls,_id):
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
