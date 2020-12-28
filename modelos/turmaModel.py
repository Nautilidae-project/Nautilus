
class Turma:

    def __init__(self):
        self.turmaId = None
        self.clienteId = None
        self.titulo = None
        self.descricao = None

    def toDict(self):
        dictTurma = {
            'turmaId': self.turmaId,
            'clienteId': self.clienteId,
            'titulo': self.titulo,
            'descricao': self.descricao
        }
        return dictTurma

    def fromDict(self, dictTurma):
        self.turmaId = dictTurma['turmaId'],
        self.clienteId = dictTurma['clienteId'],
        self.titulo = dictTurma['titulo'],
        self.descricao = dictTurma['descricao']

    def __repr__(self):
        return f'Turma(\nturmaId: {self.turmaId}, clienteId: {self.clienteId}, titulo: {self.titulo}, \n descricao: {self.descricao}'