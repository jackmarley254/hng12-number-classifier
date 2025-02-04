from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (Change this for security in production)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

@app.get("/api/classify-number")
async def classify_number(number: str):
    # Validate if number is an integer
    if not number.lstrip('-').isdigit():
        return JSONResponse(
            status_code=400,
            content={"number": number, "error": True}
        )
    
    # Convert to integer
    num = int(number)

    # Classification logic here...
    return {
        "number": num,
        "is_prime": False,  # Example
        "is_perfect": False,  # Example
        "properties": ["odd"],  # Example
        "digit_sum": sum(int(digit) for digit in str(abs(num))),  # Handle negatives
        "fun_fact": "This is a fun fact"  # Placeholder
    }
