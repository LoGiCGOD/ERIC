# test_app.py
import pytest
import sys
import os

# Add the path to the src directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from app import app

app.testing = True
test_client = app.test_client()

def test_homepage():
    response = test_client.get('/')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Hello, World!'

def test_add_route():
    response = test_client.get('/add/3/5')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'The sum of 3 and 5 is 8.'
