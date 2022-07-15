from flask_restful import Resource, reqparse
from models.customer_model import CustomerModel


class CustomerSignIn(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument(
        'username',
        type=str,
        required=True,
        help='This field cannot be lest blank'
        )
    parser.add_argument(
        'password',
        type=str,
        required=True,
        help='This field cannot be lest blank'
        )

    def post(self):

        data=CustomerSignIn.parser.parse_args()

        if CustomerModel.find_by_username(data['username']):
            return {"mesaage":"A user with given username already exists."} ,400

        user=CustomerModel(**data)

        user.save_to_db()

        return {"message":f"User created successfully"} ,201
