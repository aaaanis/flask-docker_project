from flask import request
from flask import jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
from services.open_food_fact import open_food_fact
from database.models import db, Product, Purchase
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.exc import MultipleResultsFound
 #---------------------------------------------------------------------------------------------------------------#

class ProductsAPI(Resource):
    @jwt_required()
    def get(self):
        users = Product.query.all()
        return jsonify(users)

 #---------------------------------------------------------------------------------------------------------------#

class ProductAPI(Resource):
    @jwt_required()

    def get(self, bar_code):
        try:
            result = Product.query.filter_by(bar_code = bar_code).one()

        except NoResultFound:
            # appel de la fonction store dans /services pour recuperer le resultat depuis l'api openfoodfact et l'ajouter dans la BDD,
            product = open_food_fact.store(bar_code)
            db.session.add(product)
            db.session.commit()
            return jsonify(product)
        else:
            return jsonify(result)

 #---------------------------------------------------------------------------------------------------------------#

    #création de l'entrée dans la BDD
    def post(self, bar_code):
        try:
            result = Product.query.filter_by(bar_code = bar_code).one()

        except NoResultFound:
            product = open_food_fact.store(bar_code)
            db.session.add(product)
            db.session.commit()
            return jsonify(product)
        else:
            #TODO:  si existe mais different de l'api = on le met à jour / si identique: on ne fait rien
            result = Product.query.filter_by(bar_code = bar_code).one()
            return jsonify("Le produit demandé existe déja, veuillez vérifier votre bar code")
            
    #---------------------------------------------------------------------------------------------------------------#

    def delete(self, bar_code):
        try:
            result = Product.query.filter_by(bar_code = bar_code).one()

        except NoResultFound:
            return jsonify("Product not found, please check your bar code")

        else:
            db.session.delete(result)
            db.session.commit()
            return jsonify("product successfully deleted")

#---------------------------------------------------------------------------------------------------------------#

class ProductsBuyAPI(Resource):
    @jwt_required()
    def get(self):
        purchase = Purchase.query.all()
        return jsonify(purchase)

#---------------------------------------------------------------------------------------------------------------#

class ProductBuyAPI(Resource):
    @jwt_required()
    def post(self, bar_code):
       
        body = request.json
        try:
            result = Product.query.filter_by(bar_code = bar_code).one()

        except NoResultFound:
            open_food_fact.store(bar_code)
            bar_code = str(bar_code)
            purchase = Purchase(
                buyer_id = get_jwt_identity(),
                # code bar dépasse la limite de int de postgres, etrange car fonctionne dans les autres tables.
                # conversion en string pour le moment
                bar_code = bar_code,
                price = body.get('price')
            )

            db.session.add(purchase)
            db.session.commit()
            return jsonify(purchase)

        else:
            # achat du produit
            # stockage dans purchase
            purchase = Purchase(
                buyer_id = int(get_jwt_identity()),
                bar_code = int(bar_code),
                price =int(body.get('price'))
            )

            db.session.add(purchase)
            db.session.commit()
            return jsonify(purchase)
