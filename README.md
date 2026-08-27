💰 Expense Dashboard

A backend-focused expense management project built with Python and FastAPI. The project is designed to provide REST APIs for managing expenses and will later include an interactive dashboard for expense analysis and visualization.

🚀 Project Overview

The Expense Dashboard helps users manage and analyze their daily expenses.

The project is being developed step by step using:

* Python
* FastAPI
* SQLAlchemy
* SQLite
* REST APIs
* Streamlit (planned for the dashboard)

🛠️ Tech Stack

Technology	Purpose
Python	Backend programming
FastAPI	REST API development
SQLAlchemy	Database ORM
SQLite	Database
Uvicorn	Development server
Streamlit	Dashboard (planned)
Git & GitHub	Version control

📁 Project Structure

expense-dashboard/
│
├── backend/
│   ├── app/
│   │   ├── database.py
│   │   └── models.py
│   │
│   └── main.py
│
├── venv/
│
├── .gitignore
├── requirements.txt
└── README.md

✅ Current Features

* FastAPI application setup
* Health check API
* SQLite database connection
* SQLAlchemy configuration
* Expense database model
* Automatic database table creation
* GitHub version control

🔗 Current API Endpoints

Home

GET /

Returns a message confirming that the Expense Dashboard API is running.

Health Check

GET /health

Returns the current health status of the API.

🗄️ Database

The project currently uses SQLite with SQLAlchemy.

Expense Model

The expenses table contains:

* id — Unique expense ID
* title — Expense title
* amount — Expense amount
* category — Expense category

The local SQLite database file is ignored by Git using .gitignore.

▶️ How to Run the Project

1. Clone the repository

git clone https://github.com/Shifana14-d/expense-dashboard.git

2. Open the project

cd expense-dashboard

3. Create a virtual environment

py -3.12 -m venv venv

4. Activate the virtual environment

On Windows PowerShell:

.\venv\Scripts\Activate.ps1

5. Install dependencies

pip install -r requirements.txt

6. Start the FastAPI server

uvicorn backend.main:app --reload

The API will be available at:

http://127.0.0.1:8000

📚 API Documentation

FastAPI automatically provides interactive API documentation.

Open:

http://127.0.0.1:8000/docs

You can use Swagger UI to test the available endpoints.

🔮 Future Improvements

The project will be expanded with:

* Expense CRUD APIs
* PostgreSQL database support
* User authentication
* Expense filtering
* Monthly expense analytics
* Category-based analysis
* Interactive Streamlit dashboard
* Charts and visualizations
* API testing
* Docker support
* Deployment

🎯 Learning Goals

This project is being developed to strengthen practical knowledge of:

* Python backend development
* REST API development
* FastAPI
* Database management
* SQLAlchemy
* API architecture
* Git and GitHub
* Data visualization
* Backend-to-dashboard integration

👩‍💻 Author

Shifana Parveen

GitHub: Shifana14-d