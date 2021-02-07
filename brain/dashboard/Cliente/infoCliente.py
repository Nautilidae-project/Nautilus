import base64

import requests
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMessageBox, QGridLayout, QLabel, QPushButton, QListWidget
from PyQt5.QtWidgets import QWidget, QTableWidgetItem

from Telas.dashCliente import Ui_wdgCliente
from brain.DAOs.UserConfig import DaoConfiguracoes
from brain.DAOs.daoCategoria import DaoCategoria
from brain.DAOs.daoCliente import DaoCliente
from brain.DAOs.daoGrupo import DaoGrupo
from brain.DAOs.daoParticipantes import DaoParticipantes
from brain.DAOs.daoUsuario import DaoUsuario
from brain.dashboard.Cliente.localWidgets.gruposCard import GruposCard
from brain.dashboard.Cliente.relatorio import RelatorioCliente
from brain.dashboard.Sinais import Sinais
from brain.delegates.alinhamento import AlinhamentoCentro
from brain.envioDeMensagens import Mensagens
from brain.funcoesAuxiliares import mascaraCelular, macaraFormaPagamento, isTrueBool, isTrueInt, mascaraCep
from modelos.clienteModel import Cliente
from modelos.efeitosModel import Efeitos
from modelos.grupoModel import GrupoModelo

import os

from math import ceil

from modelos.participantesModel import ParticipanteModel


class brainCliente(Ui_wdgCliente, QWidget):

    def __init__(self, parent=None, db=None):
        super(brainCliente, self).__init__(parent)
        self.db = db
        self.setupUi(self)
        self.parent = parent

        # INICIALIZAÇÕES GERAIS =============================================
        self.cliente = Cliente()
        self.daoCliente = DaoCliente(self.db)
        self.efeito = Efeitos()
        self.sinais = Sinais()
        self.enviarEmail = Mensagens()

        # INICIALIZAÇÕES DA ABA "INFORMAÇÕES" ===============================
        self.desativaInfoCampos(True)
        self.atualizaTabelaGeral()
        self.tblClientes.setColumnHidden(0, True)
        self.tblClientes.setItemDelegate(AlinhamentoCentro())

        ## Declaração dos sinais de input
        self.leInfoNome.textEdited.connect(lambda: self.defineInfoCampo('nome'))
        self.leInfoSobrenome.textEdited.connect(lambda: self.defineInfoCampo('sobrenome'))
        self.leInfoTel.textEdited.connect(lambda: self.defineInfoCampo('tel'))
        self.leInfoEmail.textEdited.connect(lambda: self.defineInfoCampo('email'))
        self.leInfoCep.textEdited.connect(lambda: self.defineInfoCampo('cep'))
        self.leInfoCpf.textEdited.connect(lambda: self.defineInfoCampo('cpf'))
        self.leInfoEndereco.textEdited.connect(lambda: self.defineInfoCampo('end'))
        self.leInfoBairro.textEdited.connect(lambda: self.defineInfoCampo('bairro'))
        self.leInfoComplemento.textEdited.connect(lambda: self.defineInfoCampo('compl'))
        self.cbInfoAtivo.clicked.connect(lambda: self.defineInfoCampo('ativo'))

        ## Declaração dos botões
        self.pbConfirmarAtualizacao.clicked.connect(lambda: self.showPopupSimCancela('As atualizações podem ser efetivadas?\nEssa ação não pode ser desfeita.'))
        self.pbEnviarEmail.clicked.connect(self.enviarUmEmail)

        ## Declaração das LineEdit
        self.leCep.editingFinished.connect(self.trataCep)
        self.leTel.editingFinished.connect(lambda: self.insereMascara('tel'))
        self.leSearchCliente.textEdited.connect(self.busca)

        ## Declaração do sinal da tabela de clientes
        self.tblClientes.doubleClicked.connect(self.carregaInfoCliente)

        ## Declaração dos efeitos
        self.efeito.shadowCards([self.frInfoCliente], color=(131, 134, 137, 90), offset=(-7, 4))
        self.efeito.shadowCards([self.leCard1, self.leCard2, self.leCard3, self.leCard4])

        # INICIALIZAÇÕES DA ABA "CADASTRO"    ===============================
        ## Declaração relacionadas à aba de cadastro de clientes
        self.leNome.textEdited.connect(lambda: self.defineCampoCadastro('nome'))
        self.leSobrenome.textEdited.connect(lambda: self.defineCampoCadastro('sobrenome'))
        self.leTel.textEdited.connect(lambda: self.defineCampoCadastro('tel'))
        self.leEmail.textEdited.connect(lambda: self.defineCampoCadastro('email'))
        self.leCep.textEdited.connect(lambda: self.defineCampoCadastro('cep'))
        self.leEnd.textEdited.connect(lambda: self.defineCampoCadastro('end'))
        self.leBairro.textEdited.connect(lambda: self.defineCampoCadastro('bairro'))
        self.leCompl.textEdited.connect(lambda: self.defineCampoCadastro('compl'))
        self.pbCadastrar.clicked.connect(lambda: self.trataCadastro(self.cliente))

        # INICIALIZAÇÕES DA ABA "GRUPOS"      ===============================
        self.colunas = 1
        self.modoEdicao = False
        self.grupoEdicao = GrupoModelo()
        self.gridBox = QGridLayout()
        self.cardGrupo = GruposCard()

        self.atualizaGruposCards()
        self.cardsInfosCliente()
        self.carregaComboBoxes()
        self.cbxOrdenar.currentTextChanged.connect(self.ordenarCards)
        self.atualizaTabelaParticipantes()
        self.carregaFiltroAZ()
        self.efeito.shadowCards([self.tblParticipantes], color=(131, 134, 137, 90))
        self.tblParticipantes.setColumnHidden(0, True)


        ## Declaração do sinal da tabela de Participantes
        self.tblParticipantes.clicked.connect(self.selecionaParticipante)

        ## Declaração dos botões
        self.pbAddGrupo.clicked.connect(lambda: self.criaGrupo() if not self.modoEdicao else self.updateGrupo())
        self.pbRefresh.clicked.connect(lambda: self.filtroAZ(letra=None))
        self.pbCancelar.clicked.connect(self.sairModoEdicao)
        self.pbExportar.clicked.connect(self.criaRelatorio)
        self.pbCancelar.hide()

        self.sinais.sResizeWindow.connect(self.redimensionaTela)

        self.tabsCliente.currentChanged.connect(self.onChange)

    def atualizaGruposCards(self):

        # Se já houverem widgets na tela, reinicia o layout
        if self.gridBox.count():
            self.limpaLayout()

        daoGrupo = DaoGrupo(self.db)
        colunas = 1
        linhas = 1

        widthCard = self.frGruposFormados.sizeHint().width() + 20
        widthScreen = self.window().size().width()

        # Busca no banco de dados todos os grupos criados
        gruposCadastrados = daoGrupo.findAll()


        if len(gruposCadastrados) > 8 and 3*widthCard < widthScreen:
            colunas = 3
        elif len(gruposCadastrados) > 2 and 2*widthCard < widthScreen:
            colunas = 2

        self.colunas = colunas

        linhas = ceil(len(gruposCadastrados)/colunas)

        # Cria um lista contendo o modelo de cada grupo buscado no banco de dados
        gruposModelos = [GrupoModelo(gruposCadastrados[i]) for i in range(0, len(gruposCadastrados))]

        # Cria uma lista contendo os layouts dos cards com as informações dos modelos contidos no gruposModelos
        listaGruposCards = [GruposCard(parent=self, grupo=gruposModelos[i], db=self.db) for i in range(0, len(gruposCadastrados))]

        # Cria uma matriz das posições nas quais os cards serão apresentados
        posicoes = [(linha, coluna) for linha in range(linhas) for coluna in range(colunas)]

        for card, posicao in zip(listaGruposCards, posicoes):
            self.efeito.shadowCards([card], color=(105, 210, 231, 80))
            self.gridBox.addWidget(card, *posicao)
        self.gridBox.setSpacing(32)

        if self.gridBox.count():
            self.scrollGrupos.setLayout(self.gridBox)

    def enviarUmEmail(self, *args):

        if (self.cliente.clienteId is not None):
            print(f'Id ------->  {self.cliente.clienteId}')
            print(f'Nome ----->  {self.cliente.nomeCliente}')
            print(f'SobreNome -> {self.cliente.sobrenomeCliente}')
            print(f'E-mail ----> {self.cliente.email}')

            self.enviarEmail.leId.setText(str(self.cliente.clienteId))
            self.enviarEmail.leNome.setText(f'{self.cliente.nomeCliente} {self.cliente.sobrenomeCliente}')
            self.enviarEmail.leEmail.setText(self.cliente.email)

            self.enviarEmail.show()
        else:
            # TODO: Criar popup que informa esse tipo de mensagem
            self.parent.menssagemSistema('Não foi possível abrir janela de e-mail.')

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

        intLoading = 0
        if self.confereDadosGrupo():
            self.parent.loading(intLoading)
            listaParticipantes = list()
            daoGrupo = DaoGrupo(self.db)
            daoParticipantes = DaoParticipantes(self.db)
            dictGrupo = {
                'grupoId': None,
                'titulo': self.leTituloGrupo.text(),
                'descricao': self.leDescricaoGrupo.toPlainText(),
                'categoria': self.cbxCategoria.currentText(),
                'dataCadastro': None,
                'dataUltAlt': None
            }

            intLoading += 20
            self.parent.loading(intLoading)
            grupoModel = GrupoModelo(dictGrupo=dictGrupo)

            intLoading += 20
            self.parent.loading(intLoading)
            grupoId = daoGrupo.insereGrupo(grupoModel)

            if grupoId is not None:
                intLoading += 20
                self.parent.loading(intLoading)
                for i in range(self.tblParticipantes.rowCount()):
                    if self.tblParticipantes.item(i, 3).checkState():
                        listaParticipantes.append(ParticipanteModel(
                            listaParticipante=[grupoId, self.tblParticipantes.item(i, 0).text()]
                        ))
                daoParticipantes.insereParticipantes(listaParticipantes)

            self.limpaLayout()
            self.limpaCampos()

            intLoading += 20
            self.parent.loading(intLoading)
            self.atualizaGruposCards()

            intLoading += 20
            self.parent.loading(intLoading)
        else:
            self.parent.menssagemSistema('Não foi possível cadastrar grupo. Verifique se o Título foi preenchido e se há ao menos um participante.')

    def defineInfoCampo(self, campo):

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
        
        if len(clientes) == 0:
            self.parent.menssagemSistema('Não há nenhum cliente cadastrcadastrado.')

        self.atualizaTabelaGeral(clientes)

    def atualizaTabelaGeral(self, clientes=None):

        if clientes is None:
            clientes = self.daoCliente.findAll()

        self.tblClientes.setRowCount(0)

        for numLinha, rowData in enumerate(clientes):
            self.tblClientes.insertRow(numLinha)
            for columnNumber, data in enumerate(rowData):

                # columnNumber == 2 coluna dos telefones
                if columnNumber == 3:
                    strItem = QTableWidgetItem(str(mascaraCelular(data)))
                    strItem.setFont(QFont('Ubuntu', pointSize=12, italic=True, weight=25))
                    self.tblClientes.setItem(numLinha, columnNumber, strItem)

                # columnNumber == 3 coluna das formas de pagamento
                elif columnNumber == 4:
                    strItem = QTableWidgetItem(str(macaraFormaPagamento(data)))
                    strItem.setFont(QFont('Ubuntu', pointSize=12, italic=True, weight=25))
                    self.tblClientes.setItem(numLinha, columnNumber, strItem)

                # columnNumber == 4 coluna dos checkbox Ativo
                elif columnNumber == 5:
                    cbItemTbl = QTableWidgetItem()
                    cbItemTbl.setFlags(QtCore.Qt.ItemIsEnabled)
                    cbItemTbl.setText('')

                    if isTrueBool(data):
                        cbItemTbl.setCheckState(QtCore.Qt.Unchecked)
                    else:
                        cbItemTbl.setCheckState(QtCore.Qt.Checked)
                    self.tblClientes.setItem(numLinha, columnNumber, cbItemTbl)
                else:
                    strItem = QTableWidgetItem(str(data))
                    strItem.setFont(QFont('Ubuntu', pointSize=12, italic=True, weight=25))
                    self.tblClientes.setItem(numLinha, columnNumber, strItem)

        self.tblClientes.resizeColumnsToContents()

    def atualizaTabelaParticipantes(self, letra=None):

        if letra is None:
            clientes = self.daoCliente.findAllNomeSobrenome()
        else:
            clientes = self.daoCliente.findAllNomeSobrenome(letra=letra)

        self.tblParticipantes.setRowCount(0)

        for numLinha, conteudoLinha in enumerate(clientes):
            self.tblParticipantes.insertRow(numLinha)

            for columnNumber, data in enumerate(conteudoLinha):
                if columnNumber == 3:
                    cbItemParticipante = QTableWidgetItem()
                    cbItemParticipante.setFlags(QtCore.Qt.ItemIsEnabled)
                    cbItemParticipante.setCheckState(QtCore.Qt.Unchecked)
                    self.tblParticipantes.setItem(numLinha, columnNumber, QTableWidgetItem(cbItemParticipante))
                else:
                    strItem = QTableWidgetItem(str(data))
                    strItem.setFont(QFont('Ubuntu', pointSize=14, italic=True, weight=25))
                    self.tblParticipantes.setItem(numLinha, columnNumber, strItem)

        self.tblParticipantes.resizeColumnsToContents()

    def carregaInfoCliente(self, *args):

        self.desativaInfoCampos(False)
        intClienteId = int(self.tblClientes.item(args[0].row(), 0).text())
        listCliente = self.daoCliente.buscaPorId(intClienteId)[0]
        if len(listCliente) == 0:
            self.parent.mensagemSistema('Não encontramos o cliente procurado.')
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

    def atualizaCliente(self, *args):
        intLoading = 0
        if args[0].text() == "&Yes":
            intLoading += 20
            self.parent.loading(intLoading)
            self.daoCliente.atualizaInfoCliente(self.cliente)

            intLoading += 20
            self.parent.loading(intLoading)
            self.limpaCampos()

            intLoading += 20
            self.parent.loading(intLoading)

            intLoading += 20
            self.parent.loading(intLoading)
            self.desativaInfoCampos(True)

            intLoading += 20
            self.parent.loading(intLoading)
            self.cliente = Cliente()
            self.parent.menssagemSistema('Cliente cadastrado com sucesso!')
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
        self.leNome.clear()
        self.leSobrenome.clear()
        self.leCompl.clear()
        self.leTel.clear()
        self.leEnd.clear()
        self.leBairro.clear()
        self.leEmail.clear()
        self.leCep.clear()

        for i in range(0, self.tblParticipantes.rowCount()):
            if self.tblParticipantes.item(i, 3) is not None:
                self.tblParticipantes.item(i, 3).setCheckState(QtCore.Qt.Unchecked)

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
            # self.atualizaGruposCards()
            self.atualizaTabelaParticipantes()

    def criaRelatorio(self):
        # Busca o usuário ativo
        # TODO: Criar um método melhor para encontrar usuário ativo
        daoUsuario = DaoUsuario(self.db)
        usuarioAtivo = daoUsuario.buscaUsuarioAtivo()

        # Cria relatório
        # TODO: Criar método para escolher, por meio do browser, o local de salvamento do arquivo e o nome
        relatorio = RelatorioCliente(nomeArquivo='Relatório', usuario=usuarioAtivo, db=self.db)
        relatorio.exportaRelatorio()
        # relatorio.exportaRelatorio(tipo='excel')

    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
        self.sinais.sResizeWindow.emit()

    def selecionaParticipante(self, *args):

        # Verifica o estado da chackbox na linha clicada
        estado = self.tblParticipantes.item(args[0].row(), 3).checkState()

        if estado == 0:
            self.tblParticipantes.item(args[0].row(), 3).setCheckState(QtCore.Qt.Checked)
        else:
            self.tblParticipantes.item(args[0].row(), 3).setCheckState(QtCore.Qt.Unchecked)

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

        for i in range(self.tblParticipantes.rowCount()):
            if self.tblParticipantes.item(i, 3).checkState():
                return True
        return False

    def editarGrupo(self, grupo: GrupoModelo):
        self.modoEdicao = True
        self.grupoEdicao = grupo
        self.pbCancelar.show()
        self.pbAddGrupo.setText('Confirmar')

        daoGrupo = DaoGrupo(self.db)
        participantes = daoGrupo.buscaParticipantesGrupo(grupo.grupoId)

        self.leTituloGrupo.setText(grupo.titulo)
        self.leDescricaoGrupo.setText(grupo.descricao)

        for i in range(self.tblParticipantes.rowCount()):
            clienteTabelaId = self.tblParticipantes.item(i, 0).text()
            for j in participantes:
                clienteCardId = j[0]
                if int(clienteTabelaId) == int(clienteCardId):
                    self.tblParticipantes.item(i, 3).setCheckState(QtCore.Qt.Checked)

    def sairModoEdicao(self):
        self.modoEdicao = False
        self.limpaLayout()
        self.limpaCampos()
        self.atualizaGruposCards()
        self.pbCancelar.hide()
        self.pbAddGrupo.setText("Criar grupo")
        self.parent.menssagemSistema('Grupo editado com sucesso.')

    def updateGrupo(self):
        self.grupoEdicao.titulo = self.leTituloGrupo.text()
        self.grupoEdicao.descricao = self.leDescricaoGrupo.toPlainText()
        listaParticipantes = list()

        daoGrupo = DaoGrupo(self.db)
        daoParticipantes = DaoParticipantes(self.db)

        daoGrupo.atualizarGrupo(self.grupoEdicao)
        daoParticipantes.deletarParticipantesEvento(self.grupoEdicao.grupoId)

        for i in range(self.tblParticipantes.rowCount()):
            if self.tblParticipantes.item(i, 3).checkState():
                listaParticipantes.append(ParticipanteModel(
                    listaParticipante=[self.grupoEdicao.grupoId, self.tblParticipantes.item(i, 0).text()]
                ))
        daoParticipantes.insereParticipantes(listaParticipantes)

        self.sairModoEdicao()

    def carregaComboBoxes(self):

        daoCategorias = DaoCategoria(self.db)
        listTupleCategorias = daoCategorias.getAll()
        ordenar = ['DATA', 'CATEGORIA', 'A-Z', 'Z-A']

        self.cbxOrdenar.addItems(ordenar)

        listCategorias = [categoria[0] for categoria in listTupleCategorias]

        self.cbxCategoria.addItems(listCategorias)

    def ordenarCards(self, *args):
        listaCards = list()
        cardsSorted = None

        for i in range(self.gridBox.count()):
            listaCards.append(self.gridBox.itemAt(i).widget())

        if args[0] == 'CATEGORIA':
            cardsSorted = sorted(listaCards, key=lambda card: card.grupo.categoria)
        elif args[0] == 'DATA':
            cardsSorted = sorted(listaCards, key=lambda card: card.grupo.grupoId)
        elif args[0] == 'A-Z':
            cardsSorted = sorted(listaCards, key=lambda card: card.grupo.titulo)
        elif args[0] == 'Z-A':
            cardsSorted = reversed(sorted(listaCards, key=lambda card: card.grupo.titulo))

        if cardsSorted is not None:
            self.limpaLayout()
            for i in cardsSorted:
                self.gridBox.addWidget(i)
            self.scrollGrupos.setLayout(self.gridBox)

    def redimensionaTela(self):
        sizeCard = GruposCard().sizeHint().width() + 20
        sizeArea = self.frGruposFormados.size().width()

        if 3*sizeCard < sizeArea:
            colunas = 3
        elif 2*sizeCard < sizeArea:
            colunas = 2
        else:
            colunas = 1

        if colunas == self.colunas:
            return True
        else:
            self.colunas = colunas

            listaCards = list()

            for i in range(self.gridBox.count()):
                listaCards.append(self.gridBox.itemAt(i).widget())

            self.limpaLayout()

            linhas = ceil(len(listaCards) / colunas)

            posicoes = [(linha, coluna) for linha in range(linhas) for coluna in range(colunas)]

            for card, posicao in zip(listaCards, posicoes):
                self.efeito.shadowCards([card], color=(105, 210, 231, 80))
                self.gridBox.addWidget(card, *posicao)
            self.gridBox.setSpacing(32)

            if self.gridBox.count():
                self.scrollGrupos.setLayout(self.gridBox)

    def carregaFiltroAZ(self):
        listAlfabeto = list(' ABCDEFGHIJKLMNOPQRSTUVWXYZ ')
        pbStrStyleSheet = """
            QPushButton {
                background-color: transparent;
                border: 0px;
                font-size: 12px;
                font-family: Ubuntu;
            }
            QPushButton::hover{
                border: 0px solid;
                border-radius: 10px;
                background-color: #838689;
                color: #fff;
                font-size: 16px;
                font-family: Ubuntu;  
            }"""
        lbStyleSheet = """
        QLabel {
            background-color: transparent;
            border: 0px;
            }
            """

        for i in range(0, len(listAlfabeto)):

            if i == 0 or i == len(listAlfabeto)-1:
                label = QLabel(' ')
                label.setFixedSize(20, 20)
                label.setStyleSheet(lbStyleSheet)
                self.hlAlfabeto.addWidget(label)
            else:
                button = QPushButton(listAlfabeto[i])
                button.setFixedSize(20, 20)
                button.setStyleSheet(pbStrStyleSheet)
                button.clicked.connect(lambda state, i=i: self.filtroAZ(i))
                self.hlAlfabeto.addWidget(button)

    def filtroAZ(self, letra, *args, **kwargs):
        listAlfabeto = list(' ABCDEFGHIJKLMNOPQRSTUVWXYZ ')

        if letra is None:
            for linha in range(self.tblParticipantes.rowCount()):
                self.tblParticipantes.showRow(linha)
        else:
            for linha in range(self.tblParticipantes.rowCount()):
                if self.tblParticipantes.item(linha, 1).text()[0] != listAlfabeto[letra]:
                    self.tblParticipantes.hideRow(linha)
                else:
                    self.tblParticipantes.showRow(linha)

    def desativaInfoCampos(self, ativa: bool):
        self.leInfoNome.setReadOnly(ativa)
        self.leInfoSobrenome.setReadOnly(ativa)
        self.leInfoBairro.setReadOnly(ativa)
        self.leInfoCep.setReadOnly(ativa)
        self.leInfoComplemento.setReadOnly(ativa)
        self.leInfoCpf.setReadOnly(ativa)
        self.leInfoEmail.setReadOnly(ativa)
        self.leInfoEndereco.setReadOnly(ativa)
        self.leInfoTel.setReadOnly(ativa)

    def defineCampoCadastro(self, campo):

        if campo == 'nome':
            self.cliente.nomeCliente = self.leNome.text().capitalize()

        if campo == 'sobrenome':
            self.cliente.sobrenomeCliente = self.leSobrenome.text().title()

        if campo == 'tel':
            if self.leTel.text().isnumeric():
                self.cliente.telefone = self.leTel.text()
            else:
                print('Digite apenas números')
                self.leTel.setText("")
                return False

        if campo == 'email':
            self.cliente.email = self.leEmail.text().lower()

        if campo == 'cep':
            if self.leCep.text().isnumeric():
                self.cliente.cep = self.leCep.text()
            else:
                print('Digite apenas números')
                self.leCep.setText("")

        if campo == 'end':
            self.cliente.endereco = self.leEnd.text().capitalize()

        if campo == 'bairro':
            self.cliente.bairro = self.leBairro.text().capitalize()

        if campo == 'compl':
            self.cliente.complemento = self.leCompl.text().capitalize()

    def trataCadastro(self, cliente):
        intLoading = 0

        self.parent.loading(intLoading)
        wdgLista = [cliente.nomeCliente, cliente.sobrenomeCliente, cliente.email, cliente.endereco, cliente.cep]
        for wdg in wdgLista:
            intLoading += 10
            self.parent.loading(intLoading)
            if wdg == "":
                print("Informação faltante - <trataCadastro>")
                self.parent.loading(100)
                self.parent.menssagemSistema('Não foi possível cadastrar cliente. Alguma informação faltante.')
                return False

        intLoading += 10
        self.parent.loading(intLoading)

        # ----- Váriaveis de envio de e-mail -----
        self.titulo = "Testando no Codigo"
        self.msgCadastro = f"""Cliente Cadastrado Com Sucesso

        --------------------- Dados Cadastrados ---------------------
        Nome: {self.cliente.nomeCliente} {self.cliente.sobrenomeCliente}
        E-mail: {self.cliente.email}
        Senha: senha
        Cep: {self.cliente.cep}
        Enredeço: {self.cliente.endereco}
        Bairro: {self.cliente.bairro}
        Complemento: {self.cliente.complemento}
"""
        # ----------------------------------------

        self.parent.loading(70)
        self.daoCliente.cadastraCliente(self.cliente)
        self.parent.loading(100)
        self.limpaCampos()
        self.parent.menssagemSistema('Cliente cadastrado com sucesso.')
        # enviaEmail(self.titulo, self.msgCadastro, self.leEmail.text())

    def trataCep(self, *args):
        if not self.leCep.text() == "":
            self.leCep.setText(mascaraCep(str(self.cliente.cep)))
            response = requests.get(f'http://viacep.com.br/ws/{str(self.cliente.cep)}/json/')

            # Ao enviar um cep que não é encontrado, ele retorna o status 200, mas com o json {'erro': True}
            if response.status_code == 200 and "erro" not in response.json():
                dictEndereco = response.json()
                self.leEnd.setText(dictEndereco['logradouro'].title())
                self.cliente.endereco = dictEndereco['logradouro'].title()
                # self.leCidade.setText(dictEndereco['localidade'])
                self.leBairro.setText(dictEndereco['bairro'].title())
                self.cliente.bairro = dictEndereco['bairro'].title()
            else:
                self.parent.menssagemSistema('Não foi possível encontrar o CEP.')
                print(f'Falha na conexão - Código de status: {response.status_code}')
                return False

    def insereMascara(self, campo: str):
        if campo == 'tel':
            if not self.leTel.text() == "":
                self.leTel.setText(mascaraCelular(str(self.cliente.telefone)))


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ui = brainCliente()
    ui.show()
    sys.exit(app.exec_())
