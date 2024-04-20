import os

import flask

os.system("pip install flask")
os.system("pip install Flask-RESTful")
os.system("pip install psycopg2-binary")
os.system("pip install flask flask-sqlalchemy flask-login")
from flask_login import LoginManager, UserMixin, login_user, logout_user
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api
from flask import render_template, make_response
import sys
import sqlite3

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


db.init_app(app)


with app.app_context():
	db.create_all()


@login_manager.user_loader
def loader_user(user_id):
	return Users.query.get(user_id)
api = Api(app)
port = 5000

if sys.argv.__len__() > 1:
    port = sys.argv[1]
print("Api running on port : {} ".format(port))


@app.route("/tour")
def index_():
    return "<h1>tourney</h1>"
"""1. Бронирование отелей 
2. Покупка туров, Пакетные туры 
3. Маркетплейс турпродуктов
4. Интересные места
5. Инфраструктура
6. Пешие маршруты
7. Пляжи
"""


@app.route("/booking")
def index______():
    return "Появилась бронирование"


@app.route("/beaches")
def tour_():
    return "<h1>Пляжи</h1>"


@app.route("/places")
def tour_3():
    return "<h1>Достопримечательности</h1>"


@app.route("/on-foot_routes")
def tour_2():
    return "<h1>Пешие маршруты</h1>"


@app.route("/")
def tour___():
    return render_template('index.html')


@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        user = Users(username=request.form.get("username"),
                     password=request.form.get("password"))
        db.session.add(user)
        db.session.commit()
        return flask.redirect(flask.url_for("login"))
    return render_template("sign_up.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = Users.query.filter_by(
			username=request.form.get("username")).first()
        if user.password == request.form.get("password"):
            login_user(user)
        return flask.redirect(flask.url_for("home"))
    return render_template("login.html")


@app.route("/logout")
def logout():
	logout_user()
	return flask.redirect(flask.url_for("home"))


@app.route("/")
def home():
	return render_template("index.html")


class Customer:
    def __init__(self, name, loyalty_level=1, bonus_points=0):
        self.name = name
        self.loyalty_level = loyalty_level
        self.bonus_points = bonus_points

    def calculate_bonus_points(self, amount_spent):
        # Рассчитываем бонусные баллы в зависимости от уровня лояльности
        if self.loyalty_level <= 1:
            bonus_rate = 0.1
        elif self.loyalty_level == 2:
            bonus_rate = 0.15
        else:
            bonus_rate = 0.2

        bonus_points = amount_spent * bonus_rate
        self.bonus_points += bonus_points
        return bonus_points

    def spend_bonus_points(self, points_spent):
        if points_spent <= self.bonus_points:
            self.bonus_points -= points_spent
            return True
        else:
            return False

# Создаем экземпляр клиента
customer1 = Customer("Alice")

# Совершаем покупки (поход в кино)
amount_spent = 50
customer1.calculate_bonus_points(amount_spent)

# Бронируем отель
hotel_booking_cost = 200
customer1.calculate_bonus_points(hotel_booking_cost)

# Проверяем баланс бонусных баллов
print(f"{customer1.name} имеет {customer1.bonus_points} бонусных баллов.")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=port)