'''Задание №7
Создать страницу, на которой будет форма для ввода числа
и кнопка "Отправить"
При нажатии на кнопку будет произведено
перенаправление на страницу с результатом, где будет
выведено введенное число и его квадрат.
'''

from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def square_num():
    if request.method == 'POST':
        number = int(request.form.get('number'))
        res = number * number
        return render_template('square_num.html', number=number, res=res)
        # return f'Число: {number}, квадрат числа: {res}'
    return render_template('form_207.html')


if __name__ == '__main__':
    app.run(debug=True)
