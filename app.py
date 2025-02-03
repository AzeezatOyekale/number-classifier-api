from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # This allows cross-origin requests

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    try:
        # Get the number from the query parameters
        number = request.args.get('number')

        # Ensure the input is a valid integer
        if not number.isdigit():
            return jsonify({"number": number, "error": True}), 400

        number = int(number)

        # Check if the number is prime (a simple check)
        is_prime = check_prime(number)

        # Check if the number is a perfect number (e.g., 6, 28)
        is_perfect = check_perfect(number)

        # Check Armstrong number
        is_armstrong = check_armstrong(number)

        # Find the number's properties (odd/even)
        parity = 'odd' if number % 2 != 0 else 'even'

        # Get fun fact from Numbers API
        fun_fact = get_fun_fact(number)

        # Build the response
        properties = []
        if is_armstrong:
            properties.append("armstrong")
        if parity == 'odd':
            properties.append("odd")
        else:
            properties.append("even")

        # Prepare the response
        response = {
            "number": number,
            "is_prime": is_prime,
            "is_perfect": is_perfect,
            "properties": properties,
            "digit_sum": sum(int(digit) for digit in str(number)),
            "fun_fact": fun_fact
        }

        return jsonify(response), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

def check_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def check_perfect(num):
    divisors = [i for i in range(1, num) if num % i == 0]
    return sum(divisors) == num

def check_armstrong(num):
    digits = str(num)
    power = len(digits)
    return sum(int(digit) ** power for digit in digits) == num

def get_fun_fact(num):
    url = f"http://numbersapi.com/{num}?json"
    response = requests.get(url)
    return response.json().get("text", "No fun fact available.")

if __name__ == '__main__':
    app.run(debug=True)
