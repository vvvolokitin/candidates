from flask import Flask

from utils import loading_candidates


app = Flask(__name__)


@app.route('/')
def page_main() -> str:
    """
    Возвращает главную страницу.

    Вывод на главную страницу иформацию о всех кандидатах.

    Возвращаемое значение:
            str_candidates (str): Информация о всех кандидатах.
    """
    candidates: list[dict] = loading_candidates()
    str_candidates: str = '<pre>'
    for candidate in candidates:
        str_candidates += (
            f'Имя: {candidate["name"]}\n'
            f'Позиция: {candidate["position"]}\n'
            f'Навыки: {candidate["skills"]}\n\n'
        )
    str_candidates += '</pre>'
    return str_candidates


if __name__ == '__main__':
    app.run()
