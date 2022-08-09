from flask import request
from flask import jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
from services.open_food_fact import open_food_fact
from database.models import db, Product, Purchase
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.exc import MultipleResultsFound

class RankUsersAPI(Resource):
	@jwt_required()
	def get(self):
	# rank users by number of purchases
		users = db.session.query(Purchase.user_id, db.func.count(Purchase.user_id)).group_by(Purchase.user_id).order_by(db.func.count(Purchase.user_id).desc()).all()
		return jsonify(users)

 #---------------------------------------------------------------------------------------------------------------#

class RankProductsAPI(Resource):
	@jwt_required()
	def get(self):
		# rank products by number of purchases
		products = db.session.query(Purchase.bar_code, db.func.count(Purchase.bar_code)).group_by(Purchase.bar_code).order_by(db.func.count(Purchase.bar_code).desc()).all()
		return jsonify(products)
