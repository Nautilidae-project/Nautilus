from PyQt5.QtWidgets import QWidget, QRadioButton

from Telas.criaCategoriaWidget import Ui_CategoriaCard
from brain.DAOs.daoCategoria import DaoCategoria
from brain.dashboard.Configuracao.localStyleSheets.ssCardCategoria import colors, botoesStyleSheet, cardCategoriaBg
from modelos.categoriaModel import CategoriaModel
from modelos.efeitosModel import Efeitos


class CategoriaCard(Ui_CategoriaCard, QWidget):

    def __init__(self, parent=None, db=None):
        super(CategoriaCard, self).__init__(parent)
        self.setupUi(self)
        self.db = db
        self.parent = parent
        self.daoCategoria = DaoCategoria(db=db)
        self.novaCategoria = CategoriaModel()
        self.modoEdicao = None

        self.dashBoard = self.parent.parent

        self.pbInserir.clicked.connect(lambda: self.atualizaCardCategoriaLayout('inserir'))
        self.pbExcluir.clicked.connect(lambda: self.atualizaCardCategoriaLayout('excluir'))
        self.pbCancelar.clicked.connect(self.limpaCampos)
        self.leNovaCategoria.textEdited.connect(self.defineNomeCategoria)
        self.pbConfirmar.clicked.connect(lambda: self.verificaCampo() if self.modoEdicao is not None else None)

        self.frColors.hide()
        self.pbConfirmar.hide()
        self.pbCancelar.hide()

        self.leNovaCategoria.setReadOnly(True)

        self.efeitos = Efeitos()
        self.efeitos.shadowCards([self.frTop], color=(63, 63, 63, 90), parentOnly=True)

        self.coloreBotoes()


    def coloreBotoes(self):
        botoes = []
        for botao in self.frColors.children():
            if isinstance(botao, QRadioButton):
                botoes.append(botao)

        for posicao, botao in enumerate(botoes):
            if posicao == 0:
                botao.setChecked(True)
                self.defineCorCategoria(posicao)
            botao.setStyleSheet(botoesStyleSheet(colors[posicao]))
            botao.clicked.connect(lambda state, posicao=posicao: self.defineCorCategoria(posicao))

    def defineNomeCategoria(self, *args):
        self.novaCategoria.nome = args[0].strip().upper()

    def defineCorCategoria(self, posicao, *args):
        self.novaCategoria.cor = colors[posicao]

    def insereCategoria(self):
        self.daoCategoria.insereCategoria(self.novaCategoria)
        self.dashBoard.menssagemSistema("Categoria cadastrada com sucesso")
        self.limpaCampos()

    def verificaCampo(self):
        if self.leNovaCategoria.text().strip() == '':
            self.dashBoard.menssagemSistema("Insira um nome válido")
        else:
            if self.modoEdicao == 'inserir':
                self.insereCategoria()
            elif self.modoEdicao == 'excluir':
                if self.daoCategoria.excluiCategoriaByNome(self.leNovaCategoria.text().strip().upper()):
                    self.dashBoard.menssagemSistema("Categoria excluída com sucesso")
                    self.limpaCampos()
                else:
                    self.dashBoard.menssagemSistema("Categoria não encontrada. Verifique se o nome está correto")

        self.modoEdicao = None

    def atualizaCardCategoriaLayout(self, modo=None):
        if modo is not None:
            self.modoEdicao = modo
            self.pbConfirmar.show()
            self.pbCancelar.show()
            self.leNovaCategoria.setReadOnly(False)
            self.frTopBg.setStyleSheet(cardCategoriaBg(modo=modo))


            if modo == 'inserir':
                self.frColors.show()
                self.lbTitulo.setText("Digite o nome da categoria")
            if modo == 'excluir':
                self.lbTitulo.setText("Excluir categoria")
                self.frColors.hide()

        self.frTopBg.update()


    def limpaCampos(self):
        self.modoEdicao = None
        self.lbTitulo.setText("Crie/Exclua uma categoria")
        self.leNovaCategoria.setReadOnly(True)
        self.leNovaCategoria.setText('')
        self.novaCategoria = CategoriaModel()
        self.pbConfirmar.hide()
        self.pbCancelar.hide()
        self.frColors.hide()
        self.frTopBg.setStyleSheet(cardCategoriaBg())

        for botao in self.frColors.children():
            if isinstance(botao, QRadioButton):
                botao.setChecked(False)