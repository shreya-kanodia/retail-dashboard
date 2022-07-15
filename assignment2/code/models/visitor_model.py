from datetime import date

from db import db


class VisitorModel(db.Model):
    # table_name='visitor-"'+ date.today().strftime("%d/%m/%Y") +'"'
    # __tablename__ =table_name
    __tablename__='visitors'
    serial_no=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(80))
    password=db.Column(db.String(80))
    # login time implementation
    # logout time implementation

    def __init__(self, username, password):
        self.username=username
        self.password=password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
