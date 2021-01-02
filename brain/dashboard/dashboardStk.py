from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QPropertyAnimation

from Telas.dashboard import Ui_mwDash
from brain.dashboard.Agenda.agendaPage import AgendaPage
from brain.dashboard.Configuracao.configPage import ConfigPage
from brain.dashboard.Financeiro.financeiroPage import FinanceiroPage
from brain.dashboard.Home.homePage import HomePage
from brain.dashboard.Cliente.infoCliente import brainCliente
from brain.dashboard.Sinais import Sinais

from modelos.clienteModel import Cliente
from brain.funcoesAuxiliares import *

from brain.DAOs.daoCliente import DaoCliente
import requests


class brainDashboard(Ui_mwDash, QMainWindow):

    def __init__(self, parent=None):
        super(brainDashboard, self).__init__(parent)
        self.parent = parent

        # Inicializando as telas e stacks
        self.pgHome = HomePage(self)
        self.pgAgenda = AgendaPage(self)
        self.pgCliente = brainCliente(self)
        self.pgFinanceiro = FinanceiroPage(self)
        self.pgConfig = ConfigPage(self)
        self.sinais = Sinais()

        self.sinais.sBackLoginPage.connect(self.logoff)

        self.daoCliente = DaoCliente()

        self.setupUi(self)
        self.enable = False
        self.pbHome.setText('')
        self.pbAgenda.setText('')
        self.cliente = Cliente()

        self.pbDash.clicked.connect(self.animationDash)
        self.pgCliente.pbCadastrar.clicked.connect(lambda: self.trataCadastro(self.cliente))

        self.pgCliente.leNome.textEdited.connect(lambda: self.defineCampo('nome'))
        self.pgCliente.leSobrenome.textEdited.connect(lambda: self.defineCampo('sobrenome'))
        self.pgCliente.leTel.textEdited.connect(lambda: self.defineCampo('tel'))
        self.pgCliente.leEmail.textEdited.connect(lambda: self.defineCampo('email'))
        self.pgCliente.leCep.textEdited.connect(lambda: self.defineCampo('cep'))
        self.pgCliente.leEnd.textEdited.connect(lambda: self.defineCampo('end'))
        self.pgCliente.leBairro.textEdited.connect(lambda: self.defineCampo('bairro'))
        self.pgCliente.leCompl.textEdited.connect(lambda: self.defineCampo('compl'))

        self.pgCliente.leCep.editingFinished.connect(self.trataCep)
        self.pgCliente.leTel.editingFinished.connect(lambda: self.insereMascara('tel'))

        # Adição das páginas na sacked Widget
        self.stkDash.addWidget(self.pgHome)
        self.stkDash.addWidget(self.pgAgenda)
        self.stkDash.addWidget(self.pgCliente)
        self.stkDash.addWidget(self.pgFinanceiro)
        self.stkDash.addWidget(self.pgConfig)

        # Definindo funcionalidades dos cliques dos botões
        self.pbHome.clicked.connect(lambda: self.stkDash.setCurrentIndex(0))
        self.pbAgenda.clicked.connect(lambda: self.stkDash.setCurrentIndex(1))
        self.pbCliente.clicked.connect(lambda: self.stkDash.setCurrentIndex(2))
        self.pbFinanceiro.clicked.connect(lambda: self.stkDash.setCurrentIndex(3))
        self.pbConfig.clicked.connect(lambda: self.stkDash.setCurrentIndex(4))
        self.pbSairDash.clicked.connect(lambda: self.sairApp())

        # ----------------------------------

    def animationDash(self):

        if self.enable:
            multBy = 1/1.4
            self.pbHome.setText('')
            self.pbAgenda.setText('')
        else:
            multBy = 1.4
            self.pbHome.setText('Home')
            self.pbAgenda.setText('Agenda')

        widthStart = self.frMenu.width()

        self.animSideBar = QPropertyAnimation(self.frMenu, b"minimumWidth")
        self.animSideBar.setDuration(200)
        self.animSideBar.setStartValue(widthStart)
        self.animSideBar.setEndValue(widthStart*multBy)
        self.animSideBar.start()

        self.enable = not self.enable

    def defineCampo(self, campo):

        if campo == 'nome':
            self.cliente.nomeCliente = self.pgCliente.leNome.text().capitalize()

        if campo == 'sobrenome':
            self.cliente.sobrenomeCliente = self.pgCliente.leSobrenome.text().title()

        if campo == 'tel':
            if self.pgCliente.leTel.text().isnumeric():
                self.cliente.telefone = self.pgCliente.leTel.text()
            else:
                print('Digite apenas números')
                self.pgCliente.leTel.setText("")
                return False

        if campo == 'email':
            self.cliente.email = self.pgCliente.leEmail.text().lower()

        if campo == 'cep':
            if self.pgCliente.leCep.text().isnumeric():
                self.cliente.cep = self.pgCliente.leCep.text()
            else:
                print('Digite apenas números')
                self.pgCliente.leCep.setText("")

        if campo == 'end':
            self.cliente.endereco = self.pgCliente.leEnd.text().capitalize()

        if campo == 'bairro':
            self.cliente.bairro = self.pgCliente.leBairro.text().capitalize()

        if campo == 'compl':
            self.cliente.complemento = self.pgCliente.leCompl.text().capitalize()

    def trataCadastro(self, cliente):
        wdgLista = [cliente.nomeCliente, cliente.sobrenomeCliente, cliente.email, cliente.endereco, cliente.cep]
        for wdg in wdgLista:
            if wdg == "":
                print("Informação faltante - <trataCadastro>")
                return False

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

        self.daoCliente.cadastraCliente(self.cliente)
        self.limpaCampos()
        # enviaEmail(self.titulo, self.msgCadastro, self.pgCliente.leEmail.text())

    def trataCep(self, *args):
        if not self.pgCliente.leCep.text() == "":
            self.pgCliente.leCep.setText(mascaraCep(str(self.cliente.cep)))
            response = requests.get(f'http://viacep.com.br/ws/{str(self.cliente.cep)}/json/')

            # Ao enviar um cep que não é encontrado, ele retorna o status 200, mas com o json {'erro': True}
            if response.status_code == 200 and "erro" not in response.json():
                dictEndereco = response.json()
                self.pgCliente.leEnd.setText(dictEndereco['logradouro'].title())
                self.cliente.endereco = dictEndereco['logradouro'].title()
                # self.leCidade.setText(dictEndereco['localidade'])
                self.pgCliente.leBairro.setText(dictEndereco['bairro'].title())
                self.cliente.bairro = dictEndereco['bairro'].title()
            else:
                print(f'Falha na conexão - Código de status: {response.status_code}')
                return False

    def insereMascara(self, campo: str):
        if campo == 'tel':
            if not self.pgCliente.leTel.text() == "":
                self.pgCliente.leTel.setText(mascaraCelular(str(self.cliente.telefone)))

    def limpaCampos(self):
        self.pgCliente.leNome.clear()
        self.pgCliente.leSobrenome.clear()
        self.pgCliente.leCompl.clear()
        self.pgCliente.leTel.clear()
        self.pgCliente.leEnd.clear()
        self.pgCliente.leBairro.clear()
        self.pgCliente.leEmail.clear()
        self.pgCliente.leCep.clear()

    def sairApp(self):
        print(self.parent)
        self.sinais.sBackLoginPage.emit()

    def logoff(self):
        self.parent.backHome()


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = brainDashboard()
    ui.show()
    sys.exit(app.exec_())