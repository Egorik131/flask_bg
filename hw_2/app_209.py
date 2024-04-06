'''  Задание №9
Создать страницу, на которой будет форма для ввода имени и электронной почты
При отправке которой будет создан cookie файл с данными пользователя
Также будет произведено перенаправление на страницу
приветствия, где будет отображаться имя пользователя.
На странице приветствия должна быть кнопка "Выйти"
При нажатии на кнопку будет удален cookie файл с данными
пользователя и произведено перенаправление на страницу
ввода имени и электронной почты.
'''

from flask import Flask, request, render_template, redirect, url_for, session

app = Flask(__name__)
app.secret_key = '123456789'


@app.route('/', methods=['GET', 'POST'])
def index():
    if 'name' in session:
        name = session["name"]
        return render_template('hello.html', name=name)
    else:
        return redirect('login')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['name'] = request.form.get('name') or 'NoName'
        return redirect(url_for('index'))
    return render_template('form_209.html')


@app.route('/logout/')
def logout():
    session.pop('name', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
