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