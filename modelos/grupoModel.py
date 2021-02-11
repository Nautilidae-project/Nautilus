import datetime


class GrupoModelo:

    def __init__(self, listGrupo: list = None, dictGrupo: dict = None):

        self.grupoId = None
        self.titulo = None
        self.descricao = None
        self.nomeCategoria = None
        self.corCategoria = None
        self.dataCadastro = None
        self.dataUltAlt = None

        if listGrupo is not None:
            self.fromList(listGrupo)
        elif dictGrupo is not None:
            self.fromDict(dictGrupo)

    def toDict(self):
        dictGrupo = {
            'grupoId': self.grupoId,
            'titulo': self.titulo,
            'descricao': self.descricao,
            'nomeCategoria': self.nomeCategoria,
            'corCategoria': self.corCategoria,
            'dataCadastro': self.dataCadastro,
            'dataUltAlt': self.dataUltAlt
        }
        return dictGrupo

    def fromDict(self, dictGrupo: dict):
        if dictGrupo['grupoId'] is not None:
            self.grupoId = dictGrupo['grupoId']

        if dictGrupo['dataCadastro'] is not None:
            self.dataCadastro = dictGrupo['dataCadastro']

        if dictGrupo['dataUltAlt'] is not None:
            self.dataUltAlt = dictGrupo['dataUltAlt']

        self.titulo = dictGrupo['titulo']
        self.descricao = dictGrupo['descricao']
        self.nomeCategoria = dictGrupo['nomeCategoria']
        self.corCategoria = dictGrupo['corCategoria']


    def fromList(self, listGrupo: list):
        self.grupoId = listGrupo[0]
        self.titulo = listGrupo[1]
        self.descricao = listGrupo[2]
        self.nomeCategoria = listGrupo[3]
        self.corCategoria = listGrupo[4]
        self.dataCadastro = listGrupo[5]
        self.dataUltAlt = listGrupo[6]

    def __repr__(self):
        return f"""Grupo(\n    grupoId: {self.grupoId}, titulo: {self.titulo}, descricao: {self.descricao}, 
                    nomeCategoria: {self.nomeCategoria}, corCategoria: {self.corCategoria}, dataCadastro: {self.dataCadastro}, 
                    dataUltAlt: {self.dataUltAlt}\n)"""
