import pandas as pd
import streamlit as st
from io import BytesIO


def upload_xlsx() :
    st.write('## Подгрузка данных из файла xlsx')

    file_xlsx = st.file_uploader('Загрузите файл xlsx', type='xlsx', accept_multiple_files=False)

    # возвращаем объект file_uploaded класса UploadedFile
    return file_xlsx


def df_from_uploaded(file_uploaded):
    """Объект df из объекта UploadedFile

    Args:
        file_uploaded (str): объект UploadedFile полученный из streamlit
    """

    # Преобразуем в BytesIO  
    bytes_file = file_uploaded.read()
    bytesIO_file = BytesIO(bytes_file)

    # BytesIO в df 
    df = pd.read_excel(bytesIO_file)
    
    return df


def get_data(file_uploaded) -> list:
    
    df = df_from_uploaded(file_uploaded)

    df.columns = ['Plan','','Value']
    value_list = df['Value'].tolist()
    required_value = value_list[6:23]

    # Округляем, из-за кривых подсчётов python
    rounded_list = [int(round(value, 2) * 100) for value in required_value]

    return rounded_list