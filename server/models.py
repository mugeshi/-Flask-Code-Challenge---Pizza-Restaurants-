from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Restaurant(db.Model):
    __tablename__ = 'restaurants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    address = db.Column(db.String(255), nullable=False)
    # Define a relationship to Pizza through the RestaurantPizza association table
    pizzas = db.relationship('Pizza', secondary='restaurant_pizzas', back_populates='restaurants')


    def __init__(self, name, address):
        self.name = name
        self.address = address

class Pizza(db.Model):
    __tablename__ = 'pizzas'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    ingredients = db.Column(db.String(255), nullable=False)
    # Define a relationship to Restaurant through the RestaurantPizza association table
    restaurants = db.relationship('Restaurant', secondary='restaurant_pizzas', back_populates='pizzas')


    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

class RestaurantPizza(db.Model):
    __tablename__ = 'restaurant_pizzas'

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float, nullable=False)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'), nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'), nullable=False)
 


    def __init__(self, price, pizza_id, restaurant_id):
        self.price = price
        self.pizza_id = pizza_id
        self.restaurant_id = restaurant_id
