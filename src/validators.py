from datetime import datetime, timezone

from configuration import GlobalErrorMessages

error = GlobalErrorMessages()


# Пример функции для владиации данных
# Каждую функцию пишем в виде validate_{что валидируем}
def validate_time_string(time_string: str, time_filename: str = '') -> bool:
    """
    Валидируем дату создания сообщения на:
    1. Корректность формата
    2. Соответствие даты создания сообщения, дате в имени файла
    3. Сравнение даты создания сообщения с текущей датой 

    :parameter(s) time_string: Строка, представляющее время,
        полученная из поля воода streamlit
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
            return False, error.MESSAGE_CREATION_DATE
        
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


def validate_provider_inn(inn: int):
    """
    Валидируем ИНН поставщика на:
    1. Корректность формата
    2. Проверка контрольного символа 
    :parameter(s) inn: Число, представляющее ИНН поставщика, 
    полученный из поля воода streamlit
    :return: True, если ИНН в верном формате, иначе - False и сообщение об ошибке
    """

    # Проверяем наличие контента в поле ввода
    if inn is None:
        return False, error.FIELD_STRING_FILL

    # получаем список с последовательностью чисел ИНН
    inn_numbers = list(inn)
    control_number_list = [2, 4, 10, 3, 5, 9, 4, 6, 8]
    control_index = 9

    # Проверка нак количество цифр в числе
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


# def validate_():
#     pass
