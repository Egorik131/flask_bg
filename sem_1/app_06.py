"""
Написать функцию, которая будет выводить на экран HTML
страницу с таблицей, содержащей информацию о студентах.
Таблица должна содержать следующие поля: "Имя",
"Фамилия", "Возраст", "Средний балл".
Данные о студентах должны быть переданы в шаблон через
контекст.
"""

from flask import Flask, render_template

app = Flask(__name__)


# html = """
# <h1> Моя первая страница </h1>
# <p> Привет, мир! <p/>
# """


@app.route('/')
def hello():
    return 'hi!'


@app.route('/students/')
def info_stud():
    students = [
        {
            'First_Name': 'Egor',
            'Last_Name': 'Mel',
            'Age': 44,
            'Avg_score': 4.5
        },
        {
            'First_Name': 'Egor1',
            'Last_Name': 'Mel1',
            'Age': 42,
            'Avg_score': 4.6
        },
        {
            'First_Name': 'Egor2',
            'Last_Name': 'Mel2',
            'Age': 41,
            'Avg_score': 4.7
        },
    ]
    context = {
        'stud': students
    }
    return render_template('index.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
