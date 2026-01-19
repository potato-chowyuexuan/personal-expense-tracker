from flask import Flask
app = Flask(__name__) #create a Flask application instance

#Simple route for testing
@app.route('/') #at this route(URL path), the function home will be executed
def home():
    return "Expense Tracker API is running."

if __name__ == '__main__': #runs if this script is run directly (not imported as a module)
    app.run(debug=True) #run the application in debug mode(for learning and development purposes)


#POST endpoint to create a new expense
from flask import request, jsonify
from models import db, Expense

@app.route('/expenses', methods=['POST']) #tells Flask when a request hits /expenses, and it's a POST request, execute function below
def create_expense():
    data = request.get_json() #takes raw HTTP body and converts it into a Python dictionary, if not JSON, returns None
    if not data: #check if JSON data is provided
        return jsonify({"error": "No input data provided"}), 400 #HTTP status code for bad request
    
    #Validate required fields
    required_fields = ["title", "amount", "date"]
    missing_fields = [field for field in required_fields if field not in data] #list comprehension, create new list for fields that are missing
    if missing_fields: #check if all required fields are present
        return jsonify({"error": f"Missing fields: {','.join(missing_fields)}"}), 400 #String join method to create comma-separated string of missing fields: "amount,date"
    
    #Create Expense object
    expense = Expense(
        title=data['title'],
        amount=data['amount'],
        date=data['date']
    )

    #Add to session and commit to database
    db.session.add(expense)
    db.session.commit()
    
    #Return success response
    return jsonify({
        "message": "Expense added successfully",
        "expense": {
            "id": expense.id,
            "title": expense.title,
            "amount": expense.amount,
            "date": expense.date
        }
    }), 201 #HTTP status code for created

#GET endpoint to retrieve all expenses
@app.route('/expenses', methods=['GET']) #when a GET request hits /expenses, execute function below
def get_expenses():