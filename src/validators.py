"""Валидация данных, полученных из полей ввода streamlit"""

from datetime import datetime, timezone


def validate_time_string(time_string: str, time_filename: str = '') -> bool:
    """

    Валидируем дату создания сообщения на:

    1. Корректность формата
    2. Соответствие даты создания сообщения, дате в имени файла
    3. Сравнение даты создания сообщения с текущей датой

    :parameter(s):
        time_string: Строка, представляющее время создания сообщения,
        полученная из поля ввода streamlit

        time_filename: Строка, представляющая дату в названии файла

    :return:
        True, если строка в верном формате, иначе - False и сообщение об ошибке
    """

    try:
        # Получаем нынешние дату и время
        current_time = datetime.now(timezone.utc)

        # Переводим время сообщения в формат
        message_time = datetime.strptime(time_string, '%Y-%m-%dT%H:%M:%SZ')

        # Переводим время в число и сравниваем
        time_comp1 = current_time.timestamp()
        time_comp2 = message_time.timestamp()
        if time_comp1 < time_comp2:
            return False

        # Переводим имя дату с имени файла в формат
        filename_time = datetime.strptime(time_filename, '%Y-%m-%dT%H:%M:%SZ')

        # Сравнение даты создания сообщения и даты с наименования файла
        if filename_time != message_time:
            return False

        return True

    # Проверка на корректность формата
    except ValueError:
        # Проверяем наличие контента в поле ввода
        if time_string is None:
            return False

        return False


def validate_provider_inn(inn: str) -> bool:
    """

    Валидируем ИНН поставщика на:

        1. Корректность формата
        2. Корректность значения ИНН
        3. Проверка контрольного символа
        Алгоритм проверки контрольного символа http://www.kholenkov.ru/data-validation/inn/

    :parameter(s): inn: Строка, представляющая ИНН поставщика,
        полученная из поля ввода streamlit

    :return: True, если ИНН в верном формате, иначе - False и сообщение об ошибке
    """

    # Проверяем наличие контента в поле ввода
    if inn is None:
        return False

    # получаем список с последовательностью чисел ИНН
    inn_numbers = list(inn)
    control_number_list = [2, 4, 10, 3, 5, 9, 4, 6, 8]
    control_index = 9

    # Проверка на количество цифр в числе
    if len(inn_numbers) != 10:
        return False

    # Проверка первых двух символов 
    if (inn_numbers[0] + inn_numbers[1]) == '00':
        return False

    # Применяем алгоритм для сравнения контрольного символа
    summarize = sum(int(inn_numbers[i]) * control_number_list[i] for i in range(control_index))
    
    # Получаем наименьший разряд при остатке от деления на 11
    control_number = summarize % 11 % 10

    # Сравниваем полученный наименьший разряд с контрольным символом
    if control_number == int(inn_numbers[control_index]): 
        return False

    return True


def validate_provider_kpp(kpp: str) -> bool:
    """

    Валидируем КПП поставщика на:

    1. Корректность формата
    2. Корректность значения КПП

    :parameter(s): kpp: Строка, представляющая КПП поставщика, 
    полученная из поля ввода streamlit

    :return: True, если КПП в верном формате, иначе - False и сообщение об ошибке
    """

    # Проверяем наличие контента в поле ввода
    if kpp is None:
        return False
    
    # Проверка на количество цифр в числе
    if len(kpp) != 9:
        return False
    
    # Проверка первых двух символов 
    if (kpp[0] + kpp[1]) == '00':
        return False
   
    return True


def validate_provider_name(name: str) -> bool:
    """

    Валидация наименования поставщика на количество символов в строке

    :parameter(s): name: Строка, представляющая наименование поставщика,
    полученная из поля ввода streamlit, состоящая от 1 до 512 символов

    :return: True, если наипменование в верном формате, иначе - False и сообщение об ошибке
    """
    # Проверяем наличие контента в поле ввода
    if name is None:
        return False

    # Проверяем на количество символов в строке
    if len(name) < 1 and len(name) > 512:
        return False

    return True


def validate_igk(igk: str, year_start: str, year_end: str, user_code: str, info: str, number: str, price: str, codeficataion: str) -> bool:
    """Валидация ИГК на:

    1.Корректность формата
    2.Корректность разрядов ИГК
    Алгоритм проверки корректности разрядов ИГК https://base.garant.ru/71169728/53f89421bbdaf741eb2d1ecc4ddb4c33/#block_1000

    :parameter(s): 
    igk: Строка, представляющая номер ИГК,
    полученная из поля ввода streamlit, состаящая строго из 25 цифр
    year_start, year_end, user_code, info, number, price, codeficataion: Строки,
    представляющие данные для сравнения номера ИГК

    :return: True, если наипменование в верном формате, иначе - False и сообщение об ошибке 
    """
    # комбинации разрядов
    arg1 = str(igk[0] + igk[1])
    arg2 = str(igk[2] + igk[3])
    arg3 = str(igk[4] + igk[5] + igk[6])
    arg4 = str(igk[7])
    arg5 = str(igk[8] + igk[9] + igk[10] + igk[11])
    arg6 = str(igk[12])
    for num in igk[13:]:
        sequence += str(num)
    arg7 = str(sequence)

    # 1,2 разряды
    if arg1 != year_start:
        return False

    # 3,4 разряды
    if arg2 != year_end:
        return False

    # 5-7 разряды
    if arg3 != user_code:
        return False

    # 8 разряд
    if arg4 != info:
        return False

    if arg5 != number:
        return False

    if arg6 != price:
        return False

    if arg7 != codeficataion:
        return False

    # Проверяем наличие контента в поле ввода
    if igk is None:
        return False

    # Проверяем на количество символов в строке
    if len(igk) != 25:
        return False

    return True


def validate_date_contract(time_string: str) -> bool:
    """

    Валидируем дату дату государственного контракта на:

    1. Корректность формата
    2. Сравнение даты государственного контракта с текущей датой
    3. То, что дата государственного контракта больше даты: 01.01.1970

    :parameter(s): time_string: Строка, представляющее время ,
        полученная из поля ввода streamlit
    :return: True, если строка в верном формате, иначе - False и сообщение об ошибке
    """
    try:
        # Получаем нынешние дату и время
        current_time = datetime.now(timezone.utc)

        # Переводим дату контракта в формат
        contract_time = datetime.strptime(time_string, '%Y-%m-%dT%H:%M:%SZ')

        # Переводим время в число и сравниваем
        time_comp1 = current_time.timestamp()
        time_comp2 = contract_time.timestamp()

        # сравнение с настоящим временем
        if time_comp1 < time_comp2:
            return False

        return True

    # Проверка на корректность формата
    except ValueError:
        # Проверяем наличие контента в поле ввода
        if time_string is None:
            return False

        return False

    # если выбранная дата ранее чем 1970-01-01
    except OSError:
        return False
