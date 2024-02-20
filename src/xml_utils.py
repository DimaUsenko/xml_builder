import xml.etree.ElementTree as ET
from xml.dom.minidom import parseString


def generate_xml(message_data, organization_data, form_data, contract_spending_data, supplement_data, part_data,
                 reasons_data):
    # Создание корневого элемента Message с атрибутами
    message = ET.Element("Message", PreviousUID=message_data['PreviousUID'], UID=message_data['UID'],
                         CreateDate=message_data['CreateDate'])

    # Добавление элемента Organization с его атрибутами внутрь Message
    ET.SubElement(message, "Organization", ContractDate=organization_data['ContractDate'],
                  GOZUID=organization_data['GOZUID'], Name=organization_data['Name'], KPP=organization_data['KPP'],
                  INN=organization_data['INN'])

    # Добавление элемента Forms внутрь Message
    forms = ET.SubElement(message, "Forms")

    # Добавление элемента Form8 с его атрибутами внутрь Forms
    form8 = ET.SubElement(forms, "Form8", Quarter=form_data[1]['Quarter'], Year=form_data[1]['Year'],
                          ReportDate=form_data[1]['ReportDate'])

    ET.SubElement(form8, "ContractSpending", Income=contract_spending_data['Income'],
                  Reserve=contract_spending_data['Reserve'],
                  Other=contract_spending_data['Other'],
                  Rates=contract_spending_data['Rates'],
                  Taxes=contract_spending_data['Taxes'],
                  Salary=contract_spending_data['Salary'],
                  Total=contract_spending_data['Total'])

    # Добавление элемента ContractSpending с его атрибутами внутрь Form8
    contractors = ET.SubElement(form8, "Contractors")

    # Добавление элемента Contractor с его атрибутами внутрь Contractors
    ET.SubElement(contractors, "Contractor", ContractDate=form_data[2]['ContractDate'],
                  Name=form_data[2]['Name'], INN=form_data[2]['INN'], Total=form_data[2]['Total'],
                  FinishDate=form_data[2]['FinishDate'], PaymentCurrent=form_data[2]['PaymentCurrent'],
                  PaymentPlanned=form_data[2]['PaymentPlanned'], Cost=form_data[2]['Cost'],
                  AccountNumber=form_data[2]['AccountNumber'], ContractNumber=form_data[2]['ContractNumber'])

    # Добавление элемента Contractors.Contractor с его атрибутами внутрь Forms
    # ET.SubElement(forms, "Contractors.Contractor", ContractDate=form_data[2]['ContractDate'],
    #               Name=form_data[2]['Name'], INN=form_data[2]['INN'], Total=form_data[2]['Total'],
    #               FinishDate=form_data[2]['FinishDate'], PaymentCurrent=form_data[2]['PaymentCurrent'],
    #               PaymentPlanned=form_data[2]['PaymentPlanned'], Cost=form_data[2]['Cost'],
    #               AccountNumber=form_data[2]['AccountNumber'], ContractNumber=form_data[2]['ContractNumber'])

    # Добавление элемента PlannedPay с его атрибутами внутрь Forms
    ET.SubElement(form8, "PlannedPay", Total=form_data[3]['Total'], PaymentCurrent=form_data[3]['PaymentCurrent'],
                  PaymentPlanned=form_data[3]['PaymentPlanned'])

    # Добавление элемента ContractFinance с его атрибутами внутрь Forms
    ET.SubElement(form8, "ContractFinance", DepositeIncome=form_data[4]['DepositeIncome'],
                  PlannedIncome=form_data[4]['PlannedIncome'], DateBalance=form_data[4]['DateBalance'],
                  CashBalance=form_data[4]['CashBalance'], TotalRequirement=form_data[4]['TotalRequirement'])

    # Добавление элемента Supplement внутрь Message
    supplement = ET.SubElement(forms, "Supplement", ReportDate=supplement_data['ReportDate'])

    # Добавление элемента Parts внутрь Supplement
    parts = ET.SubElement(supplement, "Parts")

    # Добавление элемента Parts внутрь Supplement
    part = ET.SubElement(parts, "Part", Quarter=part_data['Quarter'], Year=part_data['Year'],
                         Deviation=part_data['Deviation'], Requirement=part_data['Requirement'])

    # Добавление элемента Reasons внутрь Part
    reasons = ET.SubElement(part, "Reasons")
    ET.SubElement(reasons, "Reason").text = reasons_data['Reason']

    # Построение строки XML из дерева ET
    rough_string = ET.tostring(message, 'utf-8')
    reparsed = parseString(rough_string)

    # Возвращаем красиво отформатированную XML строку
    return reparsed.toprettyxml(indent="  ")
