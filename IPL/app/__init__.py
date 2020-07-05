import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.environ['SQLALCHEMY_DATABASE_URI'], 'challenge.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)

# ##########################
# ### LOGIN CONFIGS #######
# ########################
login_manager = LoginManager()

# We can now pass in our app to the login manager
login_manager.init_app(app)

# Tell users what view to go to when they need to login.
login_manager.login_view = "users.login"


# Register blueprints
from app.core.views import core
from app.users.views import users
from app.matches.views import matches

app.register_blueprint(users)
app.register_blueprint(core)
app.register_blueprint(matches)

