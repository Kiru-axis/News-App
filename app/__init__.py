from flask import Flask
from app.config import DevConfig

# Initializing application
app = Flask(__name__)

# setting up configuration
app.config.from_object(DevConfig)
# connect the app with the config holding the api_key
app.config.from_pyfile("config.py")

from app import views
