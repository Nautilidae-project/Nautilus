from PyQt5.QtCore import QAbstractTableModel, QModelIndex, Qt


class Cliente:

    def __init__(self):
        self.clienteId = None
        self.nomeCliente = None
        self.sobrenomeCliente = None
        self.telefone = None
        self.email = None
        self.cpf = None
        self.endereco = None
        self.complemento = None
        self.cep = None
        self.bairro = None
        self.meioPagamento = None
        self.ativo = 1

    def toDict(self):
        dictUsuario = {
        'clienteId': self.clienteId,
        'nomeCliente': self.nomeCliente,
        'sobrenomeCliente': self.sobrenomeCliente,
        'telefone': self.telefone,
        'email': self.email,
        'cpf': self.cpf,
        'endereco': self.endereco,
        'complemento': self.complemento,
        'cep': self.cep,
        'bairro': self.bairro,
        'meioPagamento': self.meioPagamento,
        'ativo': 1
        }
        return dictUsuario

    def fromDict(self, dictCliente):
        self.clienteId = dictCliente['clienteId'],
        self.nomeCliente = dictCliente['nomeCliente'],
        self.sobrenomeCliente = dictCliente['sobrenomeCliente'],
        self.telefone = dictCliente['telefone'],
        self.email = dictCliente['email'],
        self.cpf = dictCliente['cpf'],
        self.endereco = dictCliente['endereco'],
        self.complemento = dictCliente['complemento'],
        self.cep = dictCliente['cep'],
        self.bairro = dictCliente['bairro'],
        self.meioPagamento = dictCliente['meioPagamento'],
        self.ativo = dictCliente['ativo']

    def __repr__(self):
        return f'Cliente(\nclienteId: {self.clienteId}, nomeCliente: {self.nomeCliente}, sobrenomeCliente: {self.sobrenomeCliente}, \n' \
               f'telefone: {self.telefone}, email: {self.email}, cpf: {self.cpf}, endereco: {self.endereco}, \n' \
               f'complemento: {self.complemento}, cep: {self.cep}, bairro: {self.bairro}, meioPagamento: {self.meioPagamento},\n' \
               f'ativo: {self.ativo}'
