from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db=SQLAlchemy()
DB_NAME= "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY']='kingkong'
    app.config['SQLALCHEMY_DATABASE_URI']= f'sqlite:///{DB_NAME}' 
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note

    create_database(app)
 
    return app

import logging

def create_database(app):
    if not path.exists ('website/'+DB_NAME):
        try:
            with app.app_context():
                db.create_all()
            print('Created Database')

        except Exception as e:
                    print(f"Error creating database: {str(e)}")
                    logging.exception("Error creating database:")
        else:
                print('Database already exists')
