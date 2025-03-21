# Personal Finance Tracker (Flask Backend)

This is a backend API for a personal finance tracking application. It supports user authentication, linking bank accounts, tracking transactions, and calculating credit card rewards. It is built using Python, Flask, SQLAlchemy, and integrates with the Plaid API (coming soon).

## Features

- User signup and login with JWT authentication
- Link multiple bank accounts (checking, savings, credit)
- Track transactions per account
- Auto-categorize transactions
- Store and calculate rewards per credit card
- API-ready for Plaid sandbox integration

## Tech Stack

- Python 3.9+
- Flask
- Flask-JWT-Extended
- SQLAlchemy
- SQLite (default, can switch to PostgreSQL)
- Flask-Migrate
- Plaid API (to be integrated)

## Setup

1. Clone the repo:
git clone https://github.com/your-username/personal-finance-tracker.git 
cd personal-finance-tracker

2. Set up virtual environment:
python3 -m venv venv 
source venv/bin/activate

3. Install dependencies:
pip install -r requirements.txt

4. Create a `.env` file:
FLASK_ENV=development 
SECRET_KEY=your-secret-key 
DATABASE_URL=sqlite:///dev.db

5. Run database migrations:
flask db upgrade

6. Start the server:
flask run


## API Endpoints

### Auth
- `POST /signup` – Create a new user
- `POST /login` – Get JWT token
- `GET /me` – Get logged-in user info (requires token)

### Test/Seed
- `POST /seed` – Add dummy accounts and transactions (requires token)

### Accounts
- `GET /accounts` – Get all linked accounts (requires token)

### Transactions
- `GET /transactions` – Get all transactions for user (requires token)

## Coming Soon

- Plaid integration (link real bank accounts)
- Rewards summary endpoint
- Frontend UI (React)