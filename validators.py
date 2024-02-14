from datetime import datetime


# Пример функции для владиации данных
# Каждую функцию пишем в виде validate_{что валидируем}
def validate_time_string(time_string: str) -> bool:
    """
    :param time_string: Строка, представляющее время, полученная из поля воода streamlit
    :return: True, если строка в верном формате, иначе - False
    """
    try:
        datetime.strptime(time_string, "%Y-%m-%dT%H:%M:%SZ")
        return True
    except ValueError:
        return False
