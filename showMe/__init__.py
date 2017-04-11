import os

import settings
from flask import Flask

from showMe.controllers.sql_alchemy.flask_sqlalchemy import SQLAlchemy

__author__ = "Evert Arends"

app = Flask(import_name=__name__,
            static_folder=None,
            template_folder='views')

app.config['SECRET_KEY'] = settings.app_secret
app.config['dir_base'] = os.path.dirname(os.path.abspath(__file__))
app.config['dir_root'] = '/'.join(app.config['dir_base'].split('/')[:-1])
app.config['APPLICATION_ROOT'] = settings.BIND_ROUTE
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/ardjan/Documents/projects/showMe/showMe/logs.db'
db = SQLAlchemy(app)

SECRET_KEY = settings.app_secret

# init routes
import showMe.routes