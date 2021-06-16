from flask import Flask, render_template
from data import Users


Users = Users()
app = Flask(__name__)

@app.route('/')
def index():
    # return 'INDEX2'
    return render_template('index.html')

@app.route('/users')
def users():
    return render_template('users.html', users = Users)

@app.route('/user/<int:id>/')
def user(id):
    for user in Users:
        if user['id'] == id:
            _user = user
    return render_template('user.html', user = _user)

if __name__ == '__main__':
    app.run(debug=True)
