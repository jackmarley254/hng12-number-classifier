from fastapi import FastAPI, Query, HTTPException
import requests

app = FastAPI()

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
@app.get("/api/classify-number")
async def classify_number(number: str = Query(...)):
    # Validate input
    if not number:
        raise HTTPException(status_code=400, detail={"number": None, "error": True})
    
    try:
        # Reject floats and non-integers
        if '.' in number:
            raise HTTPException(status_code=400, detail={"number": number, "error": True})
        number_int = int(number)
    except ValueError:
        raise HTTPException(status_code=400, detail={"number": number, "error": True})

    # Classify properties
    properties = []
    if is_armstrong(number_int):
        properties.append("armstrong")
    properties.append("even" if number_int % 2 == 0 else "odd")

    return {
        "number": number_int,
        "is_prime": is_prime(number_int),
        "is_perfect": is_perfect(number_int),
        "properties": properties,
        "digit_sum": get_digit_sum(number_int),
        "fun_fact": get_fun_fact(number_int)
    }