from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSignal
from Telas.cadastro import Ui_mwCadastro
from modelos.usuario import Usuario
from brain.DAOs.UserConfig import *
from brain.funcoesAuxiliares import *
import bcrypt
import requests
import json


class brainCadastro(Ui_mwCadastro, QMainWindow):
    home = pyqtSignal()

    def __init__(self, parent=None):
        super(brainCadastro, self).__init__(parent)
        self.setupUi(self)
        self.pbVoltarLogin.clicked.connect(self.goHome)
        self.home.connect(self.parent().backHome)
        self.timer = QTimer()
        self.timer.timeout.connect(self.escondeSnackbar)

        self.frSnackBarCadastro.hide()

        self.usuario = Usuario()

        self.leNomeUsuario.textEdited.connect(lambda: self.defineCampo('nU'))
        self.leNomeEmpresa.textEdited.connect(lambda: self.defineCampo('nE'))
        self.leNomeFantasia.textEdited.connect(lambda: self.defineCampo('nF'))
        self.leCNPJ.textEdited.connect(lambda: self.defineCampo('cnpj'))
        self.leEmail.textEdited.connect(lambda: self.defineCampo('email'))
        self.leTelefone.textEdited.connect(lambda: self.defineCampo('tel'))
        self.leEndereco.textEdited.connect(lambda: self.defineCampo('end'))
        self.leCEP.textEdited.connect(lambda: self.defineCampo('cep'))
        self.leSenha.textEdited.connect(lambda: self.defineCampo('senha'))
        self.leSenhaConfirma.textEdited.connect(lambda: self.defineCampo('confS'))

        self.cbxEstados.addItems(getEstados())

        self.leCNPJ.editingFinished.connect(lambda: self.insereMascara('cnpj'))
        self.leTelefone.editingFinished.connect(lambda: self.insereMascara('tel'))
        self.leCEP.editingFinished.connect(self.trataCep)

        self.pbFazerCadastro.clicked.connect(self.trataCadastro)
        self.pbContinuaCadastro.clicked.connect(lambda: self.tabs.setCurrentIndex(1))
        self.pbVoltarTab.clicked.connect(lambda: self.tabs.setCurrentIndex(0))

    def goHome(self):
        self.home.emit()

    def defineCampo(self, campo):

        if campo == 'nU':
            self.usuario.nomeUsuario = self.leNomeUsuario.text().capitalize()

        if campo == 'nE':
            self.usuario.nomeEmpresa = self.leNomeEmpresa.text().title()

        if campo == 'nF':
            self.usuario.nomeFantasia = self.leNomeFantasia.text().title()

        if campo == 'cnpj':
            if self.leCNPJ.text().isnumeric():
                self.usuario.cnpj = self.leCNPJ.text()
            else:
                self.apresentaAviso('Digite apenas números')
                print('Erro ao inserir CNPJ')
                self.leCNPJ.setText("")

        if campo == 'email':
            self.usuario.email = self.leEmail.text()

        if campo == 'tel':
            if self.leTelefone.text().isnumeric():
                self.usuario.tel = self.leTelefone.text()
            else:
                self.apresentaAviso('Digite apenas números')
                print('Digite apenas números')
                self.leTelefone.setText("")
                return False

        if campo == 'end':
            self.usuario.endereco = self.leEndereco.text().capitalize()

        if campo == 'cep':
            if self.leCEP.text().isnumeric():
                self.usuario.cep = self.leCEP.text()
            else:
                self.apresentaAviso('Digite apenas números')
                print('Erro ao inserir CEP')
                self.leCEP.setText("")

    def trataCadastro(self):
        wdgLista = [self.leCEP, self.leCNPJ, self.leEmail, self.leSenha, self.leEndereco,
                    self.leTelefone, self.leSenhaConfirma, self.leNomeEmpresa]

        for wdg in wdgLista:
            if wdg.text() == "":
                self.apresentaAviso('Informação faltante')
                print("Informação faltante")
                return False

        if self.leSenha.text() != self.leSenhaConfirma.text():
            self.apresentaAviso('As senhas não coincidem')
            print("As senhas não coincidem")
            return False

        self.usuario.senha = bcrypt.hashpw(self.leSenha.text().encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        if cadastreUsuario(self.usuario):
            print('Usuário cadastrado com sucesso')
            self.goHome()
            return True
        else:
            self.apresentaAviso('Deu merda no cadastro')

    def insereMascara(self, campo):
        if campo == 'cnpj':
            if not self.leCNPJ.text() == "":
                self.leCNPJ.setText(mascaraCNPJ(self.usuario.cnpj))
        if campo == 'tel':
            if not self.leTelefone.text() == "":
                self.leTelefone.setText(mascaraCelular(str(self.usuario.tel)))

    def trataCep(self, *args):

        if not self.leCEP.text() == "":
            self.leCEP.setText(mascaraCep(str(self.usuario.cep)))
            response = requests.get(f'http://viacep.com.br/ws/{str(self.usuario.cep)}/json/')
            if response.status_code == 200:
                dictEndereco = json.loads(response.text)
                self.leEndereco.setText(dictEndereco['logradouro'].title())
                self.leCidade.setText(dictEndereco['localidade'].title())
                self.leBairro.setText(dictEndereco['bairro'].capitalize())
                self.cbxEstados.setCurrentText(getEstados(dictEndereco['uf'])[0])
            else:
                print(f'Falha na conexão - Código de status: {response.status_code}')
                return False

    def apresentaAviso(self, mensagem: str):
        self.lbSnackBarCadastro.setText(mensagem)
        self.frSnackBarCadastro.show()
        self.timer.start(5000)

    def escondeSnackbar(self):
        self.lbSnackBarCadastro.setText('')
        self.frSnackBarCadastro.hide()


