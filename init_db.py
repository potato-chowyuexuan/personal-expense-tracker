from app import app
from models import db

with app.app_context(): #create temporary application context to let flask know which app and configuration to use
    db.create_all() #create missing database tables based on models defined in models.py
    print("Database initialized and tables created.")