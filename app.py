import streamlit as st
from datetime import datetime

from src.validators import validate_time_string

import xml.etree.ElementTree as ET
from xml.dom.minidom import parseString

INCORRECT_STRING_ERROR = (
    'Время не соответствует шаблону "%Y-%m-%dT%H:%M:%SZ". Поле ввода не должно содержать пробелов.'
    'Пример корректно введенного времени: 2024-02-14T15:11:54Z')


def generate_xml(message_data, organization_data):
    # Создание корневого элемента Message с атрибутами
    message = ET.Element("Message", PreviousUID=message_data['PreviousUID'], UID=message_data['UID'],
                         CreateDate=message_data['CreateDate'])

    # Добавление элемента Organization с его атрибутами внутрь Message
    ET.SubElement(message, "Organization", ContractDate=organization_data['ContractDate'],
                  GOZUID=organization_data['GOZUID'], Name=organization_data['Name'], KPP=organization_data['KPP'],
                  INN=organization_data['INN'])

    # Построение строки XML из дерева ET
    rough_string = ET.tostring(message, 'utf-8')
    reparsed = parseString(rough_string)

    # Возвращаем красиво отформатированную XML строку
    return reparsed.toprettyxml(indent="  ")


# Функция для инициализации состояния сеанса. Сюда по сути нужно пихать только даты, т.к они обновляют состояние
# приложения
def init_session_state():
    if 'CreateDate' not in st.session_state:
        st.session_state.CreateDate = datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
    if 'ContractDate' not in st.session_state:
        st.session_state.ContractDate = datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")


def message_form():
    st.write('## Message')
    # Именование не соответствует правилам, но в силу сжатых сроков для удобства - просто копипаст из xml
    PreviousUID = st.text_input('PreviousUID',
                                '0',
                                help='Всегда 0')
    UID = st.text_input('UID',
                        '0',
                        help='help')
    # Используем значения из состояния сеанса
    CreateDate = st.text_input('CreateDate', st.session_state.CreateDate, help='Дата создания документа')
    if not validate_time_string(CreateDate):
        st.error(INCORRECT_STRING_ERROR)
    else:
        st.session_state.CreateDate = CreateDate  # Обновляем состояние сеанса при валидном вводе

    return {'PreviousUID': PreviousUID, 'UID': UID, 'CreateDate': CreateDate}


def organization_form():
    st.write('## Organization')
    ContractDate = st.text_input('ContractDate', st.session_state.ContractDate, help='В формате 2023-12-15T00:00:00Z')
    if not validate_time_string(ContractDate):
        st.error(INCORRECT_STRING_ERROR)
    else:
        st.session_state.ContractDate = ContractDate  # Обновляем состояние сеанса при валидном вводе
    GOZUID = st.text_input('GOZUID', '', help='игК')
    Name = st.text_input('Name', '', help='help')
    KPP = st.text_input('KPP', '', help='help')
    INN = st.text_input('INN', '', help='help')
    return {'ContractDate': ContractDate, 'GOZUID': GOZUID, 'Name': Name, 'KPP': KPP, 'INN': INN}


def main():
    init_session_state()  # Инициализируем состояние сеанса

    st.title('XML Template Filler')

    Message = message_form()
    Organization = organization_form()

    # Итого остается реализовать то же самое, что и для Message и Organization
    #

    if st.button('Generate XML'):
        xml_data = generate_xml(Message, Organization)
        st.text_area("Generated XML", xml_data, height=300)


if __name__ == '__main__':
    main()
