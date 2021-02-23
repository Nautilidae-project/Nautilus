class PlanoModelo:

    def __init__(self, listPlano: list = None, dictPlano: dict = None):
        self.planoId = None
        self.nomePlano = None
        self.valor = None
        self.descricao = None
        self.periodoUnidade = None
        self.dataInicio = None
        self.dataFim = None
        self.presencial = None

        if listPlano is not None:
            self.fromList(listPlano)
        elif dictPlano is not None:
            self.fromDict(dictPlano)

    def toDict(self):
        dictPlano = {
            'planoId': self.planoId,
            'nomePlano': self.nomePlano,
            'valor': self.valor,
            'descricao': self.descricao,
            'periodoUnidade': self.periodoUnidade,
            'dataInicio': self.dataInicio,
            'dataFim': self.dataFim,
            'presencial': self.presencial
        }
        return dictPlano

    def fromDict(self, dictPlano):
        self.planoId = dictPlano['planoId'],
        self.nomePlano = dictPlano['nomePlano'],
        self.valor = dictPlano['valor'],
        self.descricao = dictPlano['descricao'],
        self.periodoUnidade = dictPlano['periodoUnidade'],
        self.dataInicio = dictPlano['dataInicio'],
        self.dataFim = dictPlano['dataFim']
        self.presencial = dictPlano['presencial']

    def fromList(self, listPlano):
        self.planoId = listPlano[0],
        self.nomePlano = listPlano[1],
        self.valor = listPlano[2],
        self.descricao = listPlano[3],
        self.periodoUnidade = listPlano[4],
        self.dataInicio = listPlano[5],
        self.dataFim = listPlano[6],
        self.presencial = listPlano[7]

    def __repr__(self):
        return f'Plano(\nplanoId: {self.planoId}, nomePlano: {self.nomePlano}, valor: {self.valor}, \n' \
               f'descricao: {self.descricao}, periodoUnidade: {self.periodoUnidade}, dataInicio: {self.dataInicio}\n' \
               f'dataFim: {self.dataFim} , presencial: {self.presencial})'