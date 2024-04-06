'''
Задание №8
Создать страницу, на которой будет форма для ввода имени
и кнопка "Отправить"
При нажатии на кнопку будет произведено
перенаправление на страницу с flash сообщением, где будет
выведено "Привет, {имя}!".
'''

from flask import Flask, request, render_template, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = '123456789'


@app.route('/', methods=['GET', 'POST'])
def check_user():
    if request.method == 'POST':
        name = request.form.get('name')
        flash(f'Привет, {name}', 'success')
        return redirect(url_for('check_user'))
    return render_template('form_flash.html')


if __name__ == '__main__':
    app.run(debug=True)
