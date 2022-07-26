import imp
from datetime import date

from flask import Flask, jsonify
from flask_jwt import jwt_required
from flask_restful import Resource, reqparse
from models.customer_model import CustomerModel
from models.sales_model import SalesModel
from sqlalchemy import distinct, func


class Sales(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument(
        'user_id',
        type=int,
        required=True,
        help='This field cannot be left blank'
        )
    parser.add_argument(
        'product_id',
        type=int,
        required=True,
        help='This field cannot be left blank'
        )
    parser.add_argument(
        'sale_amount',
        type=int,
        required=True,
        help='This field cannot be left blank'
        )
    parser.add_argument(
        'sale_date',
        type=date,
        required=False,
        default=date.today(),
        help='This can be left blank'
        )

    @jwt_required()
    def post(self):

        data=Sales.parser.parse_args()

        if not CustomerModel.find_by_id(data['user_id']):
            return {"message":"Please signup first"}

        sold_product=SalesModel(**data)

        sold_product.save_to_db()

        return {"message":"Sale Done successfully "} ,201

class PurchaseList(Resource):

    @jwt_required()
    def get(self):
        return {"sold_items": [x.json() for x in SalesModel.find_by_date(date.today()).filter(SalesModel.sale_amount != 0).all()]}


class UniqueVisitors(Resource):
    @jwt_required()
    def get(self):
        visitors = SalesModel.find_by_date(date.today()).all()
        unique_visitor=len(set([visitor.user_id for visitor in visitors]))
        return jsonify({"message":f"Total no. of unique visitors in the day are - {unique_visitor}"})

class TotalSales(Resource):
    @jwt_required()
    def get(self):
        return jsonify({"message": f"Total number of sales for the day is - {len(SalesModel.find_by_date(date.today()).filter(SalesModel.sale_amount != 0).all())}."})

class Average_sales_per_customer(Resource):
    @jwt_required()
    def get(self):
        visitors = SalesModel.find_by_date(date.today()).all()
        unique_visitor = len(set([visitor.user_id for visitor in visitors]))
        total_sales=[visitor.sale_amount for visitor in visitors]
        var=sum(total_sales)/unique_visitor
        return jsonify({"message": f"Average Sales Per Customer is {var}."})


