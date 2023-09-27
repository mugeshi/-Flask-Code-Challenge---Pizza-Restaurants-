# Title: A Flask API for Pizza_Restaurants

## Author: Nicole Njeri

### Date: September 22, 2023

### Introduction
Welcome to Pizzainn, a unique project that involves building a Flask API for managing Pizza Restaurants. In this assessment, we will deliver into the world of pizza establishments and create a robust API that offers a range of functionalities described in the following sections.

### Project Overview
In this project, we aim to create a Flask API that manages Pizza Restaurants and their associated pizzas. The core relationships in our database involve Restaurants having many Pizzas through a junction table called RestaurantPizza, and Pizzas having many Restaurants through the same junction table.

### Models and Migrations
To get started, we'll need to create database models and migrations for the following tables:

### Restaurant

id (Primary Key)
name (String, max length 50, unique)
address (String)
Pizza

id (Primary Key)
name (String)
ingredients (String)
RestaurantPizza

id (Primary Key)
price (Float, between 1 and 30)
restaurant_id (Foreign Key)
pizza_id (Foreign Key)
Validations
We will apply the following validations to our models:

### RestaurantPizza

Price must be between 1 and 30.
Restaurant

Name must be less than 50 characters.
Name must be unique.
API Routes
We will set up the following API routes, ensuring they return JSON data in the specified format:

GET /restaurants

Return a list of restaurants in the following format:
json
Copy code
[
  {
    "id": 1,
    "name": "pizzainn",
    "address": "pizzainn,kimathi road, 5th Avenue"
  },
  {
    "id": 2,
    "name": "Pizza Hut",
    "address": "Westgate Mall, Mwanzi Road, Nrb 100"
  }
]
GET /restaurants/:id

If the restaurant exists, return its details along with associated pizzas in the following format:
json
Copy code
{
  "id": 1,
  "name": " Pizzainn",
  "address": "pizzainn, kimathi road, 5th Avenue",
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
If the restaurant does not exist, return a "Restaurant not found" error with the appropriate HTTP status code.
DELETE /restaurants/:id

If the restaurant exists, delete it from the database along with associated RestaurantPizzas.
Return an empty response body with the appropriate HTTP status code.
If the restaurant does not exist, return a "Restaurant not found" error with the appropriate HTTP status code.
GET /pizzas

Return a list of pizzas in the following format:
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
POST /restaurant_pizzas

Create a new RestaurantPizza associated with an existing Pizza and Restaurant.
Accept an object with the following properties in the request body:
json
Copy code
{
  "price": 5,
  "pizza_id": 1,
  "restaurant_id": 3
}
If the RestaurantPizza is created successfully, respond with data related to the Pizza:
json
Copy code
{
  "id": 1,
  "name": "Cheese",
  "ingredients": "Dough, Tomato Sauce, Cheese"
}
If the RestaurantPizza creation is not successful due to validation errors, return a "validation errors" message along with the appropriate HTTP status code.
Technologies Used
Python 3
Flask
SQLAlchemy
Project Setup
To get started with the project, follow these steps:

Clone the repository: git clone <https://github.com/mugeshi/-Flask-Code-Challenge---Pizza-Restaurants>.
Activate a virtual environment: pipenv shell.
Install project dependencies: pipenv install.
Navigate to the project directory: cd Pizza-Fusion.
Enter the server directory.
Run the Flask application using python app.py.
### Testing
You can test the API endpoints using Postman or any other API testing tool.

### Known Bugs
There are currently no known bugs in this project.

### Support and Contact
For contributions or suggestions, please contact us via email:

Email: nicolemugeshi@gmail.com

### License
This project is licensed under the Penda Kujua Company.
THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
