from app import app, db, Restaurant, Pizza

# Create an app context to work with the database
with app.app_context():
    # Drop all existing tables (for development/testing purposes)
    db.drop_all()

    # Create the tables
    db.create_all()

   
    restaurants_data = [
        {"name": "pzzainn", "address": " pizzainn, kimathi road, 5th Avenue"},
        {"name": "Pizzainn", "address": "big knife, ngong road,  Nrb 100"},
        {"name": "Restaurant 3", "address": "Address 3"},
        {"name": "Restaurant 4", "address": "Address 4"},
        {"name": "Restaurant 5", "address": "Address 5"},
        {"name": "Restaurant 6", "address": "Address 6"},
        {"name": "Restaurant 7", "address": "Address 7"},
        {"name": "Restaurant 8", "address": "Address 8"},
        {"name": "Restaurant 9", "address": "Address 9"},
        {"name": "Restaurant 10", "address": "Address 10"},
        {"name": "Restaurant 11",  "address": "Address 11"},
        {"name": "Restaurant 12",  "address": "Address 12"}
      
    ]

    pizzas_data = [
        {"name": "Cheese", "ingredients": "Tomato sauce Cheese"},
        {"name": "Pepperoni", "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni"},
        {"name": "Pizza 3", "ingredients": "Ingredients 3"},
        {"name": "Pizza 4", "ingredients": "Ingredients 4"},
        {"name": "Pizza 5", "ingredients": "Ingredients 5"},
        {"name": "Pizza 6", "ingredients": "Ingredients 6"},
        {"name": "Pizza 7", "ingredients": "Ingredients 7"},
        {"name": "Pizza 8", "ingredients": "Ingredients 8"},
        {"name": "Pizza 9", "ingredients": "Ingredients 9"},
        {"name": "Pizza 10", "ingredients": "Ingredients 10"},
       
    ]

    # Add sample restaurants to the database
    for restaurant_info in restaurants_data:
        restaurant = Restaurant(**restaurant_info)
        db.session.add(restaurant)

    # Add sample pizzas to the database
    for pizza_info in pizzas_data:
        pizza = Pizza(**pizza_info)
        db.session.add(pizza)

    # Commit the changes to the database
    db.session.commit()

print("Database seeding complete.")
