import streamlit as st

import io

from src.forms import *
from src.xml_utils import generate_xml


def main():
    st.title('XML Template Filler')

    Message = message_form()
    Organization = organization_form()
    # generate_xml может принимать только 10 аргументов, поэтому элементы Form объединены в список
    Form = [form_form(), form8_form(), contractors_contractor_form(), planned_pay_form(), contract_finance_form()]
    ContractSpending = contract_spending_form()
    Supplement = supplement_form()
    Part = part_form()
    Reasons = reasons_form()

    if st.button('Generate XML'):
        xml_data = generate_xml(Message, Organization, Form, ContractSpending, Supplement, Part, Reasons)

        st.text_area("Generated XML", xml_data, height=300)

        xml_file = io.BytesIO(xml_data.encode('utf-8'))

        # Use Streamlit's download button to allow downloading the XML file
        st.download_button(
            label="Download XML File",
            data=xml_file,
            file_name="message.xml",
            mime="text/xml"
        )


if __name__ == '__main__':
    main()
