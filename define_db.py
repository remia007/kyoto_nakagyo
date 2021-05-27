from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# Unicodeエスケープの設定
app.config['JSON_AS_ASCII'] = False
db = SQLAlchemy(app)

class Kyoto_nakagyo_m(db.Model):

    __tablename__ = 'kyoto_nakagyo_ward'

    id = db.Column(db.Integer, primary_key=True)
    prefectures = db.Column(db.String)
    city = db.Column(db.String)
    ward = db.Column(db.String)
    town = db.Column(db.String)
    polygon = db.Column(db.String)

    def __init__(self, id, prefectures, city, ward, town, polygon):
        self.id = id
        self.prefectures = prefectures
        self.city = city
        self.ward = ward
        self.town = town
        self.polygon = polygon