from flask import Flask
from flask_mongoengine import MongoEngine
from flask_sqlalchemy import SQLAlchemy
from redis import Redis


app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/my_catalog"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mysql@localhost:3306/class'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.debug = True

db1 = MongoEngine()
db2 = SQLAlchemy()


# def create_app():
#     app = Flask(__name__)
#     db1.init_app(app)
#     return app


redis = Redis()

from my_app.catalog.views import catalog
app.register_blueprint(catalog)