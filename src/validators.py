import re
import streamlit as st


def validate_wrapper(validation: tuple[bool, str]) -> None:
    """Принимает результаты валидации и в случае, если валидация не пройдена, выводит соотвествующую ошибку"""
    if not validation[0]:
        st.warning(validation[1])


def validate_inn(inn: str) -> tuple[bool, str]:
    if len(inn) != 10:
        return False, 'Длина не равна 10 символам'
    if not inn.isdigit():
        return False, 'ИНН должен содержать только цифры'
    if inn[:2] == '00':
        return False, 'Первые две цифры не могут одновременно быть нулём'
    return True, '1'


def validate_kpp(kpp: str) -> tuple[bool, str]:
    if len(kpp) != 9:
        return False, 'Длина КПП должна быть 9 символов.'
    if re.match(r'^.{4}[^A-Z0-9].*$', kpp):
        return False, 'В 5-ом разряде недопустимый символ. Разрешены только 0-9 и A-Z'
    if re.match(r'^.{5}[^A-Z0-9].*$', kpp):
        return False, 'В 6-ом разряде недопустимый символ. Разрешены только 0-9 и A-Z'

    if re.match(r'^(?:.{0,3}|.{6,})[^0-9].*$', kpp):
        return False, 'В разрядах 1-4 и 6-9 разрешены только 0-9'

    return True, '1'


def validate_igk(igk: str) -> tuple[bool, str]:
    """
    https://base.garant.ru/71169728/53f89421bbdaf741eb2d1ecc4ddb4c33/#block_1000
    :param igk:
    :return:
    """
    # Проверка длины ИГк
    if len(igk) != 25:
        return False, 'Неверная длина: должно быть 25 символов.'

    # Проверка на цифровые символы
    if not igk.isdigit():
        return False, 'Идентификатор должен содержать только цифры.'

    # Проверка информации о закупке (8 разряд)
    purchase_info = int(igk[7])
    if purchase_info < 1 or purchase_info > 9:
        return False, 'Неверное значение информации о закупке в 8 разряде.'

    # Проверка вида цены (13 разряд)
    price_type = int(igk[12])
    if price_type < 1 or price_type > 3:
        return False, 'Неверное значение вида цены в 13 разряде.'

    # Если все проверки пройдены
    return True, '1'


def validate_date(date_str: str) -> tuple[bool, str]:
    # Паттерн для проверки строки даты
    pattern = r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(Z|[+-]\d{2}:\d{2})$'

    # Проверяем, соответствует ли входная строка паттерну
    if re.match(pattern, date_str) or date_str == 'T00:00:00Z':
        return True, "1"
    else:
        return False, "Формат даты неверный"


def validate_year(year: str) -> tuple[bool, str]:
    if not year.isdigit():
        return False, 'Год содержит не цифры'

    if int(year) <= 1970 or int(year) >= 2100:
        return False, 'Год не может быть меньше 1970 или больше 2100'

    return True, '1'


def validate_quarter(quarter: str) -> tuple[bool, str]:
    if not quarter.isdigit():
        return False, 'Квартал содержит не цифры'

    if not (1 <= int(quarter) <= 4):
        return False, 'Допустимые значения: 1, 2, 3, 4'

    return True, '1'

def validate_cash(value_list: list) -> tuple[bool, str]:
    for value in value_list:
        if not value.isdigit():
            return False, 'Все величины в разделе указываются в копейках  '

    return True, '1'