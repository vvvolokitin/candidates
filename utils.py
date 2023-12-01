import json


def loading_candidates() -> list:
    """
    Возвращает список кандидатов с их характерситиками.

    Возвращаемое значение:
            list[dict]: Информация о кандидатах.
    """

    with open('candidates.json', 'r', encoding='utf-8') as file:
        return json.load(file)
