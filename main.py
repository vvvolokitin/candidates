from flask import Flask

app = Flask(__name__)


@app.route('/')
def page_main():
    """Возвращает главную страницу."""
    return 'Главная страница'


if __name__ == '__main__':
    app.run()
