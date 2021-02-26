import datetime


class PagamentoModelo:

    def __init__(self, listPagamento: list = None, dictPagamento: dict = None):

        self.pagamentoId = None
        self.titulo = None
        self.descricao = None
        self.nomeCategoria = None
        self.corCategoria = None
        self.dataCadastro = None
        self.dataUltAlt = None

        if listPagamento is not None:
            self.fromList(listPagamento)
        elif dictPagamento is not None:
            self.fromDict(dictPagamento)

    def toDict(self):
        dictPagamento = {
            'pagamentoId': self.pagamentoId,
            'titulo': self.titulo,
            'descricao': self.descricao,
            'nomeCategoria': self.nomeCategoria,
            'corCategoria': self.corCategoria,
            'dataCadastro': self.dataCadastro,
            'dataUltAlt': self.dataUltAlt
        }
        return dictPagamento

    def fromDict(self, dictPagamento: dict):
        if dictPagamento['pagamentoId'] is not None:
            self.pagamentoId = dictPagamento['pagamentoId']

        if dictPagamento['dataCadastro'] is not None:
            self.dataCadastro = dictPagamento['dataCadastro']

        if dictPagamento['dataUltAlt'] is not None:
            self.dataUltAlt = dictPagamento['dataUltAlt']

        self.titulo = dictPagamento['titulo']
        self.descricao = dictPagamento['descricao']
        self.nomeCategoria = dictPagamento['nomeCategoria']
        self.corCategoria = dictPagamento['corCategoria']


    def fromList(self, listPagamento: list):
        self.pagamentoId = listPagamento[0]
        self.titulo = listPagamento[1]
        self.descricao = listPagamento[2]
        self.nomeCategoria = listPagamento[3]
        self.corCategoria = listPagamento[4]
        self.dataCadastro = listPagamento[5]
        self.dataUltAlt = listPagamento[6]

    def __repr__(self):
        return f"""Pagamento(\n    pagamentoId: {self.pagamentoId}, titulo: {self.titulo}, descricao: {self.descricao}, 
                    nomeCategoria: {self.nomeCategoria}, corCategoria: {self.corCategoria}, dataCadastro: {self.dataCadastro}, 
                    dataUltAlt: {self.dataUltAlt}\n)"""
