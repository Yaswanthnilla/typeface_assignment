from flask import Flask, jsonify, request
from sqlalchemy.orm import Session
from sqlalchemy import func
from backend.models import Restaurant, engine
# from flask_sqlalchemy import SQLAlchemy
import random,math
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()

@app.route('/restaurant/<int:restaurant_id>', methods=['GET'])
def get_restaurants_by_id(restaurant_id):
    with Session(engine) as session:
        restaurant = session.query(Restaurant).filter(Restaurant.Restaurant_ID == restaurant_id).first()
        if restaurant is None:
            return jsonify({"error": "Restaurant not found"}), 404
        return jsonify(restaurant.to_dict())


@app.route('/restaurants', methods=['GET'])
def get_paginated_restaurants():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int) 

    offset = (page - 1) * per_page

    with Session(engine) as session:
        query = session.query(Restaurant)
        total = query.count() 
        restaurants = query.offset(offset).limit(per_page).all() 
        
        # Create response data
        response_data = {
            "total": total,
            "total_pages": math.ceil(total/10),
            "page": page,
            "per_page": per_page,
            "restaurants_data": [restaurant.to_dict() for restaurant in restaurants]
        }

        return jsonify(response_data)
    

@app.route('/restaurants/random', methods=['GET'])
def get_random_restaurants():
    with Session(engine) as session:
        random_restaurants = session.query(Restaurant).filter().order_by(func.random()).limit(10).all()
        return jsonify([restaurant.to_dict() for restaurant in random_restaurants])




if __name__ == '__main__':
    app.run(debug=True)


