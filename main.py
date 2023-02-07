from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# creating our database object! This allows us to use our ORM
db = SQLAlchemy()

def create_app():
    # using a list comprehension and multiple assignment 
    # to grab the environment variables we need
    
    # Creating the flask app object - this is the core of our app!
    app = Flask(__name__)

    # configuring our app:
    app.config.from_object("config.app_config")

    # creating our database object! this allows us to use our ORM
    db.init_app(app)

    # import the controllers and activate the blueprints
    from controllers import registerable_controllers

    for controller in registerable_controllers:
        app.register_blueprint(controller)
    
    return app
