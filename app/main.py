from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS

# Helper Functions
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    if n < 2:
        return False
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors) == n

def is_armstrong(n):
    digits = list(str(n))
    length = len(digits)
    return sum(int(d)**length for d in digits) == n

def get_digit_sum(n):
    return sum(int(d) for d in str(n))

def get_fun_fact(n):
    try:
        response = requests.get(f"http://numbersapi.com/{n}/math")
        return response.text if response.status_code == 200 else None
    except:
        return None

# API Endpoint
@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    number_param = request.args.get('number')
    
    # Validate input
    if not number_param:
        return jsonify({"number": None, "error": True}), 400
    
    try:
        # Reject floats and non-integers
        if '.' in number_param:
            return jsonify({"number": number_param, "error": True}), 400
        number = int(number_param)
    except ValueError:
        return jsonify({"number": number_param, "error": True}), 400

    # Classify properties
    properties = []
    if is_armstrong(number):
        properties.append("armstrong")
    properties.append("even" if number % 2 == 0 else "odd")

    return jsonify({
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": properties,
        "digit_sum": get_digit_sum(number),
        "fun_fact": get_fun_fact(number)
    }), 200

if __name__ == '__main__':
    app.run(debug=False)