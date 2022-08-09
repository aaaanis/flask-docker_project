
import requests
from database.models import db, Product
from flask import jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
from database.models import db, Product
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.exc import MultipleResultsFound
class OpenFoodFact:
    url= ""
    def get_product_by_code(self, bar_code):
        try:
            response = requests.get(url = self.url + "/api/v0/product/" + bar_code + ".json")
            response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            raise err
        return response.json()
    
    def store(self, bar_code):
        result = open_food_fact.get_product_by_code(bar_code)
        product = Product(
            bar_code = result['code'],
            brand = result["product"]["brands"],
            nutri_score = result["product"]["nutriscore_grade"],
            name = result["product"]["generic_name_fr"],
        )
        return (product)    
        # db.session.add(product)
        # db.session.commit()
        # return jsonify(product)

open_food_fact = OpenFoodFact()

def setup_open_food_fact(app):
    open_food_fact.url = app.config["OPEN_FOOD_FACT_URL"]