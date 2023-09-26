
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Restaurant(db.Model):
    # Define the 'restaurants' table
    __tablename__ = 'restaurants'

    # Primary key for the restaurant
    id = db.Column(db.Integer, primary_key=True)
    
    # Name of the restaurant (max 50 characters, unique, and required)
    name = db.Column(db.String(50), unique=True, nullable=False)
    
    # Address of the restaurant (max 255 characters and required)
    address = db.Column(db.String(255), nullable=False)
    
    # Define a many-to-many relationship with Pizza through the RestaurantPizza association table
    pizzas = db.relationship('Pizza', secondary='restaurant_pizzas', back_populates='restaurants')

    def __init__(self, name, address):
        self.name = name
        self.address = address

class Pizza(db.Model):
    # Define the 'pizzas' table
    __tablename__ = 'pizzas'

    # Primary key for the pizza
    id = db.Column(db.Integer, primary_key=True)
    
    # Name of the pizza (max 50 characters and required)
    name = db.Column(db.String(50), nullable=False)
    
    # Ingredients of the pizza (max 255 characters and required)
    ingredients = db.Column(db.String(255), nullable=False)
    
    # Define a many-to-many relationship with Restaurant through the RestaurantPizza association table
    restaurants = db.relationship('Restaurant', secondary='restaurant_pizzas', back_populates='pizzas')

    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

class RestaurantPizza(db.Model):
    # Define the 'restaurant_pizzas' table
    __tablename__ = 'restaurant_pizzas'

    # Primary key for the RestaurantPizza entry
    id = db.Column(db.Integer, primary_key=True)
    
    # Price of the pizza at this restaurant (required and must be a float)
    price = db.Column(db.Float, nullable=False)
    
    # Foreign key to connect to the 'pizzas' table
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'), nullable=False)
    
    # Foreign key to connect to the 'restaurants' table
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'), nullable=False)

    def __init__(self, price, pizza_id, restaurant_id):
        self.price = price
        self.pizza_id = pizza_id
        self.restaurant_id = restaurant_id
