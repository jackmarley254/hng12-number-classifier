from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

# Enable CORS for cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (Change this for security in production)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

# Function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Function to check if a number is an Armstrong number
def is_armstrong(n):
    if n < 0:
        return False  # Negative numbers cannot be Armstrong numbers
    digits = list(map(int, str(n)))
    power = len(digits)
    return sum(d ** power for d in digits) == n

# Function to check if a number is a perfect number
def is_perfect(n):
    if n < 1:
        return False  # Negative numbers and zero cannot be perfect
    return sum(i for i in range(1, n) if n % i == 0) == n

# Function to get a fun fact from Numbers API
def get_fun_fact(num):
    try:
        response = requests.get(f"http://numbersapi.com/{num}/math")
        if response.status_code == 200:
            return response.text
    except:
        return "No fun fact available."
    return "No fun fact available."

@app.get("/api/classify-number")
async def classify_number(number: str):
    # Validate input to reject non-integer values (floats, strings, etc.)
    if not number.lstrip('-').isdigit() or "." in number:
        return JSONResponse(
            status_code=400,
            content={"number": number, "error": True}
        )

    # Convert to integer
    num = int(number)

    # Define properties (order matters)
    properties = []
    
    if num >= 0 and is_armstrong(num):
        properties.append("armstrong")
    
    # Determine if the number is odd or even
    if num % 2 != 0:
        properties.append("odd")
    else:
        properties.append("even")

#    if is_armstrong(num):
#        properties.append("armstrong")
#    properties.append("odd" if num % 2 != 0 else "even")

    # Construct response
    response_data = {
        "number": num,
        "is_prime": is_prime(num),
        "is_perfect": is_perfect(num),
        "properties": properties,
        "digit_sum": sum(map(int, str(abs(num)))),  # Sum of absolute digits
        "fun_fact": get_fun_fact(num)  # Get fun fact
    }

    return response_data
