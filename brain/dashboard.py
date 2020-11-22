from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSignal, QPropertyAnimation

from Telas.dashbord import Ui_mwDash
from Telas.dashHome import Ui_wdgHome
from Telas.dashAgenda import Ui_wdgAgenda
from Telas.dashCliente import Ui_wdgCliente

from brain.DAOs.brainUserConfig import *
from brain.telaTeste import telaTeste
from modelos.cliente import Cliente
from modelos.funcoesAuxiliares import *
from brain.DAOs.brainClienteConfig import cadastraCliente
from brain.DAOs.brainUserConfig import criaBanco
import bcrypt
import requests
import json


class brainDashboard(Ui_mwDash, QMainWindow):
    home = pyqtSignal()

    def __init__(self, parent=None):
        super(brainDashboard, self).__init__(parent)

        self.pgHome = Ui_wdgHome(self)
        self.pgAgenda = Ui_wdgAgenda(self)
        self.pgCliente = Ui_wdgCliente(self)

        self.setupUi(self)
        self.enable = False
        self.pbHome.setText('')
        self.pbAgenda.setText('')
        self.cliente = Cliente()

        self.teste = telaTeste()
        self.teste.setupUi(self.teste)
        self.stkDash.addWidget(self.teste)

        self.pbAgenda.clicked.connect(self.funTeste)

        self.pbDash.clicked.connect(self.dash)
        self.pgCliente.pbCadastrar.clicked.connect(lambda: self.trataCadastro(self.cliente))

        self.pbHome.clicked.connect(self.navStkInicial)

        self.leNome.textEdited.connect(lambda: self.defineCampo('nome'))
        self.leSobrenome.textEdited.connect(lambda: self.defineCampo('sobrenome'))
        self.leTel.textEdited.connect(lambda: self.defineCampo('tel'))
        self.leEmail.textEdited.connect(lambda: self.defineCampo('email'))
        self.leCep.textEdited.connect(lambda: self.defineCampo('cep'))
        self.leEnd.textEdited.connect(lambda: self.defineCampo('end'))
        self.leBairro.textEdited.connect(lambda: self.defineCampo('bairro'))
        self.leCompl.textEdited.connect(lambda: self.defineCampo('compl'))

        self.pgCliente.leCep.editingFinished.connect(self.trataCep)
        self.pgCliente.leTel.editingFinished.connect(lambda: self.insereMascara('tel'))

        # ----------------------------------
        self.stkDash.addWidget(self.pgHome)
        self.stkDash.addWidget(self.pgAgenda)
        self.stkDash.addWidget(self.pgCliente)

        self.pbHome.clicked.connect(lambda: self.stkDash.setCurrentIndex(0))
        self.pbAgenda.clicked.connect(lambda: self.stkDash.setCurrentIndex(1))
        self.pbCliente.clicked.connect(lambda: self.stkDash.setCurrentIndex(2))
        # self.pbFuncionario.clicked.connect(lambda: self.stkDash.setCurrentIndex(3))

        criaBanco()

        # ----------------------------------

    def dash(self):

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
            self.cliente.email = self.pgCliente.leEmail.text().capitalize()

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
                print("Informação faltante.")
                return False

        cadastraCliente(self.cliente)

    def trataCep(self, *args):
        if not self.pgCliente.leCep.text() == "":
            self.pgCliente.leCep.setText(mascaraCep(str(self.cliente.cep)))
            response = requests.get(f'http://viacep.com.br/ws/{str(self.cliente.cep)}/json/')
            if response.status_code == 200:
                dictEndereco = json.loads(response.text)
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

    def funTeste(self):
        print('Clicou no botão teste')
        self.stkDash.setCurrentIndex(2)

    def navStkInicial(self):
        self.stkDash.setCurrentIndex(1)


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = brainDashboard()
    ui.show()
    sys.exit(app.exec_())
