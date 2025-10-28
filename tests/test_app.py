"""
Test cases for the Flask application
"""
import pytest
import sys
import os

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app, add_numbers, multiply_numbers

@pytest.fixture
def client():
    """Create test client"""
    with app.test_client() as client:
        yield client

def test_add_numbers():
    """Test the add_numbers function"""
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0

def test_multiply_numbers():
    """Test the multiply_numbers function"""
    assert multiply_numbers(2, 3) == 6
    assert multiply_numbers(2, -3) == -6
    assert multiply_numbers(0, 5) == 0

def test_hello_endpoint(client):
    """Test the root endpoint"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome' in response.data

def test_health_check(client):
    """Test health check endpoint"""
    response = client.get('/health')
    assert response.status_code == 200
    assert b'healthy' in response.data

def test_add_endpoint(client):
    """Test add endpoint"""
    response = client.get('/add/5/3')
    assert response.status_code == 200
    assert b'8' in response.data

def test_multiply_endpoint(client):
    """Test multiply endpoint"""
    response = client.get('/multiply/4/5')
    assert response.status_code == 200
    assert b'20' in response.data

def test_users_endpoint(client):
    """Test users endpoint"""
    response = client.get('/users?id=123')
    assert response.status_code == 200
