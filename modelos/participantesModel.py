
class ParticipanteModel:

    def __init__(self, listaParticipante: list=None):

        self.eventoId = None
        self.grupoId = None
        self.clienteId = None
        self.grupoId = None

        if listaParticipante is not None:
            self.fromList(listaParticipante)


    def toDict(self):
        dictParticipantes = {
            'eventoId': self.eventoId,
            'clienteId': self.clienteId,
            'grupoId': self.grupoId
        }
        return dictParticipantes

    def fromDict(self, dictParticipantes):
        self.eventoId = dictParticipantes['eventoId'],
        self.grupoId = dictParticipantes['grupoId'],
        self.clienteId = dictParticipantes['clienteId'],
        self.grupoId = dictParticipantes['grupoId']

    def fromList(self, participante:list):
        self.grupoId = participante[0]
        self.clienteId = participante[1]

    def __repr__(self):
        return f'Participantes(\neventoId: {self.eventoId}, clienteId: {self.clienteId}, grupoId: {self.grupoId}\n)'