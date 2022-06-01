#import flask - from the package import class
from flask import Flask 
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db=SQLAlchemy()
login_manager = LoginManager()

#create a function that creates a web application
# a web server will run this web application
def create_app():
  
    app=Flask(__name__ , instance_relative_config=False)  # this is the name of the module/package that is calling this app
    app.config.from_object('config.Config')

    # Initialize the plugins
    db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        from . import routes
        from . import auth
        # from static.assets import compile_assets

     # Register Blueprints
        app.register_blueprint(routes.main_bp)
        app.register_blueprint(auth.auth_bp)

        # Create Database Models
        db.create_all()

        # Compile static assets
        # if app.config['FLASK_ENV'] == 'development':
        #     compile_assets(app)

        return app



