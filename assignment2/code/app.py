import os
from datetime import timedelta

from flask import Flask, jsonify
from flask_jwt import JWT
from flask_restful import Api

from db import db
from models.sales_model import SalesModel
from resources.customer_resource import CustomerSignIn
from resources.product_resources import ProductList
from resources.sales_resource import PurchaseList, Sales
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


# api endpoint for customer signing in the site for the first time
api.add_resource(CustomerSignIn,'/sign_in')


# customer login and check for valid customer
app.config['JWT_AUTH_URL_RULE'] = '/log_in'
jwt=JWT(app, authenticate, identity)


# api for product purchase
api.add_resource(Sales,'/purchase')


# api endpoint for total sales
@app.route('/totalsales')
def total_sales():
    return jsonify({"message": f"Total number of sales for the day is - {len(SalesModel.query.filter(SalesModel.sale_amount != 0).all())}."})


# api end point for unique visitors
@app.route('/uniquevisitors')
def unique_visitors():
    visitors = SalesModel.query.all()
    unique_visitor = {}
    for object in visitors:
        if object.user_id in unique_visitor.keys():
            unique_visitor[object.user_id]+=1
        else:
            unique_visitor[object.user_id] = 1
    return jsonify({"message":f"Total no. of unique visitors in the day are - {len(unique_visitor)}"})


# api endpoint for avg_sales_per_customer
@app.route('/avg_sales_per_customer')
def avg_sales_per_customer():
    visitors = SalesModel.query.all()
    unique_visitor = {}
    total_sales=[]
    for object in visitors:
        total_sales.append(object.sale_amount)
        if object.user_id in unique_visitor.keys():
            unique_visitor[object.user_id]+=1
        else:
            unique_visitor[object.user_id] = 1
    var=sum(total_sales)/len(unique_visitor)
    return jsonify({"message": f"Average Sales Per Customer is {var}."})


# api endpoint for list_of_daily_displays
api.add_resource(PurchaseList,'/daily_sales_list')

# api endpoint for listing of product
api.add_resource(ProductList,'/product_list')

if __name__=='__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)
