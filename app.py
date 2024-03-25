import streamlit as st

from src.forms import *
from src.xml_utils import generate_xml
from src.autocomplete import *

def main():
    st.title('XML Template Filler')

    # если xml_file ещё не сгенерирован, то вызов переменной вызовет ошибку,
    # поэтому нужно её предварительно обнулить 
    xml_file = None
    
    with st.form("my_form"):
        Message = message_form()
        Organization = organization_form()

        upload_file = upload_xlsx()

        # автозаполнение
        if upload_file:
            autocomplete_data = get_data(upload_file)

            ContractSpending = contract_spending_form(autocomplete_data)
            ContractFinance = contract_finance_form(autocomplete_data)
        else:
            ContractSpending = contract_spending_form()
            ContractFinance = contract_finance_form()

        # generate_xml может принимать только 7 аргументов, поэтому элементы Form объединены в список
        Form = [form_form(), cash_form(), ContractSpending, ContractFinance,]
        Supplement = supplement_form()
        Part = parts_form()
        Reasons = reasons_form()

        if st.form_submit_button("Сгенерировать XML"):
            xml_file = view_xml(Message, Organization, Form, ContractSpending, Supplement, Part, Reasons)

    if xml_file:
        st.download_button(
            label="Download XML File",
            data=xml_file,
            file_name="message.xml",
            mime="text/xml"
        )


if __name__ == '__main__':
    main()