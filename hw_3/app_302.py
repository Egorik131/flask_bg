'''Задание №2
Создать базу данных для хранения информации о книгах в библиотеке.
База данных должна содержать две таблицы: "Книги" и "Авторы".
В таблице "Книги" должны быть следующие поля: id, название, год издания,
количество экземпляров и id автора.
В таблице "Авторы" должны быть следующие поля: id, имя и фамилия.
Необходимо создать связь между таблицами "Книги" и "Авторы".
Написать функцию-обработчик, которая будет выводить список всех книг с
указанием их авторов.'''

from flask import Flask, render_template
from .models_302 import db, Book, Author

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase_302.db'
db.init_app(app)


@app.route('/')
def index():
    return "Добро пожаловать в библиотеку"


@app.cli.command("init-db")
def init_db():
    db.create_all()


@app.cli.command("fill-db")
def fill_tables():
    for author in range(5, 10):
        new_author = Author(firstname=f'Имя автора {author}', lastname=f'Фамилия автора {author}')
        db.session.add(new_author)
    db.session.commit()

    for book in range(1, 4):
        for i in range(1, 5):
            new_book = Book(title=f'Название {book}', year=2000 + book,
                            copies=book * 100, id_author=i)
            db.session.add(new_book)
    db.session.commit()


@app.route('/books/')
def get_books():
    books = Book.query.all()
    context = {'books': books}
    return render_template('books_info.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
