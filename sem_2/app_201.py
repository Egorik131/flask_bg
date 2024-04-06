'''
Задание №1
Создать страницу, на которой будет кнопка "Нажми меня", при
нажатии на которую будет переход на другую страницу с
приветствием пользователя по имени.
'''


from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.get('/')
def index_get():
    return render_template('app_201_index.html')
@app.post('/')
def index_post():
    name = request.form.get('name')
    return name



if __name__ == '__main__':
    app.run(debug=True)