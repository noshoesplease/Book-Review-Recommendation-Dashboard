import logging
from logging.handlers import SMTPHandler, RotatingFileHandler
import os
from flask import Flask, request, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config


db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=Config):
    
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        # Flask Routes
        from app.main import bp as main_bp
        app.register_blueprint(main_bp)
        from app.dashboard import bp as dashboard_bp
        app.register_blueprint(dashboard_bp)
        from app.report import bp as report_bp
        app.register_blueprint(report_bp)
        from app.rec_sys import bp as rec_sys_bp
        app.register_blueprint(rec_sys_bp)

        return app