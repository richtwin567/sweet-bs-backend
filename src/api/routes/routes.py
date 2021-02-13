from marshmallow.fields import Integer
from api.db.models import IngredientModel, IngredientSchema, MenuItemModel, MenuItemSchema, OrderModel, OrderSchema, UserSchema, UserModel, app
from flask import jsonify

class Routes():

    @staticmethod
    @app.route("/users", methods=['GET'])
    def get_all_users():
        users = UserModel.query.all()
        user_schema = UserSchema(many=True)
        if users is None:
            response = {
                "message":"no users found",
            }
            return jsonify(response)
        else:
            response = user_schema.dump(users)
            return jsonify(response)

    @staticmethod
    @app.route("/orders", methods=['GET'])
    def get_all_orders():
        orders = OrderModel.query.all()
        order_schema = OrderSchema(many=True)
        if orders is None:
            response = {
                "message":"no orders found",
            }
            return jsonify(response)
        else:
            response = order_schema.dump(orders)
            return jsonify(response)

    @staticmethod
    @app.route("/menuitems", methods=['GET'])
    def get_all_menuitems():
        menuitems = MenuItemModel.query.all()
        menuitem_schema = MenuItemSchema(many=True)
        if menuitems is None:
            response = {
                "message":"no menuitems found",
            }
            return jsonify(response)
        else:
            response = menuitem_schema.dump(menuitems)
            return jsonify(response)

    @staticmethod
    @app.route("/ingredients", methods=['GET'])
    def get_all_ingredients():
        ingredients = IngredientModel.query.all()
        ingredient_schema = IngredientSchema(many=True)
        if ingredients is None:
            response = {
                "message":"no ingredients found",
            }
            return jsonify(response)
        else:
            response = ingredient_schema.dump(ingredients)
            return jsonify(response)
