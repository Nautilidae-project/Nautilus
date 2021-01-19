
class ParticipanteModel:

    def __init__(self, listaParticipante: list=None):

        self.eventoId = None
        self.clienteId = None

        if listaParticipante is not None:
            self.fromList(listaParticipante)


    def toDict(self):
        dictParticipantes = {
            'eventoId': self.eventoId,
            'clienteId': self.clienteId
        }
        return dictParticipantes

    def fromDict(self, dictParticipantes):
        self.eventoId = dictParticipantes['eventoId'],
        self.clienteId = dictParticipantes['clienteId'],

    def fromList(self, participante:list):
        self.eventoId = participante[0]
        self.clienteId = participante[1]

    def __repr__(self):
        return f'Participantes(\neventoId: {self.eventoId}, clienteId: {self.clienteId}'