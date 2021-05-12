from app_module import app
from request import Request
from flask import render_template, request, Flask
import requests

count = 0

@app.route('/')
@app.route('/index')
def index():
    user = "Ученик Яндекс.Лицея"
    return render_template('title.html', title='Домашняя страница',
                           username=user)

@app.route("/with_template")
def with_template():
    global count
    count += 1
    user = {'username': 'Miguel'}
    return render_template('index.html', title='home', user=user, count=count)

@app.route("/weather")
def weather():
    try:
        req = Request()
        data = req.get_temp()
        return render_template('weather.html', title='home',
                               today = data[0],
                               tonight = data[1],
                               tomorrow_day = data[2],
                               tomorrow_night = data[3])

    except Exception as e:
        return "Exception (find):" + str(e)
