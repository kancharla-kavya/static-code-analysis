"""
Main application module for Static Analysis Demo
"""
from flask import Flask, jsonify, request
import os

app = Flask(__name__)

def add_numbers(a: int, b: int) -> int:
    """
    Add two numbers and return the result
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        Sum of a and b
    """
    result = a + b
    return result

def multiply_numbers(a: int, b: int) -> int:
    """
    Multiply two numbers using repeated addition
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        Product of a and b
    """
    # This method has some complexity for analysis
    result = 0
    for i in range(abs(b)):
        result += a
    if b < 0:
        result = -result
    return result

@app.route('/')
def hello_world():
    """Root endpoint returning welcome message"""
    return jsonify({
        "message": "Welcome to Static Analysis Demo API",
        "status": "success"
    })

@app.route('/health')
def health_check():
    """Health check endpoint"""
    return jsonify({"status": "healthy"})

@app.route('/add/<int:a>/<int:b>')
def add_endpoint(a, b):
    """Endpoint to add two numbers"""
    try:
        result = add_numbers(a, b)
        return jsonify({
            "operation": "addition",
            "result": result,
            "numbers": [a, b]
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/multiply/<int:a>/<int:b>')
def multiply_endpoint(a, b):
    """Endpoint to multiply two numbers"""
    try:
        result = multiply_numbers(a, b)
        return jsonify({
            "operation": "multiplication",
            "result": result,
            "numbers": [a, b]
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/users')
def get_users():
    """Endpoint that has a potential security issue for demonstration"""
    user_id = request.args.get('id', '')
    # This will be flagged by security tools - potential injection
    message = f"User ID: {user_id}"
    return jsonify({"message": message})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
