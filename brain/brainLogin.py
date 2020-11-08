from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow
from Telas.arquivos_front_end.login import Ui_mwLogin
from brain.brainCadastro import brainCadastro
from brain.DAOs.brainUserConfig import *


class brainLogin(Ui_mwLogin, QMainWindow):

    def __init__(self):
        import Telas.arquivos_front_end.image_rc
        super(brainLogin, self).__init__()
        criaBanco()
        addEstados()

        self.setupUi(self)
        self.telaCadastro = brainCadastro(self)
        self.stkLogin.addWidget(self.telaCadastro)
        self.pbCadastro.clicked.connect(self.navigate)
        self.pbLogin.clicked.connect(self.trataLogin)
        self.lbPopUp.hide()
        self.pbFechaPopUp.hide()

        self.pbFechaPopUp.clicked.connect(lambda: (self.lbPopUp.hide(), self.pbFechaPopUp.hide()))
        self.leUsuario.returnPressed.connect(lambda: self.trataLogin())
        self.leSenha.returnPressed.connect(lambda: self.trataLogin())

    def navigate(self):
        self.stkLogin.setCurrentIndex(1)

    def backHome(self):
        self.stkLogin.setCurrentIndex(0)

    def trataLogin(self):
        strNomeUsuario = self.leUsuario.text()
        if strNomeUsuario == "":
            print("Digite um usuário")
            self.popUp("Digite um usuário")
            return False
        if not buscaUsuario(strNomeUsuario):
            print("Não foi encontrado nenhum usuário com o nome cadastrado")
            self.popUp("Usuário Não Cadastrado")
        else:
            if confereSenha(strNomeUsuario, self.leSenha.text()):
                self.popUp('Usuário(a) confirmado(a)!')
                print('Usuário(a) confirmado(a)!')
            else:
                print('Senha inválida!')
                self.popUp("Senha Inválida")

    def popUp(self, mensagem):
        self.lbPopUp.setText(mensagem)
        self.lbPopUp.show()
        self.pbFechaPopUp.show()


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = brainLogin()
    ui.show()
    sys.exit(app.exec_())
