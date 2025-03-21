from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.bank_account import BankAccount
from app.models.transaction import Transaction

account_bp = Blueprint("account_bp", __name__)

@account_bp.route("/accounts", methods=["GET"])
@jwt_required()
def get_accounts():
    user_id = int(get_jwt_identity())
    accounts = BankAccount.query.filter_by(user_id=user_id).all()
    return jsonify([{
        "name": a.name,
        "type": a.account_type,
        "institution": a.institution,
        "balance": a.balance
    } for a in accounts])

@account_bp.route("/transactions", methods=["GET"])
@jwt_required()
def get_transactions():
    user_id = int(get_jwt_identity())
    accounts = BankAccount.query.filter_by(user_id=user_id).all()
    account_ids = [a.id for a in accounts]
    transactions = Transaction.query.filter(Transaction.account_id.in_(account_ids)).all()
    return jsonify([
        {
            "name": t.name,
            "amount": t.amount,
            "category": t.category,
            "date": str(t.date),
            "account_id": t.account_id,
            "reward_earned": t.reward_earned
        } for t in transactions
    ])

