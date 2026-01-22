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
@app.route('/expenses', methods=['GET'])
def get_expenses():
    expenses = Expense.query.all() #fetch all expense records from the database
    expenses_list = [
        {
            "id": e.id,
            "title": e.title,
            "amount": e.amount,
            "date": e.date
        } for e in expenses
    ] #list comprehension to create a list of expense dictionaries
    return jsonify(expenses_list), 200



#GET endpoint to retrieve a single expense by ID
@app.route("/expenses/<int:expense_id>", methods=['GET'])
def get_expense(expense_id):
    expense = Expense.query.get(expense_id)
    if not expense: 
        return jsonify({"error": f"Expense with id {expense_id} not found"}), 404
    
    expense_data = {
        "id": expense.id,
        "title": expense.title,
        "amount": expense.amount,
        "date": expense.date
    }
    return jsonify(expense_data), 200



#DELETE endpoint to delete an expense by ID
@app.route("/expenses/<int:expense_id>", methods=['DELETE']) #methods act like an instruction to Flask on how to handle requests 
def delete_expense(expense_id):
    expense = Expense.query.get(expense_id) #fetch the expense record with the given ID from the database
    if not expense: #check if the expense exists
        return jsonify({"error": f"Expense with id {expense_id} not found"}), 404
    
    db.session.delete(expense) #delete the expense record from the session
    db.session.commit() #commit the changes

    return jsonify({"message": f"Expense with id {expense_id} deleted successfully"}), 200



#PUT endpoint to update an existing expense by ID
@app.route("/expenses/<int:expense_id>", methods = ["PUT"])
def update_expense(expense_id):
    expense = Expense.query.get(expense_id) #fetch the expense record with the given ID from the database
    if not expense:
        return jsonify({"error": "No input data provided"}), 400

    data = request.get_json() #takes raw HTTP body and converts it into a Python dictionary, if not JSON, returns None
    if not data: #check if JSON data is provided
        return jsonify({"error": "No input data provided"}), 400
    if "title" in data:
        expense.title = data["title"]
    if "amount" in data:
        expense.amount = data["amount"]
    if "date" in data:
        expense.date = data["date"]

    db.session.commit()

    return jsonify({
        "message": f"Expense with id {expense_id} updated successfully",
        "expense": {
            "id": expense.id,
            "title": expense.title,
            "amount": expense.amount,
            "date": expense.date
        }
    }), 200
