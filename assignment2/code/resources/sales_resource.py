import imp
from datetime import date

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

    def post(self):

        data=Sales.parser.parse_args()

        if not CustomerModel.find_by_id(data['user_id']):
            return {"message":"Please signup first"}

        sold_product=SalesModel(**data)

        sold_product.save_to_db()

        return {"message":"Sale Done successfully "} ,201

class PurchaseList(Resource):
    def get(self):
        return {"sold_items": [x.json() for x in SalesModel.query.filter(SalesModel.sale_amount != 0).all()]}



# func.count(distinct(User.name)
