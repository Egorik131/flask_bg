'''Задание №6
Создать страницу, на которой будет форма для ввода имени
и возраста пользователя и кнопка "Отправить"
При нажатии на кнопку будет произведена проверка
возраста и переход на страницу с результатом или на
страницу с ошибкой в случае некорректного возраста.
'''

from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def check_user():
    if request.method == 'POST':
        name = request.form.get('name')
        age = int(request.form.get('age'))
        if 0 < age < 120:
            return render_template('main.html')
        else:
            return render_template('404.html')
    return render_template('form_login_t6.html')


if __name__ == '__main__':
    app.run(debug=True)