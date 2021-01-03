import datetime

from PyQt5.QtWidgets import QMessageBox

def mascaraCelular(celular):
    return f'({celular[0:2]}) {celular[2:3]}.{celular[3:7]}-{celular[7:]}'


def mascaraCNPJ(cnpj):
    return f'{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:]}'


def mascaraCep(cep):
    return f'{cep[:5]}-{cep[5:]}'

def macaraFormaPagamento(pagamento: str):
    if (pagamento.upper() == 'CC'):
        return 'Cartão de crédito'
    else:
        return 'Outras opções'

def mascaraMeses(data: datetime.date):
    return f'{data.day} de {meses[data.month]} de {data.year}'

def isTrueInt(lista):
    if [bool(i) for i in lista[11]][0]:
        return 1
    else:
        return 0

def isTrueBool(data):
    if [bool(i) for i in data][0]:
        return False
    else:
        return True

formasPagamento = {
    'Cartão de crédito' : 'CC',
    'Outras opções' : 'OP'
}

meses = {
    1: 'Janeiro',
    2: 'Fevereiro',
    3: 'Março',
    4: 'Abril',
    5: 'Maio',
    6: 'Junho',
    7: 'Julho',
    8: 'Agosto',
    9: 'Setembro',
    10: 'Outubro',
    11: 'Novembro',
    12: 'Dezembro'
}