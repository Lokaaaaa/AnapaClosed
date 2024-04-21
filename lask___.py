import os
os.system("pip install flask")
os.system("pip install Flask-RESTful")
os.system("pip install psycopg2-binary")
os.system("pip install flask flask-sqlalchemy flask-login")
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user, login_required
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api
from flask import render_template, make_response
import sys
import sqlite3
import flask
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
app.config["SECRET_KEY"] = "abc"
db = SQLAlchemy()

login_manager = LoginManager()
login_manager.init_app(app)

class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    purchase = db.Column(db.Float, default=0)
    squares = db.Column(db.Float, default=0)

db.init_app(app)

with app.app_context():
	db.create_all()

@app.route("/index")
def index():
    return render_template('index.html')

@login_manager.user_loader
def loader_user(user_id):
	return Users.query.get(user_id)
api = Api(app)
port = 5000

if sys.argv.__len__() > 1:
    port = sys.argv[1]
print("Api running on port : {} ".format(port))

@app.route("/")
def tour___():
    return render_template('index.html')

@app.route("/register", methods=["POST", "GET"])
def register():
    try:
        if request.method == "POST":
            user = Users(username=request.form.get("username"), password=request.form.get("password"))
            db.session.add(user)
            db.session.commit()
            return flask.redirect(flask.url_for("login"))
        return render_template("sign_up.html")
    except Exception as e:
        print(f'ОШИБКА: {e}')
        return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    try:
        if request.method == "POST":
            user = Users.query.filter_by(
                username=request.form.get("username")).first()
            if user.password == request.form.get("password"):
                login_user(user)
            return flask.redirect(flask.url_for("home"))
        return render_template("login.html")
    except Exception as e:
        print(f'ОШИБКА: {e}')
        return render_template('index.html')

@app.route("/logout")
@login_required
def logout():
	logout_user()
	return flask.redirect(flask.url_for("home"))

@app.route("/")
def home():
	return render_template("index.html")

@app.route("/booking", methods=["POST", "GET"])
@login_required
def booking():
    try:
        purchase = 0
        squares = current_user.squares
        if request.method == "POST":
            method = request.form.get("PAY")
            purchase += float(request.form.get("purchase"))
            if method == "ОПЛАТИТЬ КУБАМИ":
                if purchase > squares:
                    return render_template('booking.html', mistake="ошибка", need=abs(squares-purchase))
                else:
                    squares -= purchase
                    user = current_user
                    user.squares = squares
                    user.purchase = purchase
                    db.session.commit()
            else:
                purchase += float(request.form.get("purchase"))
                squares += 0 if purchase < 23000 else (purchase * 0.02) if 23000 <= purchase < 32000 else (purchase * 0.03) if 32000 <= purchase < 45000 else (purchase * 0.04) if 45000 <= purchase < 58000 else (purchase * 0.05) if 58000 <= purchase < 72000 else (purchase * 0.06)
                user = current_user
                user.purchase = purchase
                user.squares = squares
                db.session.commit()
            
            return flask.redirect(flask.url_for("home"))
        return render_template('booking.html', mistake="", need=0)
    except Exception as e:
        print(f'ОШИБКА: {e}')
        return render_template('index.html')

@app.route("/tours", methods=["POST", "GET"])
@login_required
def tours():
    try:
        purchase = 0
        squares = current_user.squares
        if request.method == "POST":
            method = request.form.get("PAY")
            purchase += float(request.form.get("purchase"))
            if method == "ОПЛАТИТЬ КУБАМИ":
                if purchase > squares:
                    return render_template('tours.html', mistake="ошибка", need=abs(squares-purchase))
                else:
                    squares -= purchase
                    user = current_user
                    user.squares = squares
                    user.purchase = purchase
                    db.session.commit()
            else:
                purchase += float(request.form.get("purchase"))
                squares += 0 if purchase < 23000 else (purchase * 0.02) if 23000 <= purchase < 32000 else (purchase * 0.03) if 32000 <= purchase < 45000 else (purchase * 0.04) if 45000 <= purchase < 58000 else (purchase * 0.05) if 58000 <= purchase < 72000 else (purchase * 0.06)
                user = current_user
                user.purchase = purchase
                user.squares = squares
                db.session.commit()
            
        return render_template('tours.html', mistake="", need=0)
    except Exception as e:
        print(f'ОШИБКА: {e}')
        return render_template('index.html')

@app.route("/places", methods=["POST", "GET"])
@login_required
def places():
    try:
        purchase = 0
        squares = current_user.squares
        if request.method == "POST":
            method = request.form.get("PAY")
            purchase += float(request.form.get("purchase"))
            if method == "ОПЛАТИТЬ КУБАМИ":
                if purchase > squares:
                    return render_template('places.html', mistake="ошибка", need=abs(squares-purchase))
                else:
                    squares -= purchase
                    user = current_user
                    user.squares = squares
                    user.purchase = purchase
                    db.session.commit()
            else:
                purchase += float(request.form.get("purchase"))
                squares += 0 if purchase < 23000 else (purchase * 0.02) if 23000 <= purchase < 32000 else (purchase * 0.03) if 32000 <= purchase < 45000 else (purchase * 0.04) if 45000 <= purchase < 58000 else (purchase * 0.05) if 58000 <= purchase < 72000 else (purchase * 0.06)
                user = current_user
                user.purchase = purchase
                user.squares = squares
                db.session.commit()
            
        return render_template('places.html', mistake="", need=0)
    except Exception as e:
        print(f'ОШИБКА: {e}')
        return render_template('index.html')

@app.route("/enterteinments", methods=["POST", "GET"])
@login_required
def enterteinments():
    try:
        purchase = 0
        squares = current_user.squares
        if request.method == "POST":
            method = request.form.get("PAY")
            purchase += float(request.form.get("purchase"))
            if method == "ОПЛАТИТЬ КУБАМИ":
                if purchase > squares:
                    return render_template('enterteinments.html', mistake="ошибка", need=abs(squares-purchase))
                else:
                    squares -= purchase
                    user = current_user
                    user.squares = squares
                    user.purchase = purchase
                    db.session.commit()
            else:
                purchase += float(request.form.get("purchase"))
                squares += 0 if purchase < 23000 else (purchase * 0.02) if 23000 <= purchase < 32000 else (purchase * 0.03) if 32000 <= purchase < 45000 else (purchase * 0.04) if 45000 <= purchase < 58000 else (purchase * 0.05) if 58000 <= purchase < 72000 else (purchase * 0.06)
                user = current_user
                user.purchase = purchase
                user.squares = squares
                db.session.commit()
            
        return render_template('enterteinments.html', mistake="", need=0)
    except Exception as e:
        print(f'ОШИБКА: {e}')
        return render_template('index.html')

@app.route("/beaches", methods=["POST", "GET"])
@login_required
def beaches():
    try:
        purchase = 0
        squares = current_user.squares
        if request.method == "POST":
            method = request.form.get("PAY")
            purchase += float(request.form.get("purchase"))
            if method == "ОПЛАТИТЬ КУБАМИ":
                if purchase > squares:
                    return render_template('beaches.html', mistake="ошибка", need=abs(squares-purchase))
                else:
                    squares -= purchase
                    user = current_user
                    user.squares = squares
                    user.purchase = purchase
                    db.session.commit()
            else:
                purchase += float(request.form.get("purchase"))
                squares += 0 if purchase < 23000 else (purchase * 0.02) if 23000 <= purchase < 32000 else (purchase * 0.03) if 32000 <= purchase < 45000 else (purchase * 0.04) if 45000 <= purchase < 58000 else (purchase * 0.05) if 58000 <= purchase < 72000 else (purchase * 0.06)
                user = current_user
                user.purchase = purchase
                user.squares = squares
                db.session.commit()
            
        return render_template('beaches.html', mistake="", need=0)
    except Exception as e:
        print(f'ОШИБКА: {e}')
        return render_template('index.html')

@app.route("/cafe", methods=["POST", "GET"])
@login_required
def cafe():
    try:
        purchase = 0
        squares = current_user.squares
        if request.method == "POST":
            method = request.form.get("PAY")
            purchase += float(request.form.get("purchase"))
            if method == "ОПЛАТИТЬ КУБАМИ":
                if purchase > squares:
                    return render_template('cafe.html', mistake="ошибка", need=abs(squares-purchase))
                else:
                    squares -= purchase
                    user = current_user
                    user.squares = squares
                    user.purchase = purchase
                    db.session.commit()
            else:
                purchase += float(request.form.get("purchase"))
                squares += 0 if purchase < 23000 else (purchase * 0.02) if 23000 <= purchase < 32000 else (purchase * 0.03) if 32000 <= purchase < 45000 else (purchase * 0.04) if 45000 <= purchase < 58000 else (purchase * 0.05) if 58000 <= purchase < 72000 else (purchase * 0.06)
                user = current_user
                user.purchase = purchase
                user.squares = squares
                db.session.commit()
            
        return render_template('cafe.html', mistake="", need=0)
    except Exception as e:
        print(f'ОШИБКА: {e}')
        return render_template('index.html')


@app.route("/profile", methods=["POST", "GET"])
@login_required
def profile():
    return render_template('profile.html',username=current_user.username, squares=current_user.squares)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=port)