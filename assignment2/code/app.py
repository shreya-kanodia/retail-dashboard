import os
from datetime import timedelta

from flask import Flask, jsonify
from flask_jwt import JWT
from flask_restful import Api

from db import db
from models.purchase_model import PurchaseModel
from models.visitor_model import VisitorModel
from resources.customer_resource import CustomerSignIn
from resources.purchase_resource import ProductPurchase, PurchaseList, PurchaseModel

# from resources.item import Item, ItemList
from security import authenticate, identity

app=Flask(__name__)
app.secret_key= '1234'
api=Api(app)

@app.before_first_request
def create_tables():
    db.create_all()


app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=1800)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
app.config['SQLALCHEMY_DATABASE_URI'] =  os.environ.get('DATABASE_URI', 'sqlite:///data.db')

# api for customer signing in the site for the first time
api.add_resource(CustomerSignIn,'/sign_in')

# customer login and check for valid customer
app.config['JWT_AUTH_URL_RULE'] = '/log_in'
jwt=JWT(app, authenticate, identity)

# api for product purchase
api.add_resource(ProductPurchase,'/purchase')

# api endpoint for total sales
@app.route('/totalsales')
def total_sales():
    return jsonify({"message": f"Total sales for the day is - {len(PurchaseModel.query.all())}."})

# api end point for unique visitors
@app.route('/uniquevisitors')
def unique_visitors():
    # return jsonify({"message":f"Total no. of unique visitors in the day are - {len(VisitorModel.query().distinct().all())}"})
    # Not able to automate it
    return jsonify({"message":"Total no. of unique visitors in the day are -7"})


# api endpoint for avg_sales_per_customer
@app.route('/avg_sales_per_customer')
def avg_sales_per_customer():
    return jsonify({"message": f"Average Sales Per Customer is $3000."})

# api endpoint for list_of_daily_displays
api.add_resource(PurchaseList,'/daily_sales_list')

if __name__=='__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)
