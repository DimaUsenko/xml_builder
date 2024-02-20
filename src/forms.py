from src.validators import *

from datetime import datetime

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


def form8_form():
    st.write('## Form8')

    Quarter = st.selectbox('Квартал (Quarter)', ('1', '2', '3', '4'))
    validate_wrapper(validate_quarter(Quarter))

    Year = st.text_input('Год (Year)', value=datetime.now().strftime("%Y"), help='help')
    validate_wrapper(validate_year(Year))

    ReportDate = st.text_input('ReportDate', 'T00:00:00Z', help=DATE_HELP)
    validate_wrapper(validate_date(ReportDate))

    return {'Quarter': Quarter, 'Year': Year, 'ReportDate': ReportDate}


def contract_spending_form():
    st.write('## Собственные расходы (ContractSpending)')

    Income = st.text_input('Income', '', help='Указывается в копейках')
    Reserve = st.text_input('Reserve', '', help='Указывается в копейках')
    Other = st.text_input('Всего прочие расходы (Other)', '', help='Указывается в копейках')
    Rates = st.text_input('Тарифы (Rates)', '', help='Указывается в копейках')
    Taxes = st.text_input('Налоги (Taxes)', '', help='Указывается в копейках')
    Salary = st.text_input('Заработная плата (Salary)', '', help='Указывается в копейках')
    Total = st.text_input('Всего собственные расходы (Total)', '', help='Указывается в копейках')

    return {'Income': Income, 'Reserve': Reserve, 'Other': Other, 'Rates': Rates, 'Taxes': Taxes, 'Salary': Salary,
            'Total': Total}


def contractors_contractor_form():
    st.write('## Contractors.Contractor')

    ContractDate = st.text_input('Дата государственного контракта (ContractDate)', 'T00:00:00Z', help='В формате 2001-01-01T00:00:00Z')
    validate_wrapper(validate_date(ContractDate))

    Name = st.text_input('Наименование поставщика (Name)', key="Contractors_Name", value='', help='help')
    INN = st.text_input('ИНН Поставщика (INN)', key="Contractors_INN", value='', help='help')
    Total = st.text_input('Total', key="Contractors_Total", value='', help='Указывается в копейках')

    FinishDate = st.text_input('FinishDate', 'T00:00:00Z', help='В формате 2001-01-01T00:00:00Z')
    validate_wrapper(validate_date(FinishDate))

    PaymentCurrent = st.text_input('PaymentCurrent', '', help='help')
    PaymentPlanned = st.text_input('PaymentPlanned', '', help='help')
    Cost = st.text_input('Cost', '', help='help')
    AccountNumber = st.text_input('AccountNumber', '', help='help')
    ContractNumber = st.text_input('ContractNumber', '', help='help')

    return {'ContractDate': ContractDate, 'Name': Name, 'INN': INN, 'Total': Total, 'FinishDate': FinishDate,
            'PaymentCurrent': PaymentCurrent,
            'PaymentPlanned': PaymentPlanned, 'Cost': Cost, 'AccountNumber': AccountNumber,
            'ContractNumber': ContractNumber}


def planned_pay_form():
    st.write('## Планируемые расчеты с кооперацией (PlannedPay)')

    Total = st.text_input('Total', key="PlannedPay_Total", value='', help='help')
    PaymentCurrent = st.text_input('PaymentCurrent', key="PlannedPay_PaymentCurrent", value='', help='help')
    PaymentPlanned = st.text_input('PaymentPlanned', key="PlannedPay_PaymentPlanned", value='', help='help')

    return {'Total': Total, 'PaymentCurrent': PaymentCurrent, 'PaymentPlanned': PaymentPlanned}


def contract_finance_form():
    st.write('## Финансовые показатели (ContractFinance)')

    DepositeIncome = st.text_input('DepositeIncome', '', help='help')
    PlannedIncome = st.text_input('К поступлению от заказчика (PlannedIncome)', '', help='help')

    DateBalance = st.text_input('DateBalance', 'T00:00:00Z', help='В формате 2024-02-08T00:00:00Z')
    validate_wrapper(validate_date(DateBalance))

    CashBalance = st.text_input('Фактичекский остаток денежных средств на отдельном счете головного исполнителя на дату составления кассового плана на очередной квартал (CashBalance)', '', help='help')
    TotalRequirement = st.text_input('Итого потребность головного исполнителя (TotalRequirement)', '', help='Указывается в копейках')

    return {'DepositeIncome': DepositeIncome, 'PlannedIncome': PlannedIncome, 'DateBalance': DateBalance,
            'CashBalance': CashBalance, 'TotalRequirement': TotalRequirement}


def supplement_form():
    st.write('## Supplement')

    ReportDate = st.text_input('ReportDate', 'T00:00:00Z', help='В формате 2024-02-09T00:00:00Z')
    validate_wrapper(validate_date(ReportDate))

    return {'ReportDate': ReportDate}


def part_form():
    st.write('## Parts')

    Quarter = st.selectbox('Квартал (Quarter)', ('1', '2', '3', '4'), key="<uniquevalueofsomesort>")
    validate_wrapper(validate_quarter(Quarter))

    Year = st.text_input('Год (Year)', key="Part_Year", value=datetime.now().strftime("%Y"), help='help')
    validate_wrapper(validate_year(Year))

    Deviation = st.text_input('Величина отклонения (Deviation)', '', help='help')
    Requirement = st.text_input('Заявленная потребность (Requirement)', '', help='help')

    return {'Quarter': Quarter, 'Year': Year, 'Deviation': Deviation, 'Requirement': Requirement}


def reasons_form():
    st.write('## Код причины (Reasons)')

    Reason = st.text_input('Код причины (Reason)', value='3', help='help')

    return {'Reason': Reason}
