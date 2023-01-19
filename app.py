from flask import Flask, request, render_template, jsonify
from utils import *


app = Flask(__name__, template_folder='templates')


@app.route('/')
def show_data():
    """ вьюшка, где задается функция с загрузкой json файла"""
    days = load_data()
    return render_template('index.html', days=days)

@app.route('/monday')
def show_by_day():
    """ вьюшка, где задается функция с загрузкой json файла"""
    days = load_data_monday()
    return render_template('search.html', days=days)


@app.errorhandler(404)
""" обработчик ошибок"""
def error_404(e):
    return 'Такое не найдено', 404

@app.errorhandler(500)
""" обработчик ошибок"""
def error_500(e):
    return'Internal Server Error ', 500

@app.route('/api/post')
def api_posts():
    days = load_data()
    return jsonify(days)

@app.route('/api/post/<pk>')
def api_post(pk):
    day = load_data_monday()

    return jsonify(day)


if __name__ == '__main__':
    app.run()