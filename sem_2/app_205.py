'''Задание №5
Создать страницу, на которой будет форма для ввода двух
чисел и выбор операции (сложение, вычитание, умножение
или деление) и кнопка "Вычислить"
При нажатии на кнопку будет произведено вычисление
результата выбранной операции и переход на страницу с
результатом.'''


from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def check_name():
    if request.method == 'POST':
        first_number = int(request.form.get('first_number'))
        second_number = int(request.form.get('second_number'))
        operation = request.form.get('operation')
        if operation == '+':
            res = first_number + second_number
        elif operation == '-':
            res = first_number - second_number
        elif operation == '/':
            res = first_number / second_number
        elif operation == '*':
            res = first_number * second_number
        else:
            res = "оператора не существует"
        return str(res)
    return render_template('form_calc.html')


if __name__ == '__main__':
    app.run(debug=True)
