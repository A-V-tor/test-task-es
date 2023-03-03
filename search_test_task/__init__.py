from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_apispec.extension import FlaskApiSpec
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec import APISpec


app = Flask(__name__, instance_relative_config=False)

app.config.from_object('config.Config')

db = SQLAlchemy(app)
docs = FlaskApiSpec(app)

app.config.update(
    {
        'APISPEC_SPEC': APISpec(
            title='best cars',
            version='v1',
            openapi_version='2.0',
            plugins=[MarshmallowPlugin()],
        )
    }
)

with app.app_context():
    from .routes import *

    db.create_all()
