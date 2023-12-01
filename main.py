import json

from flask import Flask


app = Flask(__name__)


@app.route('/')
def page_main():
    """
    Возвращает главную страницу.

    Возвращаемое значение:
            str: Информация о главной страницу.
    """
    return 'Главная страница'


if __name__ == '__main__':
    app.run()
