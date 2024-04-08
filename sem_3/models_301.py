from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(20), nullable=False)
    lastname = db.Column(db.String(20), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    group = db.Column(db.String(10), nullable=False)
    id_faculty = db.Column(db.Integer, db.ForeignKey('faculty.id'), nullable=False)

    def __repr__(self):
        return f'Студент (Имя: {self.firstname}, Фамилия: {self.lastname}, Факультет: {self.faculty})'

class Faculty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    student = db.relationship('Student', backref=db.backref('faculty'), lazy=True)

    def __repr__(self):
        return f'Факультет: {self.name}'
