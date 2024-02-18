from datetime import datetime, timezone

from configuration import GlobalErrorMessages


error = GlobalErrorMessages()

def validate_time_string(time_string: str, time_filename: str = '') -> bool:
    """
    Валидируем дату создания сообщения на:
    1. Корректность формата
    2. Соответствие даты создания сообщения, дате в имени файла
    3. Сравнение даты создания сообщения с текущей датой 

    :parameter(s) time_string: Строка, представляющее время,
        полученная из поля ввода streamlit
    :return: True, если строка в верном формате, иначе - False и сообщение об ошибке
    """
    try:
        # Получаем нынешние дату и время 
        current_time_no_format = datetime.now(timezone.utc)
        current_time = current_time_no_format.strftime('%Y-%m-%dT%H:%M:%SZ')

        # Переводим время сообщения в формат
        message_time = datetime.strptime(time_string, '%Y-%m-%dT%H:%M:%SZ')

        # Переводим время в число и сравниваем 
        time_comp1 = current_time.timestamp()
        time_comp2 = message_time.timestamp()
        if time_comp1 < time_comp2:
            return False, error.MESSAGE_CREATION_DATE_MESSAGE
        
        # Переводим имя дату с имени файла в формат
        filename_time = datetime.strptime(time_filename, '%Y-%m-%dT%H:%M:%SZ')

        # Сравнение даты создания сообщения и даты с наименования файла
        if filename_time != message_time:
            return False, error.COMPARE_WITH_FILENAME

        return True

    # Проверка на корректность формата
    except ValueError:
        # Проверяем наличие контента в поле ввода
        if time_string is None:
            return False, error.FIELD_STRING_FILL
 
        return False, error.UNCORRECT_STRING_FORMAT

def validate_provider_inn(inn: str) -> bool:
    """
    Валидируем ИНН поставщика на:
    1. Корректность формата
    2. Корректность значения ИНН
    3. Проверка контрольного символа 

    :parameter(s) inn: Строка, представляющая ИНН поставщика, 
    полученная из поля ввода streamlit
    :return: True, если ИНН в верном формате, иначе - False и сообщение об ошибке
    """

    # Проверяем наличие контента в поле ввода
    if inn is None:
        return False, error.FIELD_STRING_FILL

    # получаем список с последовательностью чисел ИНН
    inn_numbers = list(inn)
    control_number_list = [2, 4, 10, 3, 5, 9, 4, 6, 8]
    control_index = 9

    # Проверка на количество цифр в числе
    if len(inn_numbers) != 10:
        return False, error.UNCORRECT_STRING_FORMAT
    
    # Проверка первых двух символов 
    if (inn_numbers[0] + inn_numbers[1]) == '00':
        return False, error.UNCORRECT_STRING_FORMAT
    
    # Применяем алгоритм для сравнения контрольного символа
    summarize = sum(int(inn_numbers[i]) * control_number_list[i] for i in range(control_index))
    
    # Получаем наименьший разряд при остатке от деления на 11
    control_number = summarize % 11 % 10

    # Сравниваем полученный наименьший разряд с контрольным символом
    if control_number == int(inn_numbers[control_index]): 
        return False, error.UNCORRECT_INN_VALUE

    return True

def validate_provider_kpp(kpp: str) -> bool:
    """
    Валидируем КПП поставщика на:
    1. Корректность формата
    2. Корректность значения КПП

    :parameter(s) kpp: Строка, представляющая КПП поставщика, 
    полученная из поля ввода streamlit
    :return: True, если КПП в верном формате, иначе - False и сообщение об ошибке
    """

    # Проверяем наличие контента в поле ввода
    if kpp is None:
        return False, error.FIELD_STRING_FILL
    
    # Проверка на количество цифр в числе
    if len(kpp) != 9:
        return False, error.UNCORRECT_KPP_VALUE
    
    # Проверка первых двух символов 
    if (kpp[0] + kpp[1]) == '00':
        return False, error.UNCORRECT_KPP_VALUE
   
    return True

def validate_provider_name(name: str) -> bool:
    """Валидация наименования поставщика на количество символов в строке

    :parameter(s) name: Строка, представляющая наименование поставщика, 
    полученная из поля ввода streamlit, состоящая от 1 до 512 символов 
    :return: True, если наипменование в верном формате, иначе - False и сообщение об ошибке 
    """
    # Проверяем наличие контента в поле ввода
    if name is None:
        return False, error.FIELD_STRING_FILL

    # Проверяем на количество символов в строке
    if len(name) < 1 and len(name) > 512:
        return False, error.UNCORRECT_STRING_FORMAT

    return True

def validate_igk(igk: str) -> bool:
    # Проверяем наличие контента в поле ввода
    if igk is None:
        return False, error.FIELD_STRING_FILL

    # Проверяем на количество символов в строке
    if len(igk) != 25:
        return False, error.UNCORRECT_STRING_FORMAT
    


    return True

def validate_date_contract(time_string: str) -> bool:
    """
    Валидируем дату дату государственного контракта на:
    1. Корректность формата
    2. Сравнение даты государственного контракта с текущей датой 
    3. То, что дата государственного контракта больше даты: 01.01.1970

    :parameter(s) time_string: Строка, представляющее время,
        полученная из поля ввода streamlit
    :return: True, если строка в верном формате, иначе - False и сообщение об ошибке
    """
    try:
        # Получаем нынешние дату и время 
        current_time_no_format = datetime.now(timezone.utc)
        current_time = current_time_no_format.strftime('%Y-%m-%dT%H:%M:%SZ')

        # Переводим дату контракта в формат
        contract_time = datetime.strptime(time_string, '%Y-%m-%dT%H:%M:%SZ')

        # Переводим время в число и сравниваем 
        time_comp1 = current_time.timestamp()
        time_comp2 = contract_time.timestamp()
        if time_comp1 < time_comp2:
            return False, error.MESSAGE_CREATION_DATE_CONTRACT

        return True

    # Проверка на корректность формата
    except ValueError:
        # Проверяем наличие контента в поле ввода
        if time_string is None:
            return False, error.FIELD_STRING_FILL
 
        return False, error.UNCORRECT_STRING_FORMAT




# def validate_():
    # pass