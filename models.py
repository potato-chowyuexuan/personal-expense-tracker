from flask_sqlalchemy import SQLAlchemy
from app import app #import object 'app' to link to SQLAlchemy

#configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expenses.db' #use SQLite database named expenses.db
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #disable modification tracking to save resources

db = SQLAlchemy(app) #create SQLAlchemy object linked to Flask app above

#Define Expense model
class Expense(db.Model): #every class inherits from db.Model becomes a table
    id = db.Column(db.Integer, primary_key=True) #a column in Expense table, primary key=True is unique identifier (auto-incremented with each new row: 1,2,3...)
    title = db.Column(db.String(100), nullable=False) #max length 100 characters, cannot be null(empty)
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.String(10),nullable=False)

    def __repr__(self): #__repr__ method defines how an object is displayed when printed or in console, useful for debugging
        return f"<Expense {self.title} | ${self.amount} | {self.date}>" #returns display only showing the title of the expense instead of memory address