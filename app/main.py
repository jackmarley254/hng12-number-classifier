from fastapi import FastAPI, Query, HTTPException
import requests
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def is_armstrong(number: int) -> bool:
    """Check if a number is an Armstrong number."""
    if number < 0:
        return False
    digits = [int(digit) for digit in str(number)]
    return sum(digit ** len(digits) for digit in digits) == number

def is_prime(n: int) -> bool:
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n: int) -> bool:
    """Check if a number is a perfect number."""
    if n <= 0:
        return False
    return sum(i for i in range(1, n) if n % i == 0) == n

def get_fun_fact(number: int) -> str:
    """Fetch a fun fact from the Numbers API."""
    try:
        response = requests.get(f"http://numbersapi.com/{number}/math", timeout=5)
        return response.text if response.status_code == 200 else "No fun fact available"
    except requests.RequestException:
        return "No fun fact available"

@app.get("/api/classify-number")
def classify_number(number: str = Query(..., description="Number to classify")):
    """Classify a given number with its mathematical properties."""
    
    # Validate integer input (reject floats, strings, etc.)
    if number.lstrip("-").isdigit() == False or "." in number:
        raise HTTPException(status_code=400, detail={"number": number, "error": True})

    number = int(number)  # Convert valid input to integer

    # Classify number properties
    properties = []
    if is_armstrong(number):
        properties.append("armstrong")
    properties.append("odd" if number % 2 else "even")

    response = {
        "number": number,
        "is_prime": is_prime(number) if number > 0 else False,
        "is_perfect": is_perfect(number) if number > 0 else False,
        "properties": properties,
        "digit_sum": sum(map(int, str(abs(number)))) * (-1 if number < 0 else 1),
        "fun_fact": get_fun_fact(number)
    }

    return response
