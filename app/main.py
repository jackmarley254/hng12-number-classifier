from flask import Flask, request, jsonify  
import requests
from flask_cors import CORS  
 

app = Flask(__name__)
CORS(app)

@app.route('/api/classify-number', methods=['GET'])  
def classify_number():  
    number = request.args.get('number')  
    try:  
        number = int(number)  
    except (ValueError, TypeError):  
        return jsonify({"number": number, "error": True}), 400  

    is_prime = is_prime_number(number)  
    is_perfect = is_perfect_number(number)  
    properties = classify_properties(number)  
    digit_sum = sum_of_digits(number)  
    fun_fact = get_fun_fact(number)  

    return jsonify({  
        "number": number,  
        "is_prime": is_prime,  
        "is_perfect": is_perfect,  
        "properties": properties,  
        "digit_sum": digit_sum,  
        "fun_fact": fun_fact  
    })  

def is_prime_number(n):  
    if n < 2:  
        return False  
    for i in range(2, int(n**0.5) + 1):  
        if n % i == 0:  
            return False  
    return True  

def is_perfect_number(n):  
    if n < 2:  
        return False  
    sum_divisors = sum(i for i in range(1, n) if n % i == 0)  
    return sum_divisors == n  

def classify_properties(n):  
    properties = []  
    if is_armstrong_number(n):  
        properties.append("armstrong")  
    properties.append("odd" if n % 2 != 0 else "even")  
    return properties  

def is_armstrong_number(n):  
    digits = [int(d) for d in str(n)]  
    num_digits = len(digits)  
    armstrong_sum = sum(d ** num_digits for d in digits)  
    return armstrong_sum == n  

def sum_of_digits(n):  
    return sum(int(d) for d in str(n))  

def get_fun_fact(n):  
    url = f"http://numbersapi.com/{n}/math"  
    response = requests.get(url)  
    return response.text  

if __name__ == '_main_':  
    app.run(debug=True)