from flask import Flask

app = Flask(__name__) #create a Flask application instance

@app.route('/') #at this route(URL path), the function home will be executed
def home():
    return "Expense Tracker API is running."

if __name__ == '__main__': #runs if this script is run directly (not imported as a module)
    app.run(debug=True) #run the application in debug mode(for learning and development purposes)