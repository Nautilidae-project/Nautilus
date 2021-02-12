from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSignal
from Telas.cadastro import Ui_mwCadastro
from brain.DAOs.daoUsuario import DaoUsuario
from modelos.usuarioModel import UsuarioModel
from brain.DAOs.UserConfig import *
from brain.funcoesAuxiliares import *
import bcrypt
import requests
import json


class brainCadastro(Ui_mwCadastro, QMainWindow):
    home = pyqtSignal()

    def __init__(self, parent=None, db=None):
        super(brainCadastro, self).__init__(parent)
        self.setupUi(self)
        self.db = db

        self.daoConfig = DaoConfiguracoes(self.db)
        self.daoUsuario = DaoUsuario(self.db)
        self.pbVoltarLogin.clicked.connect(self.goHome)
        self.home.connect(self.parent().backHome)
        self.timer = QTimer()
        self.timer.timeout.connect(self.escondeSnackbar)

        self.frSnackBarCadastro.hide()

        self.usuarioModel = UsuarioModel()

        self.leNomeUsuario.textEdited.connect(lambda: self.defineCampo('nU'))
        self.leNomeEmpresa.textEdited.connect(lambda: self.defineCampo('nE'))
        self.leNomeFantasia.textEdited.connect(lambda: self.defineCampo('nF'))
        self.leCNPJ.textEdited.connect(lambda: self.defineCampo('cnpj'))
        self.leEmail.textEdited.connect(lambda: self.defineCampo('email'))
        self.leTelefone.textEdited.connect(lambda: self.defineCampo('tel'))
        self.leEndereco.textEdited.connect(lambda: self.defineCampo('end'))
        self.leCidade.textEdited.connect(lambda: self.defineCampo('cid'))
        self.leCEP.textEdited.connect(lambda: self.defineCampo('cep'))
        self.leSenha.textEdited.connect(lambda: self.defineCampo('senha'))
        self.leBairro.textEdited.connect(lambda: self.defineCampo('bairro'))
        self.leComplemento.textEdited.connect(lambda: self.defineCampo('comp'))
        self.leSenhaConfirma.textEdited.connect(lambda: self.defineCampo('confS'))

        self.cbxEstados.addItems(self.daoConfig.getEstados())

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
            self.usuarioModel.nomeUsuario = self.leNomeUsuario.text().capitalize()

        if campo == 'nE':
            self.usuarioModel.nomeEmpresa = self.leNomeEmpresa.text().title()

        if campo == 'nF':
            self.usuarioModel.nomeFantasia = self.leNomeFantasia.text().title()

        if campo == 'cnpj':
            if self.leCNPJ.text().isnumeric():
                self.usuarioModel.cnpj = self.leCNPJ.text()
            else:
                self.apresentaAviso('Digite apenas números')
                print('Erro ao inserir CNPJ')
                self.leCNPJ.setText("")

        if campo == 'email':
            self.usuarioModel.email = self.leEmail.text()

        if campo == 'tel':
            if self.leTelefone.text().isnumeric():
                self.usuarioModel.tel = self.leTelefone.text()
            else:
                self.apresentaAviso('Digite apenas números')
                print('Digite apenas números')
                self.leTelefone.setText("")
                return False

        if campo == 'end':
            self.usuarioModel.endereco = self.leEndereco.text().capitalize()

        if campo == 'cid':
            self.usuarioModel.cidade = self.leCidade.text().title()

        if campo == 'comp':
            self.usuarioModel.complemento = self.leComplemento.text().title()

        if campo == 'cep':
            if self.leCEP.text().isnumeric():
                self.usuarioModel.cep = self.leCEP.text()
            else:
                self.apresentaAviso('Digite apenas números')
                print('Erro ao inserir CEP')
                self.leCEP.setText("")

        if campo == 'bairro':
            self.usuarioModel.bairro = self.leBairro.text().title()


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

        self.usuarioModel.senha = bcrypt.hashpw(self.leSenha.text().encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        if self.daoUsuario.cadastreUsuario(self.usuarioModel):
            print('Usuário cadastrado com sucesso')
            self.goHome()
            return True
        else:
            self.apresentaAviso('Deu merda no cadastro')

    def insereMascara(self, campo):
        if campo == 'cnpj':
            if not self.leCNPJ.text() == "":
                self.leCNPJ.setText(mascaraCNPJ(self.usuarioModel.cnpj))
        if campo == 'tel':
            if not self.leTelefone.text() == "":
                self.leTelefone.setText(mascaraCelular(str(self.usuarioModel.tel)))

    def trataCep(self, *args):

        if not self.leCEP.text() == "":
            self.leCEP.setText(mascaraCep(str(self.usuarioModel.cep)))
            response = requests.get(f'http://viacep.com.br/ws/{str(self.usuarioModel.cep)}/json/')
            if response.status_code == 200:
                dictEndereco = json.loads(response.text)
                self.leEndereco.setText(dictEndereco['logradouro'].title())
                self.usuarioModel.endereco = dictEndereco['logradouro'].title()

                self.leCidade.setText(dictEndereco['localidade'].title())
                self.usuarioModel.cidade = dictEndereco['localidade'].title()

                self.leBairro.setText(dictEndereco['bairro'].capitalize())
                self.usuarioModel.bairro = dictEndereco['bairro'].capitalize()

                self.cbxEstados.setCurrentText(self.daoConfig.getEstados(dictEndereco['uf'])[0])
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


