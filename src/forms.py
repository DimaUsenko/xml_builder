from src.validators import *
from src.xml_utils import generate_xml

from datetime import datetime

import io


DATE_HELP = "Все даты указываются в формате временной метки с указанием часового пояса, например: 2024-12-31T23:59:59Z или 2024-12-31T23:59:59+03:00, в случае, если указание времени не требуется указывается T00:00:00Z"


def message_form():
    st.write('## Сообщение (Message)')
    # Именование не соответствует правилам, но в силу сжатых сроков для удобства - просто копипаст из xml
    PreviousUID = st.text_input('Идентификатор предыдущего сообщения (PreviousUID)',
                                '0',
                                help='В первой посылке ожидается 0')
    UID = st.text_input('Идентификатор сообщения (UID)',
                        '0',
                        help='help')
    # Используем значения из состояния сеанса
    CreateDate = st.text_input('Дата создания обращения (CreateDate)', 'T00:00:00Z', help='Дата создания документа')
    validate_wrapper(validate_date(CreateDate))

    return {'PreviousUID': PreviousUID, 'UID': UID, 'CreateDate': CreateDate}


def organization_form():
    st.write('## Поставщик (Organization)')
    ContractDate = st.text_input('ContractDate', 'T00:00:00Z', help='В формате 2023-12-15T00:00:00Z')
    validate_wrapper(validate_date(ContractDate))

    GOZUID = st.text_input('Идентификатор государственного контракта (GOZUID)', '',
                           help='ИГК. Проверка осуществялется в соотвествии с https://base.garant.ru/71169728/53f89421bbdaf741eb2d1ecc4ddb4c33/#block_1000')
    validate_wrapper(validate_igk(GOZUID))

    Name = st.text_input('Name', '', help='help')

    KPP = st.text_input('KPP', '', help='help')
    validate_wrapper(validate_kpp(KPP))

    INN = st.text_input('INN', '', help='help')
    validate_wrapper(validate_inn(INN))

    return {'ContractDate': ContractDate, 'GOZUID': GOZUID, 'Name': Name, 'KPP': KPP, 'INN': INN}


def form_form():
    st.write('## Форма (Form)')

    Type = st.text_input('Type', '8', help='Для данной формы принимается значение 8')

    return {'Type': Type}


def cash_form():
    st.write('## Cash')

    Quarter = st.selectbox('Квартал (Quarter)', ('1', '2', '3', '4'))
    validate_wrapper(validate_quarter(Quarter))

    Year = st.text_input('Год (Year)', value=datetime.now().strftime("%Y"), help='help')
    validate_wrapper(validate_year(Year))

    ReportDate = st.text_input('ReportDate', 'T00:00:00Z', help=DATE_HELP)
    validate_wrapper(validate_date(ReportDate))

    return {'Quarter': Quarter, 'Year': Year, 'ReportDate': ReportDate}


def contract_spending_form(autocomplete: list = []):
    st.write('## Собственные расходы (ContractSpending)')

    # Создаю массив с пустыми строками, чтобы не возникало ошибки при вызове autocomplete[x]
    if not autocomplete:
        autocomplete = ['','','','','','','','','','']

    Income = st.text_input('Income', autocomplete[9], help='Указывается в копейках')
    Reserve = st.text_input('Reserve', autocomplete[8], help='Указывается в копейках')
    Other = st.text_input('Всего прочие расходы (Other)', autocomplete[7], help='Указывается в копейках')
    Repayment = st.text_input('Repayment', autocomplete[6], help='Указывается в копейках')
    Return = st.text_input('Return', autocomplete[5], help='Указывается в копейках')
    OtherTotal = st.text_input('OtherTotal', autocomplete[4], help='Указывается в копейках')
    Rates = st.text_input('Тарифы (Rates)', autocomplete[3], help='Указывается в копейках')
    Taxes = st.text_input('Налоги (Taxes)', autocomplete[2], help='Указывается в копейках')
    Salary = st.text_input('Заработная плата (Salary)', autocomplete[1], help='Указывается в копейках')
    Total = st.text_input('Всего собственные расходы (Total)', autocomplete[0], help='Указывается в копейках')

    validate_list = [Income, Reserve, Other, Repayment, Return, OtherTotal, Rates, Taxes, Salary, Total]
    validate_wrapper(validate_cash(validate_list))
 
    return {'Income': Income, 'Reserve': Reserve, 'Other': Other,
        'Repayment': Repayment, 'Return': Return,
        'OtherTotal': OtherTotal, 'Rates': Rates, 
        'Taxes': Taxes, 'Salary': Salary,'Total': Total}
    

def contract_finance_form(autocomplete: list = []):
    st.write('## Финансовые показатели (ContractFinance)')

    # Создаю массив с пустыми строками, чтобы не возникало ошибки при вызове autocomplete[x]
    if not autocomplete:
        autocomplete = ['','','','','','','','','','','','','','','','','']

    PlannedPay = st.text_input('(PlannedPay)',autocomplete[10], help='help')
    TotalRequirement = st.text_input('Итого потребность головного исполнителя (TotalRequirement)',autocomplete[11], help='Указывается в копейках')
    CashBalance = st.text_input('Фактичекский остаток денежных средств на отдельном счете головного исполнителя на дату составления кассового плана на очередной квартал (CashBalance)',autocomplete[12], help='help')
    PlannedIncome = st.text_input('К поступлению от заказчика (PlannedIncome)',autocomplete[13], help='help')
    PastPayments = st.text_input('(PastPayments)',autocomplete[14], help='help')
    SeparateAccount = st.text_input('(SeparateAccount)',autocomplete[15], help='help')
    BankAccount = st.text_input('(BankAccount)',autocomplete[16], help='help')
    
    validate_list = [PlannedPay, TotalRequirement, CashBalance, PlannedIncome, PastPayments, SeparateAccount, BankAccount]
    validate_wrapper(validate_cash(validate_list))    

    return {'PlannedPay': PlannedPay, 'PastPayments': PastPayments, 
            'SeparateAccount': SeparateAccount, 'BankAccount': BankAccount, 
            'PlannedIncome': PlannedIncome, 'CashBalance': CashBalance, 
            'TotalRequirement': TotalRequirement}


def supplement_form():
    st.write('## Supplement')

    ReportDate = st.text_input('ReportDate', 'T00:00:00Z', help='В формате 2024-02-09T00:00:00Z')
    validate_wrapper(validate_date(ReportDate))

    return {'ReportDate': ReportDate}


def parts_form():
    st.write('## Parts')
    
    col1, col2 = st.columns(2)
    with col1:
        Quarter_1 = st.selectbox('Квартал (Quarter)', ('1', '2', '3', '4'), key="<uniquevalueofsomesort_1>")
        validate_wrapper(validate_quarter(Quarter_1))

        Year_1 = st.text_input('Год (Year)', key="Part_Year_1", value=datetime.now().strftime("%Y"), help='help')
        validate_wrapper(validate_year(Year_1))

        Deviation_1 = st.text_input('Величина отклонения (Deviation)', '', key="Deviation_1", help='help')
        Requirement_1 = st.text_input('Заявленная потребность (Requirement)', '', key="Requirement_1", help='help')
    with col2:
        Quarter_2 = st.selectbox('Квартал (Quarter)', ('1', '2', '3', '4'), key="<uniquevalueofsomesort_2>")
        validate_wrapper(validate_quarter(Quarter_2))

        Year_2 = st.text_input('Год (Year)', key="Part_Year_2", value=datetime.now().strftime("%Y"), help='help')
        validate_wrapper(validate_year(Year_2))

        Deviation_2 = st.text_input('Величина отклонения (Deviation)', '', key="Deviation_2", help='help')
        Requirement_2 = st.text_input('Заявленная потребность (Requirement)', '', key="Requirement_2", help='help')

    return [{'Quarter': Quarter_1, 'Year': Year_1, 'Deviation': Deviation_1, 'Requirement': Requirement_1}, 
            {'Quarter': Quarter_2, 'Year': Year_2, 'Deviation': Deviation_2, 'Requirement': Requirement_2}]


def reasons_form():
    st.write('## Код причины (Reasons)')

    col1, col2 = st.columns(2)

    with col1:
        Reason_11 = st.text_input('Код причины (Reason)', value='7', key="reason_1", help='help')
    with col2:
        Reason_21 = st.text_input('Код причины (Reason)', value='1', key="reason_2", help='help')
        Reason_22 = st.text_input('Код причины (Reason)', value='2', key="reason_3", help='help')

    return {'Reason_11': Reason_11, 'Reason_21': Reason_21, 'Reason_22': Reason_22}


def view_xml(message, organization, form, contractSpending, supplement, part, reasons):
    xml_data = generate_xml(message, organization, form, contractSpending, supplement, part, reasons)

    st.text_area("Generated XML", xml_data, height=300)

    xml_file = io.BytesIO(xml_data.encode('utf-8'))
    
    return xml_file