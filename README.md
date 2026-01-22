# Personal Expense Tracker API

## Overview

### Project goal
Build a backend web application that allows users to create, view, update, and delete personal expense records via RESTful APIs, with data stored persistently in a SQLite database.

### Expected time
2 weeks, 1-2 hrs per day

---

## Core Features
* Create a new expense record (title, amount, date)
* Retrieve all expense records
* Retrieve a specific expense record
* Update an existing expense record
* Delete an expense record
* Input validation and error handling

---

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| /expenses | POST | Create a new expense |
| /expenses | GET | Retrieve all expenses |
| /expenses/<id> | GET | Retrieve a specific expense |
| /expenses/<id> | PUT | Update an expense |
| /expenses/<id> | DELETE | Delete an expense |

### Examples

**Create an expense**

**POST /expenses**  

Request body:
```json
{
  "title": "Lunch",
  "amount": 12.5,
  "date": "2026-01-19"
}
```
Response:
```json
{
  "message": "Expense created successfully",
  "expense": {
    "id": 1,
    "title": "Lunch",
    "amount": 12.5,
    "date": "2026-01-19"
  }
}
```
**Update an expense**

**PUT /expenses/1**
Request body:
```json
{
  "title": "Dinner",
  "amount": 20.0
}
```
Response:
```json
{
  "message": "Expense with id 1 updated successfully",
  "expense": {
    "id": 1,
    "title": "Dinner",
    "amount": 20.0,
    "date": "2026-01-19"
  }
}
```
**Delete an expense**

**DELETE /expenses/1**

Response:
```json
{
  "message": "Expense with id 1 deleted successfully"
}
```
---

# Tech Stack

**Backend**
* Python
* Flask

**Database**
* SQLite
* SQLAlchemy ORM

**Frontend (optional / for testing)**
* HTML
* CSS
* JavaScript

**Tools**
* Git
* GitHub

---

# Getting Started

**1. Clone the repository**
```bash
git clone https://github.com/potato-chowyuexuan/personal-expense-tracker
cd personal-expense-tracker
```
**2. Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
```
**3. Install dependencies**
```bash
pip install -r requirements.txt
```
**4. Run the Flask application**
```bash
flask run
```
**5. Test the API**
Use curl, Postman, or your browser (for GET endpoints)

---

# Future Improvements
* User authentication
* Expense filtering by date or category
* Frontend interface for easier interaction
* Deployment to a cloud platform

---

## Author
Chow Yue Xuan

## Contact
Email: chowyuexuan@gmail.com
GitHub: https://github.com/potato-chowyuexuan
