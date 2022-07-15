from flask_restful import Resource, reqparse
from models.purchase_model import PurchaseModel


class ProductPurchase(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument(
        'cust_name',
        type=str,
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
        'prod_name',
        type=str,
        required=True,
        help='This field cannot be left blank'
        )
    parser.add_argument(
        'prod_des',
        type=str,
        required=False,
        help='This field can be left blank'
        )
    parser.add_argument(
        'prod_cost',
        type=int,
        required=True,
        help='This field cannot be left blank'
        )


    def post(self):

        data=ProductPurchase.parser.parse_args()


        sold_product=PurchaseModel(**data)

        sold_product.save_to_db()

        return {"message":"Sale Done successfully "} ,201

class PurchaseList(Resource):
    def get(self):
        return {"sold_items": [x.json() for x in PurchaseModel.query.all()]}


