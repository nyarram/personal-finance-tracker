# app/models/bank_account.py

from app import db

class BankAccount(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    name = db.Column(db.String(100))
    account_type = db.Column(db.String(50))  # 'credit', 'checking', etc.
    institution = db.Column(db.String(100))
    plaid_account_id = db.Column(db.String(100), unique=True)  # returned by Plaid
    balance = db.Column(db.Float, default=0.0)
    
    user = db.relationship("User", backref="bank_accounts")
