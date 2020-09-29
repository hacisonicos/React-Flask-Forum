from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
# from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__, static_folder='../build', static_url_path='/')
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# For exisiting tables
# Base = declarative_base()
# Base.metadata.reflect(db.engine)


# class NewsModel(Base):
#    __table__ = Base.metadata.tables['users']
class News(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(1000))
    description = db.Column(db.String(10000))
    text = db.Column(db.String(10000))
    image_url = db.Column(db.String(200))
    date = db.Column(db.DateTime())
    url = db.Column(db.String(200))

    def __repr__(self):
        return "test"


resource_fields = {
    'title': fields.String,
    'description': fields.String,
    'text': fields.String,
    'image_url': fields.String,
    'date': fields.String,
    'url': fields.String,
}


class News(Resource):
    @marshal_with(resource_fields)
    def get(self):
        result = pd.read_sql_table(
            'users', db.engine).head(10).to_dict('records')
        return result


api.add_resource(News, "/news")
