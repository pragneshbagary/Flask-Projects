from flask import Flask, request, jsonify, render_template, redirect
import requests
from models import db, User
from flask_sqlalchemy import SQLAlchemy
from services import user_service



app = Flask('__name')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db.init_app(app)

@app.route('/')
def index():
    return "Hello World Again!!!"

@app.route("/hello", methods=["GET"])
def hello():
    return jsonify(message="Hello from Flask!")


@app.route("/echo", methods=["POST", "GET"])
def echo():
    if request.method == "POST":
        data = request.get_json()
        return jsonify(received=data)
    else:
        return jsonify(message="Use POST to send JSON data")
    
@app.route("/external", methods=["GET"])
def external_call():
    response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
    data = response.json()
    return jsonify(data)


@app.route("/user", methods=['POST','GET'])
def user():
    if request.method == 'POST':
        name = request.form['user']
        new_user = User(userName=name)
        try:
            db.session.add(new_user)
            db.session.commit()
            print("✅ User added to DB:", name)
            return render_template('index.html', greeting=name)
        except Exception as e:
            return f"Cannot add user: {e}"
    else:
        return render_template('index.html', greeting = "looser")
    


@app.route("/create_user", methods=["POST"])
def create():
    name = request.json["name"]
    user = user_service.create_user(name)
    return jsonify(id=user.id, name=user.userName)


if __name__ == "__main__":
    app.run(port=8000,debug=True)

