from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_folder='../build', static_url_path='/')
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class NewsModel(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.Text(1000), nullable=False)
    url = db.Column(db.Text(1000), nullable=False)
    alt = db.Column(db.Text(10), nullable=False)
    context = db.Column(db.Text(5000), nullable=False)

    def __repr__(self):
        return f"News(title = {title}, url = {url})"


resource_fields = {
    'title': fields.String,
    'url': fields.String,
    'alt': fields.String,
    'context': fields.String,
}


class News(Resource):
    @marshal_with(resource_fields)
    def get(self):
        result = NewsModel.query.all()
        return result


api.add_resource(News, "/news")
