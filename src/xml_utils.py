import xml.etree.ElementTree as ET
from xml.dom.minidom import parseString


def generate_xml(message_data, organization_data, form_data, contract_spending_data,
                supplement_data, part_data, reasons_data):
    # Создание корневого элемента Message с атрибутами
    message = ET.Element("Message", PreviousUID=message_data['PreviousUID'], 
                        UID=message_data['UID'],
                        CreateDate=message_data['CreateDate'])

    # Добавление элемента Organization с его атрибутами внутрь Message
    ET.SubElement(message, "Organization", ContractDate=organization_data['ContractDate'],
                GOZUID=organization_data['GOZUID'],
                Name=organization_data['Name'], 
                KPP=organization_data['KPP'],
                INN=organization_data['INN'])

    # Добавление элемента Forms внутрь Message
    forms = ET.SubElement(message, "Forms")

    # Добавление элемента cash с его атрибутами внутрь Forms
    cash = ET.SubElement(forms, "Cash", Quarter=form_data[1]['Quarter'], 
                        Year=form_data[1]['Year'],
                        ReportDate=form_data[1]['ReportDate'])

    ET.SubElement(cash, "ContractSpending", Income=contract_spending_data['Income'],
                Reserve=contract_spending_data['Reserve'],
                Other=contract_spending_data['Other'],
                Repayment=contract_spending_data['Repayment'],
                Return=contract_spending_data['Return'],
                OtherTotal=contract_spending_data['OtherTotal'],
                Rates=contract_spending_data['Rates'],
                Taxes=contract_spending_data['Taxes'],
                Salary=contract_spending_data['Salary'],
                Total=contract_spending_data['Total'])


    # Добавление элемента ContractFinance с его атрибутами внутрь Forms
    ET.SubElement(cash, "ContractFinance", PlannedPay=form_data[3]['PlannedPay'],
                TotalRequirement=form_data[3]['TotalRequirement'],
                CashBalance=form_data[3]['CashBalance'],
                PlannedIncome=form_data[3]['PlannedIncome'],
                PastPayments=form_data[3]['PastPayments'],
                SeparateAccount=form_data[3]['SeparateAccount'],
                BankAccount=form_data[3]['BankAccount'],
                )

    # Добавление элемента Supplement внутрь Message
    supplement = ET.SubElement(forms, "Supplement", ReportDate=supplement_data['ReportDate'])

    # Добавление элемента Parts внутрь Supplement
    parts = ET.SubElement(supplement, "Parts")

    # Добавление элемента Part внутрь Parts
    part = ET.SubElement(parts, "Part", Quarter=part_data[0]['Quarter'],
                        Year=part_data[0]['Year'],
                        Deviation=part_data[0]['Deviation'],
                        Requirement=part_data[0]['Requirement'])

    # Добавление элемента Reasons внутрь Part
    reasons = ET.SubElement(part, "Reasons")
    ET.SubElement(reasons, "Reason").text = reasons_data['Reason_11']

    # Добавление элемента Part внутрь Parts
    part = ET.SubElement(parts, "Part", Quarter=part_data[1]['Quarter'],
                        Year=part_data[1]['Year'],
                        Deviation=part_data[1]['Deviation'], 
                        Requirement=part_data[1]['Requirement'])

    # Добавление элемента Reasons внутрь Part
    reasons = ET.SubElement(part, "Reasons")
    ET.SubElement(reasons, "Reason").text = reasons_data['Reason_21']
    ET.SubElement(reasons, "Reason").text = reasons_data['Reason_22']

    # Построение строки XML из дерева ET
    rough_string = ET.tostring(message, 'utf-8')
    reparsed = parseString(rough_string)

    # Возвращаем красиво отформатированную XML строку
    return reparsed.toprettyxml(indent="  ")