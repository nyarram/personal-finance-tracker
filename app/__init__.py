from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
import os

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    load_dotenv()

    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config["JWT_SECRET_KEY"] = os.getenv("SECRET_KEY")

    db.init_app(app)
    migrate.init_app(app, db)
    jwt = JWTManager(app)
    CORS(app)

    # Import models *after* db is initialized
    with app.app_context():
        from app.models.user import User
        from app.models.bank_account import BankAccount
        from app.models.transaction import Transaction
        from app.models.card_reward_rule import CardRewardRule

    # Register blueprints
    from app.routes.auth_routes import auth_bp
    from app.routes.account_routes import account_bp  # if added
    app.register_blueprint(auth_bp)
    app.register_blueprint(account_bp)

    from app.routes.test_routes import test_bp
    app.register_blueprint(test_bp)


    return app
