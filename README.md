# Number Classification API

This API classifies a number and provides interesting mathematical properties and a fun fact.

## Endpoint

- **GET** `/api/classify-number?number=<number>`

### Example Request

```bash
GET http://<your-public-url>/api/classify-number?number=371

Example Response (200 OK)
json
Copy
Edit
{
  "number": 371,
  "is_prime": false,
  "is_perfect": false,
  "properties": ["armstrong", "odd"],
  "digit_sum": 11,
  "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
Example Response (400 Bad Request)
json
Copy
Edit
{
  "number": "alphabet",
  "error": true
}
Running Locally
Clone this repository
Set up a Python virtual environment and install dependencies
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
pip install -r requirements.txt
Run the app
bash
Copy
Edit
python app.py
Deployment
You can deploy this API using services like Render or Heroku.

Technologies Used
Python
Flask
Requests (for Numbers API)
markdown
Copy
Edit

### **3. Save and Commit the README.md**

1. Save the `README.md` file.
2. **Add it to Git**:
   - Run the following commands in your terminal (if you're using Git):
     ```bash
     git add README.md
     git commit -m "Added README file"
     git push origin main
     ```
