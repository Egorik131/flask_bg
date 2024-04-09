from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    copies = db.Column(db.Integer, nullable=False)
    id_author = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)

    def __repr__(self):
        return (f'Книга (Название: {self.title}, Год издания: {self.year}, Автор: {self.id_author})')


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(20), nullable=False)
    lastname = db.Column(db.String(30), nullable=False)
    book = db.relationship('Book', backref=db.backref('author'), lazy=True)

    def __repr__(self):
        return (f'Автор: {self.firstname} {self.lastname}')
