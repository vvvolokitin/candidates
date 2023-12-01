from flask import Flask

from utils import loading_candidates


app = Flask(__name__)

candidates: list[dict] = loading_candidates()

@app.route('/')
def page_main() -> str:
    """
    Возвращает главную страницу.

    Вывод на главную страницу иформацию о всех кандидатах.

    Возвращаемое значение:
            str_candidates (str): Информация о всех кандидатах.
    """
    str_candidates: str = '<pre>'
    for candidate in candidates:
        str_candidates += (
            f'Имя: {candidate["name"]}\n'
            f'Позиция: {candidate["position"]}\n'
            f'Навыки: {candidate["skills"]}\n\n'
        )
    str_candidates += '</pre>'
    return str_candidates


@app.route('/candidate/<int:candidate_id>')
def page_candidate(candidate_id: int) -> str:
    """
    Возвращает страницу кандидата.

    Вывод информации о кандидате по его id.

    Возвращаемое значение:
            result_candidate (str): Информация о кандидатe.
    """
    result_candidate: str = 'Кандидата с таким id нет'
    for candidate in candidates:
        if candidate['id'] == candidate_id:
            result_candidate = (
                f'<img src="{candidate["picture"]}"<br>'
                f'<pre><br>Имя: {candidate["name"]}'
                f'<br>Позиция: {candidate["position"]}'
                f'<br>Навыки: {candidate["skills"]}</pre>'
            )
    return result_candidate


@app.route('/skill/<skill>')
def page_skill(skill: str):
    """
    Возвращает страницу с кандидатами по навыкам.

    Вывод на страницу иформацию о всех кандидатах с указанными навыками.

    Возвращаемое значение:
            str_candidates (str): Информация о кандидатах.
    """
    str_candidates: str = '<pre>'
    for candidate in candidates:
        if skill in [sk.lower() for sk in candidate['skills'].split(', ')]:
            str_candidates += (
                f'Имя: {candidate["name"]}\n'
                f'Позиция: {candidate["position"]}\n'
                f'Навыки: {candidate["skills"]}\n\n'
            )
    str_candidates += '</pre>'
    return str_candidates


if __name__ == '__main__':
    app.run(debug=False, port=8000)
