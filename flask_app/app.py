from flask import Flask
from flask_app.config import Configuration

application = Flask(__name__)
application.config.from_object(Configuration)