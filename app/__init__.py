from flask import Flask
from app.config import DevConfig
from flask_bootstrap import Bootstrap

# initializing the application
# instance_relative_config allows us to connect with the instance folder holding the api_key
app = Flask(__name__,instance_relative_config=True)


# setting up configuration
app.config.from_object(DevConfig)
# connect the app with the config holding the api_key
app.config.from_pyfile("config.py")

# initialising Flask Extensions
# We then initialize the Bootstrap class by passing in the app instance. This is how most extensions are initialized. We can now use bootstrap in our application.
bootstrap = Bootstrap(app)

from app import views
from app import error