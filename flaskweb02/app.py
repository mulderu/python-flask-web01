from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os


app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)

# example model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(200))
    price = db.Column(db.Float)
    qty = db.Column(db.Integer)

    def __init__(self, name, description, price, qty):
        self.name = name
        self.description = description
        self.price = price
        self.qty = qty

# example model
class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'price', 'qty')

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

@app.route('/', methods=['GET'])
def index():
    # return render_template('index.html')
    return jsonify({'msg': 'helo index'})

'''
@app.route('/users')
def users():
    return render_template('users.html', users = Users)

@app.route('/user/<int:id>/')
def user(id):
    for user in Users:
        if user['id'] == id:
            _user = user
    return render_template('user.html', user = _user)
'''

if __name__ == '__main__':
    app.run(debug=True)
