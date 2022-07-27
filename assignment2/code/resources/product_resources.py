
from flask_jwt_extended import jwt_required
from flask_restful import Resource
from models.product_model import ProductModel


class ProductList(Resource):

    @jwt_required()

    def get(self):
        prod1 = ProductModel(101, 'A wide leg jeans')
        prod1.save_to_db()
        prod2 = ProductModel(102, 'A flatter jeans')
        prod2.save_to_db()
        prod3 = ProductModel(103, 'A black shoe')
        prod3.save_to_db()
        prod4 = ProductModel(104, 'A orande large size shirt')
        prod4.save_to_db()
        prod5 = ProductModel(105, 'A red top')
        prod5.save_to_db()
        prod6 = ProductModel(106, 'umbrella')
        prod6.save_to_db()
        prod7 = ProductModel(107, 'socks and shoes')
        prod7.save_to_db()
        prod8 = ProductModel(108, 'A light peach top')
        prod8.save_to_db()
        prod9 = ProductModel(109, 'A bootcut jeans')
        prod9.save_to_db()
        prod10 = ProductModel(1010, 'A pink blue top')
        prod10.save_to_db()

        return {"product_items": [x.json() for x in ProductModel.query.all()]}


