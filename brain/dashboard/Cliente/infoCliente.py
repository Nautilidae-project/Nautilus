import base64

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMessageBox, QGridLayout
from PyQt5.QtWidgets import QWidget, QTableWidgetItem

from Telas.dashCliente import Ui_wdgCliente
from brain.DAOs.UserConfig import DaoConfiguracoes
from brain.DAOs.daoCliente import DaoCliente
from brain.DAOs.daoGrupo import DaoGrupo
from brain.DAOs.daoParticipantes import DaoParticipantes
from brain.dashboard.Cliente.localWidgets.gruposCard import GruposCard
from brain.dashboard.Cliente.relatorio import RelatorioCliente
from brain.dashboard.Sinais import Sinais
from brain.delegates.alinhamento import AlinhamentoCentro, AlinhamentoEsq
from brain.envioDeMensagens import Mensagens
from brain.funcoesAuxiliares import mascaraCelular, macaraFormaPagamento, isTrueBool, isTrueInt
from modelos.clienteModel import Cliente
from modelos.efeitosModel import Efeitos
from modelos.grupoModel import GrupoModelo

from math import ceil

from modelos.participantesModel import ParticipanteModel


class brainCliente(Ui_wdgCliente, QWidget):

    def __init__(self, parent=None):
        super(brainCliente, self).__init__(parent)
        self.setupUi(self)
        self.cliente = Cliente()
        self.daoCliente = DaoCliente()
        self.efeito = Efeitos()
        self.parent = parent
        self.sinais = Sinais()
        self.enviarEmail = Mensagens()
        self.modoEdicao = False
        self.grupoEdicao = GrupoModelo()

        self.pbCancelar.hide()
        self.pbCancelar.clicked.connect(self.sairModoEdicao)

        self.gridBox = QGridLayout()

        self.tblGrupo.clicked.connect(self.selecionaParticipante)

        self.pbExportar.clicked.connect(self.criaRelatorio)
        self.atualizaTabelaGeral()
        self.atualizaTabelaParticipantes()
        self.frInfoCliente.hide()

        # Escondendo as colunas Id das tabelas Geral e Grupo
        self.tblClientes.setColumnHidden(0, True)
        self.tblGrupo.setColumnHidden(0, True)

        self.tblClientes.setItemDelegate(AlinhamentoCentro())
        # self.tblGrupo.setItemDelegate(AlinhamentoEsq())

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
        self.tblClientes.doubleClicked.connect(self.enviarUmEmail)


        # Cards Tela Cliente Informações
        self.cardsInfosCliente()
        # Adicionando Sombra nos cards
        self.efeito.shadowCards([self.leCard1, self.leCard2, self.leCard3, self.leCard4])

        # GRupos/Turmas
        self.cardGrupo = GruposCard()
        self.pbAddGrupo.clicked.connect(lambda: self.criaGrupo() if not self.modoEdicao else self.updateGrupo())

        # Tentando fazer uma lista de cards de grupos
        self.atualizaGruposCards()

    def atualizaGruposCards(self):

        # Se já houverem widgets na tela, reinicia o layout
        if self.gridBox.count():
            self.limpaLayout()

        daoGrupo = DaoGrupo()
        colunas = 1
        linhas = 1

        # Busca no banco de dados todos os grupos criados
        gruposCadastrados = daoGrupo.findAll()

        # Calcula quantas colunas teremos
        if 4 < len(gruposCadastrados) <= 8:
            colunas = 2
        # elif len(gruposCadastrados) > 8 and self.size().width() < 900:
        #     colunas = 2
        elif len(gruposCadastrados) > 8:
            colunas = 3

        linhas = ceil(len(gruposCadastrados)/colunas)

        # Cria um lista contendo o modelo de cada grupo buscado no banco de dados
        gruposModelos = [GrupoModelo(gruposCadastrados[i]) for i in range(0, len(gruposCadastrados))]

        # Cria uma lista contendo os layouts dos cards com as informações dos modelos contidos no gruposModelos
        listaGruposCards = [GruposCard(parent=self, grupo=gruposModelos[i]) for i in range(0, len(gruposCadastrados))]

        # Cria uma matriz das posições nas quais os cards serão apresentados
        posicoes = [(linha, coluna) for linha in range(linhas) for coluna in range(colunas)]

        for card, posicao in zip(listaGruposCards, posicoes):
            self.efeito.shadowCards([card], color=(105, 210, 231, 80))
            self.gridBox.addWidget(card, *posicao)
        self.gridBox.setSpacing(32)

        if self.gridBox.count():
            self.scrollGrupos.setLayout(self.gridBox)

    def enviarUmEmail(self, *args):

        intClienteId = int(self.tblClientes.item(args[0].row(), 0).text())
        listCliente = self.daoCliente.buscaPorId(intClienteId)[0]
        print(f'Id ------->  {listCliente[0]}')
        print(f'Nome ----->  {listCliente[1]}')
        print(f'SobreNome -> {listCliente[2]}')
        print(f'E-mail ----> {listCliente[4]}')

        self.enviarEmail.leId.setText(str(listCliente[0]))
        self.enviarEmail.leNome.setText(f'{listCliente[1]} {listCliente[2]}')
        self.enviarEmail.leEmail.setText(listCliente[4])

        self.enviarEmail.show()

    def cardsInfosCliente(self):
        self.leCard1.setText(
            f"Clientes Ativos:\n{self.daoCliente.contaCliente('ativo=1')}/{self.daoCliente.contaCliente()}")
        self.leCard2.setText(
            f"Clientes Inativos:\n{self.daoCliente.contaCliente('ativo=0')}/{self.daoCliente.contaCliente()}")

    def criaGrupo(self):
        '''
        Função confere se é possível fazer a inserção do grupo no banco de dados e, caso afirmativo:
        - Cria uma lista com os ids dos participantes do grupo;
        - Cria um grupo com o título e a descrição definidas;
        - Pega o id do grupo;
        - Insere a lista de participantes no banco com o id do grupo criado.
        Caso contrário, retorna False e dá a mensagem de erro ao usuário.
        :return: bool
        '''

        if self.confereDadosGrupo():
            listaParticipantes = list()
            daoGrupo = DaoGrupo()
            daoParticipantes = DaoParticipantes()
            dictGrupo = {
                'grupoId': None,
                'titulo': self.leTituloGrupo.text(),
                'descricao': self.leDescricaoGrupo.text(),
                'dataCadastro': None,
                'dataUltAlt': None
            }

            grupoModel = GrupoModelo(dictGrupo=dictGrupo)
            grupoId = daoGrupo.insereGrupo(grupoModel)

            if grupoId is not None:
                for i in range(self.tblGrupo.rowCount()):
                    if self.tblGrupo.item(i, 3).checkState():
                        listaParticipantes.append(ParticipanteModel(
                            listaParticipante=[grupoId, self.tblGrupo.item(i, 0).text()]
                        ))
                daoParticipantes.insereParticipantes(listaParticipantes)

            self.limpaLayout()
            self.limpaCampos()
            self.atualizaGruposCards()
        else:
            print('Não pode cadastrar grupo')

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

    def atualizaTabelaParticipantes(self):
        clientes = self.daoCliente.findAllNomeSobrenome()

        self.tblGrupo.setRowCount(0)

        for rowCount, rowData in enumerate(clientes):
            self.tblGrupo.insertRow(rowCount)

            for columnNumber, data in enumerate(rowData):
                if columnNumber == 3:
                    cbItemParticipante = QTableWidgetItem()
                    cbItemParticipante.setFlags(QtCore.Qt.ItemIsEnabled)
                    cbItemParticipante.setCheckState(QtCore.Qt.Unchecked)
                    self.tblGrupo.setItem(rowCount, columnNumber, QTableWidgetItem(cbItemParticipante))
                else:
                    strItem = QTableWidgetItem(str(data))
                    strItem.setFont(QFont('Ubuntu', pointSize=14, italic=True))
                    self.tblGrupo.setItem(rowCount, columnNumber, strItem)

        self.tblGrupo.resizeColumnsToContents()

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
        self.leTituloGrupo.clear()
        self.leDescricaoGrupo.clear()

        for i in range(0, self.tblClientes.rowCount()):
            if self.tblGrupo.item(i, 3) is not None:
                self.tblGrupo.item(i, 3).setCheckState(QtCore.Qt.Unchecked)

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
        elif args[0] == 2:
            self.atualizaGruposCards()
            self.limpaCampos()
            self.atualizaTabelaParticipantes()

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

    def selecionaParticipante(self, *args):

        # Verifica o estado da chackbox na linha clicada
        estado = self.tblGrupo.item(args[0].row(), 3).checkState()

        if estado == 0:
            self.tblGrupo.item(args[0].row(), 3).setCheckState(QtCore.Qt.Checked)
        else:
            self.tblGrupo.item(args[0].row(), 3).setCheckState(QtCore.Qt.Unchecked)

    def limpaLayout(self):
        '''
        Função que deleta todos os cards de grupos inseridos no gridLayout
        :return:
        '''

        for i in reversed(range(self.gridBox.count())):
            self.gridBox.takeAt(i).widget().setParent(None)

    def confereDadosGrupo(self):
        '''
        Função que confere se, ao tentar criar um grupo, o campo título não está
        vazio e se tem, pelo menos, um cliente selecionado
        :return: bool
        '''

        if len(self.leTituloGrupo.text()) < 1:
            return False

        for i in range(self.tblGrupo.rowCount()):
            if self.tblGrupo.item(i, 3).checkState():
                return True
        return False

    def editarGrupo(self, grupo: GrupoModelo):
        self.modoEdicao = True
        self.grupoEdicao = grupo
        self.pbCancelar.show()
        self.pbAddGrupo.setText('Confirmar')

        daoGrupo = DaoGrupo()
        participantes = daoGrupo.buscaParticipantesGrupo(grupo.grupoId)

        self.leTituloGrupo.setText(grupo.titulo)
        self.leDescricaoGrupo.setText(grupo.descricao)

        for i in range(self.tblGrupo.rowCount()):
            clienteTabelaId = self.tblGrupo.item(i, 0).text()
            for j in participantes:
                clienteCardId = j[0]
                if int(clienteTabelaId) == int(clienteCardId):
                    self.tblGrupo.item(i, 3).setCheckState(QtCore.Qt.Checked)

    def sairModoEdicao(self):
        self.modoEdicao = False
        self.limpaLayout()
        self.limpaCampos()
        self.atualizaGruposCards()
        self.pbCancelar.hide()
        self.pbAddGrupo.setText("Criar grupo")

    def updateGrupo(self):
        self.grupoEdicao.titulo = self.leTituloGrupo.text()
        self.grupoEdicao.descricao = self.leDescricaoGrupo.text()
        listaParticipantes = list()

        daoGrupo = DaoGrupo()
        daoParticipantes = DaoParticipantes()

        daoGrupo.atualizarGrupo(self.grupoEdicao)
        daoParticipantes.deletarParticipantesEvento(self.grupoEdicao.grupoId)

        for i in range(self.tblGrupo.rowCount()):
            if self.tblGrupo.item(i, 3).checkState():
                listaParticipantes.append(ParticipanteModel(
                    listaParticipante=[self.grupoEdicao.grupoId, self.tblGrupo.item(i, 0).text()]
                ))
        daoParticipantes.insereParticipantes(listaParticipantes)

        self.sairModoEdicao()

if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ui = brainCliente()
    ui.show()
    sys.exit(app.exec_())
