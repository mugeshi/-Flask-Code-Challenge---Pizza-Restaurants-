import pytest
from ..app import app, db, Restaurant, Pizza


@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()

    # Create an in-memory SQLite database for testing
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    db.init_app(app)
    with app.app_context():
        db.create_all()
    
    yield client

def test_post_restaurant(client):
    # Create a new restaurant using a POST request
    new_restaurant_data = {
        'name': 'New Restaurant',
        'address': '789 Oak St'
    }
    response = client.post('/restaurants', json=new_restaurant_data)

    # Check if the response status code is 201 Created
    assert response.status_code == 201

    # Check if the response data contains the newly created restaurant
    created_restaurant = response.get_json()
    assert created_restaurant['name'] == new_restaurant_data['name']
    assert created_restaurant['address'] == new_restaurant_data['address']

def test_get_restaurant_by_id(client):
    # Create a sample restaurant
    sample_restaurant = Restaurant(name='Sample Restaurant', address='456 Elm St')
    with app.app_context():
        db.session.add(sample_restaurant)
        db.session.commit()

    # Send a GET request to retrieve the restaurant by ID
    response = client.get(f'/restaurants/{sample_restaurant.id}')

    # Check if the response status code is 200 OK
    assert response.status_code == 200

    # Check if the response data matches the expected restaurant data
    expected_data = {
        'id': sample_restaurant.id,
        'name': sample_restaurant.name,
        'address': sample_restaurant.address,
        'pizzas': []
    }
    assert response.get_json() == expected_data

def test_post_pizza(client):
    # Create a new pizza using a POST request
    new_pizza_data = {
        'name': 'New Pizza',
        'ingredients': 'Ingredient 1, Ingredient 2'
    }
    response = client.post('/pizzas', json=new_pizza_data)

    # Check if the response status code is 201 Created
    assert response.status_code == 201

    # Check if the response data contains the newly created pizza
    created_pizza = response.get_json()
    assert created_pizza['name'] == new_pizza_data['name']
    assert created_pizza['ingredients'] == new_pizza_data['ingredients']

def test_get_pizza_by_id(client):
    # Create a sample pizza
    sample_pizza = Pizza(name='Sample Pizza', ingredients='Ingredient 3, Ingredient 4')
    with app.app_context():
        db.session.add(sample_pizza)
        db.session.commit()

    # Send a GET request to retrieve the pizza by ID
    response = client.get(f'/pizzas/{sample_pizza.id}')

    # Check if the response status code is 200 OK
    assert response.status_code == 200

    # Check if the response data matches the expected pizza data
    expected_data = {
        'id': sample_pizza.id,
        'name': sample_pizza.name,
        'ingredients': sample_pizza.ingredients,
        'restaurants': []
    }
    assert response.get_json() == expected_data


if __name__ == '__main__':
    pytest.main()
