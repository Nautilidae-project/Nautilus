
class Evento:

    def __init__(self):
        self.eventoId = None
        self.titulo = None
        self.detalhe = None
        self.turmaId = None
        self.dataEvento = None
        self.dataCadastro = None
        self.horaInicio = None
        self.horaFim = None
        self.diaInteiro = None
        
    def toDict(self):
        dictEvento = {
        'eventoId': self.eventoId,
        'titulo': self.titulo,
        'detalhe': self.detalhe,
        'turmaId': self.turmaId,
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
        self.turmaId = dictEvento['turmaId'],
        self.dataEvento = dictEvento['dataEvento'],
        self.dataCadastro = dictEvento['dataCadastro'],
        self.horaInicio = dictEvento['horaInicio'],
        self.horaFim = dictEvento['horaFim'],
        self.diaInteiro = dictEvento['diaInteiro']

    def __repr__(self):
        return f'Evento(\neventoId: {self.eventoId}, titulo: {self.titulo}, detalhe: {self.detalhe}, \n' \
               f'turmaId: {self.turmaId}, dataEvento: {self.dataEvento}, dataCadastro: {self.dataCadastro}, horaInicio: {self.horaInicio}, \n' \
               f'horaFim: {self.horaFim}, diaInteiro: {self.diaInteiro}'