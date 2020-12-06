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
        self.ativo: dictCliente['ativo']

    def __repr__(self):
        return f'Cliente(\nclienteId: {self.clienteId}, nomeCliente: {self.nomeCliente}, sobrenomeCliente: {self.sobrenomeCliente}, \n' \
               f'telefone: {self.telefone}, email: {self.email}, cpf: {self.cpf}, endereco: {self.endereco}, \n' \
               f'complemento: {self.complemento}, cep: {self.cep}, bairro: {self.bairro}, meioPagamento: {self.meioPagamento},\n' \
               f'ativo: {self.ativo}'


class ClientTableModel(QAbstractTableModel):

    def __init__(self, colunas=None, dados=None):
        super(ClientTableModel, self).__init__()
        self.dados = dados
        self.colunas = colunas
        self.qtdColunas = len(colunas)
        self.qtdLinhas = len(dados)

        print(f'self.dados: {self.dados}')
        print(f'qtdLinhas: {self.qtdLinhas}')
        print(f'self.colunas: {self.colunas}')
        print(f'qtdColunas: {self.qtdColunas}')

    def rowCount(self, parent=QModelIndex()) -> int:
        return self.qtdLinhas

    def columnCount(self, parent=QModelIndex()) -> int:
        return self.qtdColunas

    def headerData(self, section: int, orientation: Qt.Orientation, role: int = ...):
        print('Entrou no headerData')
        if role != Qt.DisplayRole:
            return None

        if orientation == Qt.Horizontal:
            # print(f'Colunas: {self.colunas[section]}')
            return self.colunas[section]
        else:
            return section

    def data(self, index: QModelIndex, role=Qt.DisplayRole):
        column = index.column()
        row = index.row()

        if role == Qt.DisplayRole:
            # print(self.dados[row][column])
            return self.dados[row][column]
        elif role == Qt.TextAlignmentRole:
            return Qt.AlignCenter
        else:
            return None