Pizza Restaurant API
Welcome to the Pizza Restaurant API! This API allows you to interact with pizza restaurants and their menus.

Table of Contents
Installation
Usage
Endpoints
Contributing
License
Installation
Clone this repository to your local machine.
Install the required dependencies using pip install -r requirements.txt.
Create a SQLite database named pizza_restaurants.db.
Run migrations to set up the database tables using flask db upgrade.
Usage
To start the Flask server, run python app.py in your terminal. You can then use tools like Postman to make requests to the API.

Endpoints
Get All Restaurants
URL: /restaurants
Method: GET
Description: Get a list of all pizza restaurants.
Sample Response:
json
Copy code
[
  {
    "id": 1,
    "name": "Dominion Pizza",
    "address": "Good Italian, Ngong Road, 5th Avenue"
  },
  {
    "id": 2,
    "name": "Pizza Hut",
    "address": "Westgate Mall, Mwanzi Road, Nrb 100"
  }
]
Get Restaurant by ID
URL: /restaurants/:id
Method: GET
Description: Get details of a restaurant by its ID.
Sample Response (if found):
json
Copy code
{
  "id": 1,
  "name": "Dominion Pizza",
  "address": "Good Italian, Ngong Road, 5th Avenue",
  "pizzas": [
    {
      "id": 1,
      "name": "Cheese",
      "ingredients": "Dough, Tomato Sauce, Cheese"
    },
    {
      "id": 2,
      "name": "Pepperoni",
      "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni"
    }
  ]
}
Sample Response (if not found):
json
Copy code
{
  "error": "Restaurant not found"
}
Delete Restaurant by ID
URL: /restaurants/:id
Method: DELETE
Description: Delete a restaurant by its ID. Also deletes associated menu items.
Sample Response (if successful):
scss
Copy code
No content (204)
Sample Response (if not found):
json
Copy code
{
  "error": "Restaurant not found"
}
Get All Pizzas
URL: /pizzas
Method: GET
Description: Get a list of all available pizzas.
Sample Response:
json
Copy code
[
  {
    "id": 1,
    "name": "Cheese",
    "ingredients": "Dough, Tomato Sauce, Cheese"
  },
  {
    "id": 2,
    "name": "Pepperoni",
    "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni"
  }
]
Create Restaurant Pizza
URL: /restaurant_pizzas
Method: POST
Description: Create a new menu item for a restaurant.
Request Body:
json
Copy code
{
  "price": 5,
  "pizza_id": 1,
  "restaurant_id": 3
}
Sample Response (if successful):
json
Copy code
{
  "id": 1,
  "name": "Cheese",
  "ingredients": "Dough, Tomato Sauce, Cheese"
}
Sample Response (if validation errors):
json
Copy code
{
  "errors": ["Validation errors"]
}


License
This project is licensed under the penda kujua License.