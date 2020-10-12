from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSignal
from Telas.cadastro import Ui_mwCadastro
from modelos.usuario import Usuario
from brain.DAOs.brainUserConfig import *
import bcrypt


class brainCadastro(Ui_mwCadastro, QMainWindow):
    home = pyqtSignal()

    def __init__(self, parent=None):
        super(Ui_mwCadastro, self).__init__(parent)
        self.setupUi(self)
        self.pbVoltarLogin.clicked.connect(self.goHome)
        self.home.connect(self.parent().backHome)

        self.usuario = Usuario()

        self.leNomeEmpresa.textChanged.connect(lambda: self.defineCampo('nE'))
        self.leNomeFantasia.textChanged.connect(lambda: self.defineCampo('nF'))
        self.leCNPJ.textChanged.connect(lambda: self.defineCampo('cnpj'))
        self.leEmail.textChanged.connect(lambda: self.defineCampo('email'))
        self.leTelefone.textChanged.connect(lambda: self.defineCampo('tel'))
        self.leEndereco.textChanged.connect(lambda: self.defineCampo('end'))
        self.leCEP.textChanged.connect(lambda: self.defineCampo('cep'))
        self.leSenha.textChanged.connect(lambda: self.defineCampo('senha'))
        self.leSenha_2.textChanged.connect(lambda: self.defineCampo('confS'))

        self.pbFazerCadastro.clicked.connect(self.trataCadastro)

    def goHome(self):
        self.home.emit()

    def defineCampo(self, campo):
        if campo == 'nE':
            self.usuario.nomeEmpresa = self.leNomeEmpresa.text()
        if campo == 'nF':
            self.usuario.nomeFantasia = self.leNomeFantasia.text()
        if campo == 'cnpj':
            self.usuario.cnpj = self.leCNPJ.text()
        if campo == 'email':
            self.usuario.email = self.leEmail.text()
        if campo == 'tel':
            try:
                self.usuario.tel = int(self.leTelefone.text())
            except:
                return False
        if campo == 'end':
            self.usuario.endereco = self.leEndereco.text()
        if campo == 'cep':
            try:
                self.usuario.cep = int(self.leCEP.text())
            except:
                return False
            
    def trataCadastro(self):
        wdgLista = [self.leCEP, self.leCNPJ, self.leEmail, self.leSenha, self.leEndereco, self.leTelefone, self.leSenha_2,
                    self.leNomeEmpresa]
        for wdg in wdgLista:
            if wdg.text() == "":
                print("Informação faltante.")
                return False
        if self.leSenha.text() != self.leSenha_2.text():
            print("As senhas não coincidem")
            return False

        self.usuario.senha = bcrypt.hashpw(self.leSenha.text().encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        if cadastreUsuario(self.usuario):
            print('Usuário cadastrado com sucesso')
        else:
            print('Deu merda no cadastro')
