'''
Задание №4
Создать страницу, на которой будет форма для ввода текста и кнопка "Отправить"
При нажатии кнопки будет произведен подсчет количества слов
в тексте и переход на страницу с результатом.
'''

from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def check_name():
    if request.method == 'POST':
        my_text = request.form.get('my_text')
        count = len(request.form.get('my_text').split())
        return f'{my_text} <br> текст из {count} слов(а)'
    return render_template('form_text.html')


if __name__ == '__main__':
    app.run(debug=True)