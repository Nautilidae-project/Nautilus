
class Participante:

    def __init__(self):
        self.eventoId = None
        self.clienteId = None

    def toDict(self):
        dictParticipantes = {
            'eventoId': self.eventoId,
            'clienteId': self.clienteId
        }
        return dictParticipantes

    def fromDict(self, dictParticipantes):
        self.eventoId = dictParticipantes['eventoId'],
        self.clienteId = dictParticipantes['clienteId'],

    def __repr__(self):
        return f'Participantes(\neventoId: {self.eventoId}, clienteId: {self.clienteId}'