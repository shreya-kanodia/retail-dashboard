import os
from datetime import date, timedelta

from flask import Flask, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_restful import Api

from db import db
from models.sales_model import SalesModel
from resources.customer_resource import CustomerRegister, UserLogin
from resources.product_resources import ProductList
from resources.sales_resource import (
    Average_sales_per_customer,
    PurchaseList,
    Sales,
    TotalSales,
    UniqueVisitors,
)
from security import authenticate, identity

app=Flask(__name__)
app.secret_key= '1234'
CORS(app)
api=Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

jwt=JWTManager(app)

app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=1800)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
app.config['SQLALCHEMY_DATABASE_URI'] =  os.environ.get('DATABASE_URI', 'sqlite:///data.db')

# api endpoint for customer signing in the site for the first time
api.add_resource(CustomerRegister,'/register')


# customer login and check for valid customer
api.add_resource(UserLogin,'/log_in')


# api for product purchase
api.add_resource(Sales,'/purchase')


# api endpoint for total sales
api.add_resource(TotalSales,'/totalsales')


# api end point for unique visitors
api.add_resource(UniqueVisitors,'/uniquevisitors')



# api endpoint for avg_sales_per_customer
api.add_resource(Average_sales_per_customer,'/avg_sales_per_customer')


# api endpoint for list_of_daily_displays
api.add_resource(PurchaseList,'/daily_sales_list')

# api endpoint for listing of product
api.add_resource(ProductList,'/product_list')

if __name__=='__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)
