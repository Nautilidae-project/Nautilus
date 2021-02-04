
class EventoModelo:

    def __init__(self, listEvento: list = None, dictEvento: dict = None):
        self.eventoId = None
        self.titulo = None
        self.detalhe = None
        self.grupoId = None
        self.dataEvento = None
        self.dataCadastro = None
        self.horaInicio = None
        self.horaFim = None
        self.diaInteiro = None

        if listEvento is not None:
            self.fromList(listEvento)
        elif dictEvento is not None:
            self.fromDict(dictEvento)
        
    def toDict(self):
        dictEvento = {
        'eventoId': self.eventoId,
        'titulo': self.titulo,
        'detalhe': self.detalhe,
        'grupoId': self.grupoId,
        'dataEvento': self.dataEvento,
        'dataCadastro': self.dataCadastro,
        'horaInicio': self.horaInicio,
        'horaFim': self.horaFim,
        'diaInteiro': self.diaInteiro
        }
        return dictEvento

    def fromDict(self, dictEvento):
        self.eventoId = dictEvento['eventoId'],
        self.titulo = dictEvento['titulo'],
        self.detalhe = dictEvento['detalhe'],
        self.grupoId = dictEvento['grupoId'],
        self.dataEvento = dictEvento['dataEvento'],
        self.dataCadastro = dictEvento['dataCadastro'],
        self.horaInicio = dictEvento['horaInicio'],
        self.horaFim = dictEvento['horaFim'],
        self.diaInteiro = dictEvento['diaInteiro']

    def fromList(self, listEvento):
        self.eventoId = listEvento[0],
        self.titulo = listEvento[1],
        self.detalhe = listEvento[2],
        self.grupoId = listEvento[3],
        self.dataEvento = listEvento[4],
        self.dataCadastro = listEvento[5],
        self.horaInicio = listEvento[6],
        self.horaFim = listEvento[7],
        self.diaInteiro = listEvento[8]

    def __repr__(self):
        return f'Evento(\neventoId: {self.eventoId}, titulo: {self.titulo}, detalhe: {self.detalhe}, \n' \
               f'grupoId: {self.grupoId}, dataEvento: {self.dataEvento}, dataCadastro: {self.dataCadastro}\n' \
               f'horaInicio: {self.horaInicio}, horaFim: {self.horaFim}, diaInteiro: {self.diaInteiro}\n\n)'