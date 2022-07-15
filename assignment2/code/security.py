from werkzeug.security import safe_str_cmp

from models.customer_model import CustomerModel
from models.visitor_model import VisitorModel


def authenticate(username,password):
    # not ablt to provide validation by id
    user= CustomerModel.find_by_username(username)
    if user and safe_str_cmp(user.password,password) :
        print('Yes')
        visitor=VisitorModel(username,password)
        visitor.save_to_db()
        return user

def identity(payload):
    user_id=payload['identity']
    return CustomerModel.find_by_id(user_id)
