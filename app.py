from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    try:
        # Get the number from query parameters
        number = request.args.get('number')

        if not number:
            return jsonify({"error": "No input provided"}), 400
        elif number.isdigit():
            number = int(number)  # Convert to integer
            
        elif number.isalpha():
            return jsonify({"number": "alphabet","error":"true"}), 400
        elif number.isalnum():
            return jsonify({"number": "alphanumeric","error":"true"}), 400
        else:
            return jsonify({"number": "unknown", "error": "true"}), 400

        # Check if the number has special properties
        is_prime = check_prime(number)
        is_perfect = check_perfect(number)
        is_armstrong = check_armstrong(number)
        parity = "odd" if number % 2 != 0 else "even"

        # Get fun fact from Numbers API
        fun_fact = get_fun_fact(number)

        # Build response properties
        properties = []
        if is_armstrong:
            properties.append("armstrong")
        if is_prime:
            properties.append("prime")
        if is_perfect:
            properties.append("perfect")
        properties.append(parity)  # Add "odd" or "even"

        # Prepare response
        response = {
            "number": number,
        
            "is_prime": is_prime,
            "is_perfect": is_perfect,
            "is_armstrong": is_armstrong,
            "properties": properties,
            "digit_sum": sum(int(digit) for digit in str(number)),
            "fun_fact": fun_fact
        }

        return jsonify(response), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Function to check if a number is prime
def check_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Function to check if a number is a perfect number
def check_perfect(num):
    divisors = [i for i in range(1, num) if num % i == 0]
    return sum(divisors) == num

# Function to check if a number is an Armstrong number
def check_armstrong(num):
    digits = str(num)
    power = len(digits)
    return sum(int(digit) ** power for digit in digits) == num

# Function to get a fun fact about the number
def get_fun_fact(num):
    try:
        url = f"http://numbersapi.com/{num}?json"
        response = requests.get(url)
        response.raise_for_status()  # Raise an error if request fails
        return response.json().get("text", "No fun fact available.")
    except requests.exceptions.RequestException:
        return "Fun fact service unavailable."

if __name__ == '__main__':
    app.run(debug=True)
