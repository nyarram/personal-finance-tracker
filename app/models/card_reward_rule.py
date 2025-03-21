# app/models/card_reward_rule.py

from app import db

class CardRewardRule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.Integer, db.ForeignKey("bank_account.id"), nullable=False)
    category = db.Column(db.String(100))  # 'Groceries', 'Dining', etc.
    reward_rate = db.Column(db.Float)     # e.g., 1.5 for 1.5%

    account = db.relationship("BankAccount", backref="reward_rules")
