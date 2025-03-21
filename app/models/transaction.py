# app/models/transaction.py

from app import db
from datetime import datetime

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.Integer, db.ForeignKey("bank_account.id"), nullable=False)
    name = db.Column(db.String(200))  # Description (e.g., "Walmart")
    amount = db.Column(db.Float)
    category = db.Column(db.String(100))  # auto-tagged later
    date = db.Column(db.Date)
    type = db.Column(db.String(20))  # 'credit' or 'debit'
    pending = db.Column(db.Boolean, default=False)
    reward_earned = db.Column(db.Float, default=0.0)

    account = db.relationship("BankAccount", backref="transactions")
