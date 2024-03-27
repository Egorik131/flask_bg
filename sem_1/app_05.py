"""
Написать функцию, которая будет выводить на экран HTML
страницу с заголовком "Моя первая HTML страница" и
абзацем "Привет, мир!".
"""

from flask import Flask

app = Flask(__name__)

html = """
<h1> Моя первая страница </h1>
<p> Привет, мир! <p/>
"""


@app.route('/')
def hello():
    return html

@app.route('/about/')
def about():
    return 'Меня зовут Егор!!!'

@app.route('/contact/')
def contact():
    return 'My phone number 333 22 111'

if __name__ == '__main__':
    app.run(debug=True)
