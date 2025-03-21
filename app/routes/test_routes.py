from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from app.models.bank_account import BankAccount
from app.models.transaction import Transaction
from app.models.card_reward_rule import CardRewardRule
from datetime import date

test_bp = Blueprint("test_bp", __name__)

@test_bp.route("/seed", methods=["POST"])
@jwt_required()
def seed_data():
    user_id = int(get_jwt_identity())
    from app.models.user import User
    user = User.query.get(user_id)

    if not user:
        return jsonify({"message": "User not found"}), 404

    # Create Bank Accounts
    bank1 = BankAccount(
        user_id=user.id,
        name="Capital One Venture X",
        account_type="credit",
        institution="Capital One",
        plaid_account_id="plaid_acc_venturex",
        balance=5000.00
    )
    bank2 = BankAccount(
        user_id=user.id,
        name="Citi Custom Cash",
        account_type="credit",
        institution="Citi Bank",
        plaid_account_id="plaid_acc_citi",
        balance=3000.00
    )
    bank3 = BankAccount(
        user_id=user.id,
        name="US Bank Checking",
        account_type="checking",
        institution="US Bank",
        plaid_account_id="plaid_acc_usbank",
        balance=2500.00
    )

    db.session.add_all([bank1, bank2, bank3])
    db.session.commit()

    # Create Transactions
    tx1 = Transaction(
        account_id=bank1.id,
        name="Hotel Booking",
        amount=-300.00,
        category="Travel",
        date=date.today(),
        type="debit",
        pending=False,
        reward_earned=3000  # example: 10x
    )
    tx2 = Transaction(
        account_id=bank2.id,
        name="Grocery Store",
        amount=-50.00,
        category="Groceries",
        date=date.today(),
        type="debit",
        pending=False,
        reward_earned=250  # example: 5x
    )
    tx3 = Transaction(
        account_id=bank3.id,
        name="Direct Deposit",
        amount=1000.00,
        category="Income",
        date=date.today(),
        type="credit",
        pending=False
    )

    db.session.add_all([tx1, tx2, tx3])
    db.session.commit()

    return jsonify({"message": "Seeded successfully"}), 201
