# 📊 Number Classification API 🚀

## **Overview**
The **Number Classification API** is a fast and scalable API that analyzes a given number and returns its mathematical properties along with a fun fact. It checks if a number is **prime**, **perfect**, or **Armstrong**, and determines whether it is **odd or even**. Additionally, it fetches an interesting fun fact using the [Numbers API](http://numbersapi.com/).  

This project was built as part of **HNG12 Stage 1 Backend Task**.

---

## **📌 Features**
✅ Accepts a number as a query parameter.  
✅ Determines whether the number is **prime**, **perfect**, or an **Armstrong number**.  
✅ Identifies if the number is **odd or even**.  
✅ Computes the **digit sum** of the number.  
✅ Fetches a **fun fact** from an external API.  
✅ Returns a structured **JSON response**.  
✅ Handles **CORS** and provides proper error handling.  
✅ Deployed to a publicly accessible endpoint.  

---

## **🚀 API Endpoint**
### **Base URL:**  https://hng12-number-classifier.onrender.com

- **Method:** `GET`
- **Response Format:** `JSON`

### ✅ Correct Inputs

```
GET /api/classify-number?number=371
```

### Response (200 Ok)

```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

### ❌ Invalid Input - Alphabetic String

```
GET /api/classify-number?number=abc
```

###  Reponse (400 Bad Request)

```json
{
    "number": "alphabet",
    "error": true
}
```

### ❌ Invalid Input - Floating Point

```
GET /api/classify-number?number=3.14
```
### Response (400 Bad Request)

```json
{
    "number": "3.14",
    "error": true
}
```

## Setup Instructions

### 1 Clone the repository

```bash
git clone https://github.com/yourusername/repo-name
cd repo-name
```


### 2 Create a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
### 3 Install dependencies

```bash
pip install -r requirements.txt
```

### 4 Run the Server

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

### Example Usage

#### Using `curl`

```bash
curl -s https://hng12-number-classifier.onrender.com
```

#### Using a browser 

1. Open  your browser.
2. Enter the API URL:
   ```
   https://hng12-number-classifier.onrender.com
   ```
3. Send a `GET` request.
4. View the JSON response

## 📢 Hiring? Let's Talk!

Are you looking for a dedicated backend developer skilled in Python, FastAPI, and scalable APIs? Let's connect and build something amazing! 🚀 [HNG Tech - Hire Python Developers](https://hng.tech/hire/python-developers).

## 📚 Resources & References

🔗 **Numbers API:** [http://numbersapi.com/]
🔗 **Parity in Mathematics (Wikipedia):** [https://en.wikipedia.org/wiki/Parity_(mathematics)]
🔗 FastAPI Docs
🔗 Python Requests Library

## 📝 License

This project is open-source and available under the **MIT License**.

## 📢 About Me

I'm a passionate Backend Software Engineer currently honing my skills and building scalable APIs. Follow my journey as I strive to become one of the best in the field! 🚀

## 📩 Let's Connect:
💎 **Email:** [jackndiritu97@gmail.com](mailto:jackndiritu97@gmail.com)\
🔗 **GitHub:** [jackmarley254](https://github.com/jackmarley254)\
🔗 **LinkedIn:** [Jackson Gitahi](https://linkedin.com/in/jackson-gitahi)
💎 **X:** [Jackson Ndiritu](https://x.com/ndiritu_jack)