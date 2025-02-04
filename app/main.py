import os
import uvicorn
from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import requests
from datetime import datetime

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all domains
    allow_credentials=True,
    allow_methods=["GET"],  # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

def is_prime(n: int) -> bool:
    if n <2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n: int) -> bool:
    return sum(i for i in range(1, n) if n % 1 == 0) == n

def is_armstrong(number: int) -> bool:
    digits = [int(digit) for digit in str(number)]
    power = len(digits)
    return sum(digit ** len(digits) for digit in digits) == number

def get_fun_fact(number):
    """Fetch a fun fact from Numbers API"""
    try:
        
        response =requests.get(f"http://numbersapi.com/{number}/math?json", timeout=5)
        return response.text if response.status_code == 200 else "No fun fact available"
    except requests.RequestException:
        return "No fun fact available"

@app.get("/api/classify-number")
def classify_number(number: str = Query(..., description="The number to classify")):
    if not number.lstrip("-").isdigit(): # Ensure it's an integer
       raise HTTPException(status_code=400, detail={"number": number, "error": True})
   
    number = int(number)


    properties = []
    if is_armstrong(number):
        properties.append("armstrong")
    properties.append("odd" if number % 2 else "even")
            
    response = {
            "number": number,
            "is_prime": is_perfect(number),
            "is_perfect": is_perfect(number),
            "properties": properties,
            "digit_sum": sum(map(int, str(abs(number)))),
            "fun_fact": get_fun_fact(number)
        }
    return response
    
if __name__ == "__main__":
   port = int(os.getenv("PORT", 8000))  # Default to 8000 if PORT not set
   uvicorn.run(app, host="0.0.0.0", port=port)   