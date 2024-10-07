import requests
import json


# ========== GET METHODS ==========

# Get - Brand
def test_get_brand():
    response = requests.get('http://127.0.0.1:8000/brand/')
    assert response.status_code == 200

# Get - Brand ID
def test_get_brand_id():
    response = requests.get('http://127.0.0.1:8000/brand/id/2')
    assert response.status_code == 200

# Get - Brand Name
def test_get_brand_name():
    response = requests.get('http://127.0.0.1:8000/brand/name/Ford')
    assert response.status_code == 200

# Get - Model
def test_get_model():
    response = requests.get('http://127.0.0.1:8000/model/')
    assert response.status_code == 200

# Get - Model ID
def test_get_model_id():
    response = requests.get('http://127.0.0.1:8000/model/id/3')
    assert response.status_code == 200

# Get - Model Name
def test_get_model_name():
    response = requests.get('http://127.0.0.1:8000/model/name/Tacoma')
    assert response.status_code == 200

# Get - Model Year
def test_get_model_year():
    response = requests.get('http://127.0.0.1:8000/model/year/2017')
    assert response.status_code == 200

# Get - Model Body Type
def test_get_model_bodytype():
    response = requests.get('http://127.0.0.1:8000/model/bodytype/SUV')
    assert response.status_code == 200

# Get - Model Power
def test_get_model_power():
    response = requests.get('http://127.0.0.1:8000/model/power/410')
    assert response.status_code == 200

# Get - Model Brand ID
def test_get_model_brand_id():
    response = requests.get('http://127.0.0.1:8000/model/brand/3')
    assert response.status_code == 200


# ========== POST METHODS ==========

# Post - Model
def test_post_model():
    request_data = {"name": "Tacoma",
                    "year": 2015,
                    "body_type": "Truck",
                    "power_hp": 278,
                    "cylinders": 6,
                    "liters": 3.5,
                    "id": 4,
                    "brand_id": 1}
    response = requests.post('http://127.0.0.1:8000//brand/1/model', json=request_data)
    if response.status_code == 200:
        assert response.status_code == 200
    else:
        response_directory = response.json()
        assert 'error' in response_directory.keys()


# Post - Brand
def test_post_brand():
    request_data = {"id": 2,
                    "headquarters_city": "Detroit",
                    "owner_id": 2,
                    "name": "Chevrolet",
                    "country": "USA",
                    "date_founded": 1911}
    response = requests.post('http://127.0.0.1:8000/brand/', json=request_data)
    if response.status_code == 200:
        assert response.status_code == 200
    else:
        response_directory = response.json()
        assert 'error' in response_directory.keys()


# Post - Owner
def test_post_owner():
    request_data = {"name": "",
                    "password": ""}
    response = requests.post('http://127.0.0.1:8000/owner/', json=request_data)
    if response.status_code == 200:
        assert response.status_code == 200
    else:
        response_directory = response.json()
        assert 'error' in response_directory.keys()


# Post - Token
def test_post_token():
    request_data = {"client_id": "",
                    "client_secret": "",
                    "scope": "",
                    "grant_type": "",
                    "refresh_token": "",
                    "username": "Mathias Wouters",
                    "password": "test"}
    response = requests.post('http://127.0.0.1:8000/token', json=request_data)
    if response.status_code == 200:
        assert response.status_code == 200
    else:
        response_directory = response.json()
        assert 'error' in response_directory.keys()

