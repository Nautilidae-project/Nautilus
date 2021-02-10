from PyQt5.QtWidgets import QWidget, QRadioButton

from Telas.criaCategoriaWidget import Ui_CategoriaCard
from brain.DAOs.daoCategoria import DaoCategoria
from brain.dashboard.Configuracao.localStyleSheets.CardCategoria import colors, botoesStyleSheet
from modelos.categoriaModel import CategoriaModel
from modelos.efeitosModel import Efeitos


class CategoriaCard(Ui_CategoriaCard, QWidget):

    def __init__(self, parent=None, db=None):
        super(CategoriaCard, self).__init__(parent)
        self.setupUi(self)
        self.db = db
        self.daoCategoria = DaoCategoria(db=db)
        self.novaCategoria = CategoriaModel()

        self.pbConfirmar.clicked.connect(self.insereCategoria)
        self.leNovaCategoria.textEdited.connect(lambda: self.defineCategoria(None, campo='nome'))

        self.efeitos = Efeitos()
        self.efeitos.shadowCards([self.frTop], color=(63, 63, 63, 90), parentOnly=True)

        self.coloreBotoes()

    def coloreBotoes(self):
        botoes = []
        for botao in self.frColors.children():
            if isinstance(botao, QRadioButton):
                botoes.append(botao)

        for posicao, botao in enumerate(botoes):
            botao.setStyleSheet(botoesStyleSheet(colors[posicao]))
            botao.clicked.connect(lambda state, posicao=posicao: self.defineCategoria(posicao, campo='cor'))

    def insereCategoria(self, posicao, campo=None):
        if campo == 'nome':
            self.novaCategoria.nome = self.
        elif campo == 'cor':

