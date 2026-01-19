from flask import Flask, jsonify

app = Flask(__name__) #create a Flask application instance

#Simple route for testing
@app.route('/') #at this route(URL path), the function home will be executed
def home():
    return "Expense Tracker API is running."

if __name__ == '__main__': #runs if this script is run directly (not imported as a module)
    app.run(debug=True) #run the application in debug mode(for learning and development purposes)


#POST endpoint to create a new expense
@app.route('/expenses', methods=['POST']) #tells Flask when a request hits /expenses, and it's a POST request, execute function below
def create_expense():
    return jsonify({
        "message": "POST /expenses endpoint reached"
    }), 201