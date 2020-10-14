from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSignal
from Telas.arquivos_front_end.cadastro import Ui_mwCadastro
from modelos.usuario import Usuario
from brain.DAOs.brainUserConfig import *
from modelos.funcoesAuxiliares import *
import bcrypt


class brainCadastro(Ui_mwCadastro, QMainWindow):
    home = pyqtSignal()

    def __init__(self, parent=None):
        super(Ui_mwCadastro, self).__init__(parent)
        self.setupUi(self)
        self.pbVoltarLogin.clicked.connect(self.goHome)
        self.home.connect(self.parent().backHome)

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

        self.leCNPJ.editingFinished.connect(lambda: self.insereMascara('cnpj'))
        self.leTelefone.editingFinished.connect(lambda: self.insereMascara('tel'))
        self.leCEP.editingFinished.connect(lambda: self.insereMascara('cep'))

        self.pbFazerCadastro.clicked.connect(self.trataCadastro)

    def goHome(self):
        self.home.emit()

    def defineCampo(self, campo):

        if campo == 'nU':
            self.usuario.nomeUsuario = self.leNomeUsuario.text()

        if campo == 'nE':
            self.usuario.nomeEmpresa = self.leNomeEmpresa.text()

        if campo == 'nF':
            self.usuario.nomeFantasia = self.leNomeFantasia.text()

        if campo == 'cnpj':
            if self.leCNPJ.text().isnumeric():
                self.usuario.cnpj = self.leCNPJ.text()
            else:
                print('Digite apenas números')
                self.leCNPJ.setText("")

        if campo == 'email':
            self.usuario.email = self.leEmail.text()

        if campo == 'tel':
            if self.leTelefone.text().isnumeric():
                self.usuario.tel = int(self.leTelefone.text())
            else:
                print('Digite apenas números')
                self.leTelefone.setText("")
                return False

        if campo == 'end':
            self.usuario.endereco = self.leEndereco.text()

        if campo == 'cep':
            if self.leCEP.text().isnumeric():
                self.usuario.cep = self.leCEP.text()
            else:
                print('Digite apenas números')
                self.leCEP.setText("")


            
    def trataCadastro(self):
        wdgLista = [self.leCEP, self.leCNPJ, self.leEmail, self.leSenha, self.leEndereco, self.leTelefone, self.leSenhaConfirma,
                    self.leNomeEmpresa]
        for wdg in wdgLista:
            if wdg.text() == "":
                print("Informação faltante.")
                return False
        if self.leSenha.text() != self.leSenhaConfirma.text():
            print("As senhas não coincidem")
            return False

        self.usuario.senha = bcrypt.hashpw(self.leSenha.text().encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        if cadastreUsuario(self.usuario):
            print('Usuário cadastrado com sucesso')
            self.goHome()
            return True
        else:
            print('Deu merda no cadastro')

    def insereMascara(self, campo):
        if campo == 'cnpj':
            if not self.leCNPJ.text() == "":
                self.leCNPJ.setText(mascaraCNPJ(self.usuario.cnpj))
        if campo == 'cep':
            if not self.leCEP.text() == "":
                self.leCEP.setText(mascaraCep(str(self.usuario.cep)))
        if campo == 'tel':
            if not self.leTelefone.text() == "":
                self.leTelefone.setText(mascaraCelular(str(self.usuario.tel)))
