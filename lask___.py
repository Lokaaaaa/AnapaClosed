import os

import flask

os.system("pip install flask")
os.system("pip install Flask-RESTful")
os.system("pip install psycopg2-binary")

from flask import Flask, request
from flask_restful import Resource, Api
from flask import render_template, make_response
import sys
import sqlite3

app = Flask(__name__)
api = Api(app)
port = 5100

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
    return render_template('register.html')


@app.route("/register_get", methods=["POST", "GET"])
def register_get_data():
    a = request.form
    con = sqlite3.connect("data.db")
    cur = con.cursor()
    print(a)
    user_exists = cur.execute(f"""SELECT * from Users WHERE username="{a['username']}" """).fetchall()

    if len(a["password"]) >= 8 and a["username"] and not (user_exists):
        cur.execute(f"""INSERT INTO Users(username, password) VALUES ("{a['username']}", "{a['password']}")""")
        con.commit()

    return flask.redirect("/")


@app.route("/login", methods=["POST", "GET"])
def get_login_form_data():
    a = request.form
    print(a)
    con = sqlite3.connect("data.db")
    cur = con.cursor()
    user_exists = cur.execute(f"""SELECT * from Users WHERE username="{a['username']}" AND password="{a['password']}" """).fetchall()

    if user_exists:
        con.commit()
        print("юзер сущесвует ура")
        resp = make_response()
        resp.set_cookie('user', a["username"])
        resp.set_cookie('pass', a["password"])
        return resp

    return flask.redirect("/login")


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