'''Задание №3
Создать страницу, на которой будет форма для ввода логина и пароля

При нажатии на кнопку "Отправить" будет произведена
проверка соответствия логина и пароля и переход на
страницу приветствия пользователя или страницу с ошибкой.'''

from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        if request.form.get('login') == 'Egorik' and request.form.get('password') == '123':
          return render_template('main.html')
        else:
            return render_template('404.html')
    return render_template('form_login_pass.html')


if __name__ == '__main__':
    app.run(debug=True)