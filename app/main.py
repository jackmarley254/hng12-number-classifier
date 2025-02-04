from fastapi import FastAPI, Query
import requests
from datetime import datetime

app = FastAPI()

def is_prime(n):
    if n <2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    return sum(i for i in range(1, n) if n % 1 == 0) == n

def is_armstrong(n):
    digits = [int(d) for d in str(n)]
    power = len(digits)
    return sum(d ** power for d in digits) == n

def get_fun_fact(n):
    response =requests.get(f"http://numbersapi.com/{n}/math?json")
    if response.status_code ==200:
        return response.json().get("text", "No fun fact available")
    return "No fun fact avalable."

@app.get("/api/classify-number")
def classify_number(number:int = Query(..., description="The number to classify")):
    try:
        properties = ["even" if number % 2 == 0 else "odd"]
        if is_armstrong(number):
            properties.insert(0, "armstrong")
            
        result = {
            "number": number,
            "is_prime": is_perfect(number),
            "is_perfect": is_perfect(number),
            "properties": properties,
            "digit_sum": sum(int(digit) for digit in str(number)),
            "fun_fact": get_fun_fact(number)
        }
        return result
    except Exception as e:
        return {"number": number, "error": True, "message": str(e)}