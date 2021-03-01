import datetime


class PagamentoModelo:

    def __init__(self, listPagamento: list = None, dictPagamento: dict = None):

        self.pagId = None
        self.clienteId = None
        self.planoId = None
        self.valorPlano = None
        self.valorAPagar = None
        self.valorRecebido = None
        self.formaPagamento = 'Crédito'
        self.dataVencimento = None
        self.dataPagamento = None
        self.situacao = 'aPagar'
        self.dataCadastro = None

    def toDict(self):
        dictPagamento = {
            'pagId': self.pagId,
            'clienteId': self.clienteId,
            'planoId': self.planoId,
            'valorPlano': self.valorPlano,
            'valorAPagar': self.valorAPagar,
            'valorRecebido': self.valorRecebido,
            'formaPagamento': self.formaPagamento,
            'dataVencimento': self.dataVencimento,
            'dataPagamento': self.dataPagamento,
            'situacao': self.situacao,
            'dataCadastro': self.dataCadastro

        }
        return dictPagamento

    def fromDict(self, dictPagamento: dict):
        self.pagId = dictPagamento['pagId']
        self.clienteId = dictPagamento['clienteId']
        self.planoId = dictPagamento['planoId']
        self.valorPlano = dictPagamento['valorPlano']
        self.valorAPagar = dictPagamento['valorAPagar']
        self.valorRecebido = dictPagamento['valorRecebido']
        self.formaPagamento = dictPagamento['formaPagamento']
        self.dataVencimento = dictPagamento['dataVencimento']
        self.dataPagamento = dictPagamento['dataPagamento']
        self.situacao = dictPagamento['situacao']
        self.dataCadastro = dictPagamento['dataCadastro']

    def fromList(self, listPagamento: list):
        pass

    def __repr__(self):
        return f"""Pagamento(
        pagId: {self.pagId},
        clienteId: {self.clienteId},
        planoId: {self.planoId},
        dataVencimento: {self.dataVencimento},
        valorPlano: {self.valorPlano},
        valorAPagar: {self.valorAPagar},
        valorRecebido: {self.valorRecebido},
        dataCadastro: {self.dataCadastro}, 
        formaPagamento: {self.formaPagamento}\n)"""
