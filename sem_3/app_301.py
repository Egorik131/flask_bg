'''Задание №1
Создать базу данных для хранения информации о студентах университета.
База данных должна содержать две таблицы: "Студенты" и "Факультеты".
В таблице "Студенты" должны быть следующие поля: id, имя, фамилия,
возраст, пол, группа и id факультета.
В таблице "Факультеты" должны быть следующие поля: id и название факультета.
Необходимо создать связь между таблицами "Студенты" и "Факультеты".
Написать функцию-обработчик, которая будет выводить список всех
студентов с указанием их факультета.'''

from flask import Flask, render_template
from .models_301 import db, Student, Faculty

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase_301.db'
db.init_app(app)


@app.route('/')
def index():
    return "Hello"


@app.cli.command("init-db")
def init_db():
    db.create_all()


@app.cli.command("fill-db")
def fill_tables():
    for faculty in range(1, 4):
        new_faculty = Faculty(name=f'Факультет {faculty}')
        db.session.add(new_faculty)
    db.session.commit()

    for student in range(1, 11):
        for i in range(1, 4):
            new_student = Student(firstname=f'Имя студента {student}', lastname=f'Фамилия студента {student}',
                                  age=20 + student, gender='m', group=str(100 + student), id_faculty=i)
            db.session.add(new_student)
    db.session.commit()

@app.route('/students/')
def get_students():
    students = Student.query.all()
    context = {'students': students}
    return render_template('students.html', **context)



if __name__ == '__main__':
    app.run(debug=True)
