import datetime


class GrupoModelo:

    def __init__(self, listGrupo: list=None):
        if listGrupo is not None:
            self.fromList(listGrupo)
        else:
            self.grupoId = None
            # self.participantesId = None
            self.titulo = None
            self.descricao = None
            self.dataCadastro = None
            self.dataUltAlt = None

    def toDict(self):
        dictGrupo = {
            'grupoId': self.grupoId,
            # 'participantesId': self.participantesId,
            'titulo': self.titulo,
            'descricao': self.descricao,
            'dataCadastro': self.dataCadastro,
            'dataUltAlt': self.dataUltAlt
        }
        return dictGrupo

    def fromDict(self, dictGrupo: dict):
        self.grupoId = dictGrupo['grupoId']
        # self.participantesId = dictGrupo['participantesId']
        self.titulo = dictGrupo['titulo']
        self.descricao = dictGrupo['descricao']
        self.dataCadastro = dictGrupo['dataCadastro']
        self.dataUltAlt = dictGrupo['dataUltAlt']

    def fromList(self, listGrupo: list):
        # print(listGrupo)
        self.grupoId = listGrupo[0]
        self.titulo = listGrupo[1]
        self.descricao = listGrupo[2]
        self.dataCadastro = listGrupo[3]
        self.dataUltAlt = listGrupo[4]

    def __repr__(self):
        return f'Grupo(\ngrupoId: {self.grupoId}, titulo: {self.titulo}, \n descricao: {self.descricao}' \
               f'dataCadastro: {self.dataCadastro}, dataUltAlt: {self.dataUltAlt}'