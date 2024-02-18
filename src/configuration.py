# def __init__():
#     pass

class  GlobalErrorMessages():
    """Текст ошибок при валидации
    """

    def __init__(self) -> None:
        pass

    UNCORRECT_STRING_FORMAT = "Некорректный формат"
    FIELD_STRING_FILL = "Не заполнено поле"
    MESSAGE_CREATION_DATE_MESSAGE = "Дата создания сообщения превышает текущую дату"
    COMPARE_WITH_FILENAME = "Дата создания сообщения не соответствует дате в наименовнии файла"
    UNCORRECT_INN_VALUE = "Некорректное значение ИНН"
    UNCORRECT_KPP_VALUE = "Некорректное значение КПП"
    MESSAGE_CREATION_DATE_CONTRACT = "Дата государственного контракта превышает текущую дату"