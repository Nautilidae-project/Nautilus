import base64

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox, QGridLayout
from PyQt5.QtWidgets import QWidget, QTableWidgetItem

from Telas.dashCliente import Ui_wdgCliente
from brain.DAOs.UserConfig import DaoConfiguracoes
from brain.DAOs.daoCliente import DaoCliente
from brain.DAOs.daoGrupo import DaoGrupo
from brain.dashboard.Cliente.localWidgets.gruposCard import GruposCard
from brain.dashboard.Cliente.relatorio import RelatorioCliente
from brain.dashboard.Sinais import Sinais
from brain.delegates.alinhamento import AlinhamentoDelegate
from brain.funcoesAuxiliares import mascaraCelular, macaraFormaPagamento, isTrueBool, isTrueInt, formasPagamento
from modelos.clienteModel import Cliente
from modelos.efeitosModel import Efeitos
from modelos.grupoModel import GrupoModelo


class brainCliente(Ui_wdgCliente, QWidget):

    def __init__(self, parent=None):
        super(brainCliente, self).__init__(parent)
        self.setupUi(self)
        self.cliente = Cliente()
        self.daoCliente = DaoCliente()
        self.efeito = Efeitos()
        self.parent = parent
        self.sinais = Sinais()

        self.sinais.sResizeWindow.connect(self.resizedWindow)

        self.vBox = QGridLayout()

        self.pbExportar.clicked.connect(self.criaRelatorio)
        self.atualizaTabelaGeral()
        self.atualizaTabelaGrupos()
        self.frInfoCliente.hide()

        # Escondendo as colunas Id das tabelas Geral e Grupo
        self.tblClientes.setColumnHidden(0, True)
        self.tblGrupo.setColumnHidden(0, True)

        self.tblClientes.setItemDelegate(AlinhamentoDelegate())

        self.pbConfirmarAtualizacao.clicked.connect(
            lambda: self.showPopupSimCancela('As atualizações podem ser efetivadas?\nEssa ação não pode ser desfeita.'))
        self.leSearchCliente.textEdited.connect(lambda: self.busca())

        self.tblClientes.doubleClicked.connect(self.carregaInfoCliente)

        self.leInfoNome.textEdited.connect(lambda: self.defineCampo('nome'))
        self.leInfoSobrenome.textEdited.connect(lambda: self.defineCampo('sobrenome'))
        self.leInfoTel.textEdited.connect(lambda: self.defineCampo('tel'))
        self.leInfoEmail.textEdited.connect(lambda: self.defineCampo('email'))
        self.leInfoCep.textEdited.connect(lambda: self.defineCampo('cep'))
        self.leInfoCpf.textEdited.connect(lambda: self.defineCampo('cpf'))
        self.leInfoEndereco.textEdited.connect(lambda: self.defineCampo('end'))
        self.leInfoBairro.textEdited.connect(lambda: self.defineCampo('bairro'))
        self.leInfoComplemento.textEdited.connect(lambda: self.defineCampo('compl'))
        self.cbInfoAtivo.clicked.connect(lambda: self.defineCampo('ativo'))

        self.tabsCliente.currentChanged.connect(self.onChange)

        # Cards Tela Cliente Informações
        self.cardsInfosCliente()
        # Adicionando Sombra nos cards
        self.efeito.shadowCards([self.leCard1, self.leCard2, self.leCard3, self.leCard4])

        # GRupos/Turmas
        self.cardGrupo = GruposCard()
        self.pbAddGrupo.clicked.connect(lambda: self.addGrupo())

        # Tentando fazer uma lista de cards de grupos
        self.adicionaGruposCards()

    def adicionaGruposCards(self):
        daoGrupo = DaoGrupo()
        colunas = 1

        # Busca no banco de dados todos os grupos criados
        gruposCadastrados = daoGrupo.findAll()

        # Calcula quantas colunas teremos
        if 4 < len(gruposCadastrados) <= 8:
            colunas = 2
        elif len(gruposCadastrados) > 8 and self.size().width() < 900:
            colunas = 2
        elif len(gruposCadastrados) > 8 and self.size().width() > 900:
            colunas = 3

        # Cria um lista contendo o modelo de cada grupo buscado no banco de dados
        gruposModelos = [GrupoModelo(gruposCadastrados[i]) for i in range(0, len(gruposCadastrados))]

        # Cria uma lista contendo os layouts dos cards com as informações dos modelos contidos no gruposModelos
        listaGruposCards = [GruposCard(parent=self, grupo=gruposModelos[i]) for i in range(0, len(gruposCadastrados))]

        # Cria uma matriz das posições nas quais os cards serão apresentados
        posicoes = [(linha, coluna) for linha in range(int(len(listaGruposCards) / colunas)) for coluna in range(colunas)]

        for card, posicao in zip(listaGruposCards, posicoes):
            self.vBox.addWidget(card, *posicao)

        self.scrollGrupos.setLayout(self.vBox)

    def cardsInfosCliente(self):
        self.leCard1.setText(
            f"Clientes Ativos:\n{self.daoCliente.contaCliente('ativo=1')}/{self.daoCliente.contaCliente()}")
        self.leCard2.setText(
            f"Clientes Inativos:\n{self.daoCliente.contaCliente('ativo=0')}/{self.daoCliente.contaCliente()}")

    def addGrupo(self):
        self.gridLayout_6.addWidget(self.cardGrupo, 0, 0)
        print("Chamando")

    def defineCampo(self, campo):

        if campo == 'nome':
            self.cliente.nomeCliente = self.leInfoNome.text().capitalize()

        if campo == 'sobrenome':
            self.cliente.sobrenomeCliente = self.leInfoSobrenome.text().title()

        if campo == 'tel':
            if self.leInfoTel.text().isnumeric():
                self.cliente.telefone = self.leInfoTel.text()
            else:
                print('Digite apenas números')
                self.leInfoTel.setText("")
                return False

        if campo == 'email':
            self.cliente.email = self.leInfoEmail.text().lower()

        if campo == 'cpf':
            if self.leInfoCpf.text().isnumeric():
                self.cliente.cpf = self.leInfoCpf.text()

        if campo == 'cep':
            if self.leInfoCep.text().isnumeric():
                self.cliente.cep = self.leInfoCep.text()
            else:
                print('Digite apenas números no cep')
                self.leInfoCep.setText("")

        if campo == 'end':
            self.cliente.endereco = self.leInfoEndereco.text().capitalize()

        if campo == 'bairro':
            self.cliente.bairro = self.leInfoBairro.text().capitalize()

        if campo == 'compl':
            self.cliente.complemento = self.leInfoComplemento.text().capitalize()

        if campo == 'ativo':
            self.cliente.ativo = self.cbInfoAtivo.isChecked()

        self.atualizaTabelaGeral()

    def busca(self):
        clientes = self.daoCliente.buscaCliente(self.leSearchCliente.text())

        self.atualizaTabelaGeral(clientes)

    def atualizaTabelaGeral(self, clientes=None):

        if clientes is None:
            clientes = self.daoCliente.findAll()

        self.tblClientes.setRowCount(0)

        for rowCount, rowData in enumerate(clientes):
            self.tblClientes.insertRow(rowCount)
            for columnNumber, data in enumerate(rowData):

                # columnNumber == 2 coluna dos telefones
                if columnNumber == 2:
                    self.tblClientes.setItem(rowCount, columnNumber, QTableWidgetItem(str(mascaraCelular(data))))

                # columnNumber == 3 coluna das formas de pagamento
                elif columnNumber == 3:
                    self.tblClientes.setItem(rowCount, columnNumber, QTableWidgetItem(str(macaraFormaPagamento(data))))

                # columnNumber == 4 coluna dos checkbox Ativo
                elif columnNumber == 4:
                    cbItemTbl = QTableWidgetItem()
                    cbItemTbl.setFlags(QtCore.Qt.ItemIsEnabled)
                    cbItemTbl.setText('')

                    if isTrueBool(data):
                        cbItemTbl.setCheckState(QtCore.Qt.Unchecked)
                    else:
                        cbItemTbl.setCheckState(QtCore.Qt.Checked)
                    self.tblClientes.setItem(rowCount, columnNumber, cbItemTbl)
                else:
                    self.tblClientes.setItem(rowCount, columnNumber, QTableWidgetItem(str(data)))

        self.tblClientes.resizeColumnsToContents()

    def atualizaTabelaGrupos(self):
        clientes = self.daoCliente.findAll(all='ns')

        self.tblGrupo.setRowCount(0)
        print(clientes)

        for rowCount, rowData in enumerate(clientes):
            self.tblGrupo.insertRow(rowCount)

            for columnNumber, data in enumerate(rowData):
                self.tblClientes.setItem(rowCount, columnNumber, QTableWidgetItem(str(data)))




        self.tblClientes.resizeColumnsToContents()

    def carregaInfoCliente(self, *args):

        intClienteId = int(self.tblClientes.item(args[0].row(), 0).text())
        listCliente = self.daoCliente.buscaPorId(intClienteId)[0]
        if len(listCliente) == 0:
            print('Não encontrei o cliente')
        # elif len(listCliente) > 1:
        #     print('O SELECT trouxe mais do que um cliente')
        else:
            self.cliente.clienteId = listCliente[0]
            self.cliente.nomeCliente = listCliente[1]
            self.cliente.sobrenomeCliente = listCliente[2]
            self.cliente.telefone = listCliente[3]
            self.cliente.email = listCliente[4]
            self.cliente.cpf = listCliente[5]
            self.cliente.endereco = listCliente[6]
            self.cliente.complemento = listCliente[7]
            self.cliente.cep = listCliente[8]
            self.cliente.bairro = listCliente[9]
            self.cliente.meioPagamento = listCliente[10]
            self.cliente.ativo = isTrueInt(listCliente)

            if self.cliente.nomeCliente != 'None':
                self.leInfoNome.setText(self.cliente.nomeCliente)

            if self.cliente.sobrenomeCliente != 'None':
                self.leInfoSobrenome.setText(self.cliente.sobrenomeCliente)

            if self.cliente.telefone != 'None':
                self.leInfoTel.setText(self.cliente.telefone)

            if self.cliente.email != 'None':
                self.leInfoEmail.setText(self.cliente.email)

            if self.cliente.cpf != 'None':
                self.leInfoCpf.setText(self.cliente.cpf)

            if self.cliente.endereco != 'None':
                self.leInfoEndereco.setText(self.cliente.endereco)

            if self.cliente.complemento != 'None':
                self.leInfoComplemento.setText(self.cliente.complemento)

            if self.cliente.cep != 'None':
                self.leInfoCep.setText(self.cliente.cep)

            if self.cliente.bairro != 'None':
                self.leInfoBairro.setText(self.cliente.bairro)

            # self.leInfoMeioPag.setText(formasPagamento[self.cliente.meioPagamento])
            self.cbInfoAtivo.setChecked(self.cliente.ativo)

            self.frInfoCliente.show()

    def atualizaCliente(self, *args):
        if args[0].text() == "&Yes":
            self.daoCliente.atualizaInfoCliente(self.cliente)
            self.limpaCampos()
        self.frInfoCliente.hide()
        self.atualizaTabelaGeral()

    def animationInfo(self):
        pass

    def limpaCampos(self):
        self.leInfoNome.clear()
        self.leInfoSobrenome.clear()
        self.leInfoCep.clear()
        self.leInfoTel.clear()
        self.leInfoCpf.clear()
        self.leInfoComplemento.clear()
        self.leInfoBairro.clear()
        self.leInfoEndereco.clear()
        self.leInfoEmail.clear()

    def showPopupSimCancela(self, mensagem, titulo='Atenção!'):
        dialogPopup = QMessageBox()
        dialogPopup.setWindowTitle(titulo)
        dialogPopup.setText(mensagem)
        dialogPopup.setIcon(QMessageBox.Warning)
        dialogPopup.setStandardButtons(QMessageBox.Cancel | QMessageBox.Yes)

        dialogPopup.buttonClicked.connect(self.atualizaCliente)
        dialogPopup.buttonClicked.connect(self.cardsInfosCliente)
        close = dialogPopup.exec_()

    def onChange(self, *args):
        if args[0] == 0:
            self.cardsInfosCliente()
            self.atualizaTabelaGeral()
            self.limpaCampos()

    def criaRelatorio(self):
        # Busca o usuário ativo
        # TODO: Criar um método melhor para encontrar usuário ativo
        config = DaoConfiguracoes()
        usuarioAtivo = config.buscaUsuarioAtivo()

        # Cria relatório
        # TODO: Criar método para escolher, por meio do browser, o local de salvamento do arquivo e o nome
        relatorio = RelatorioCliente(nomeArquivo='Relatório', usuario=usuarioAtivo)
        relatorio.exportaRelatorio()
        # relatorio.exportaRelatorio(tipo='excel')

    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
        self.sinais.sResizeWindow.emit()

    def resizedWindow(self):
        # self.adicionaGruposCards()
        pass


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ui = brainCliente()
    ui.show()
    sys.exit(app.exec_())
