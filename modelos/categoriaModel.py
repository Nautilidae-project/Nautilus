from PyQt5.QtCore import QAbstractTableModel, QModelIndex, Qt


class CategoriaModel:

    def __init__(self):
        self.categoriaId = None
        self.nome = None
        self.cor = None


    def toDict(self):
        dictCategoria = {
        'categoriaId': self.categoriaId,
        'nome': self.nome,
        'cor': self.cor
        }
        return dictCategoria

    def fromDict(self, dictCategoria):
        self.categoriaId = dictCategoria['categoriaId']
        self.nome = dictCategoria['nome']
        self.cor = dictCategoria['cor']

    def __repr__(self):
        return f'Categoria(\ncategoriaId: {self.categoriaId}, nome: {self.nome}, cor: {self.cor}\n)'
