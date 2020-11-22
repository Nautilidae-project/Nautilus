from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow
from Telas.login import Ui_mwLogin
from brain.dashboard import brainDashboard
from brain.brainCadastro import brainCadastro
from brain.DAOs.brainUserConfig import *


class brainLogin(Ui_mwLogin, QMainWindow):

    def __init__(self):
        import Telas.image_rc
        super(brainLogin, self).__init__()
        criaBanco()
        addEstados()

        self.setupUi(self)

        # Iniciando a tela cadastro e inserindo-a no stkWidget
        self.telaCadastro = brainCadastro(self)
        self.stkLogin.addWidget(self.telaCadastro)

        # Iniciando a tela cadastro e inserindo-a no stkWidget
        self.telaDashboard = brainDashboard(self)
        self.stkLogin.addWidget(self.telaDashboard)

        self.pbCadastro.clicked.connect(self.navigate)
        self.pbLogin.clicked.connect(self.trataLogin)
        self.lbSnackBarLogin.hide()
        self.pbFechaSnackBarLogin.hide()

        self.pbFechaSnackBarLogin.clicked.connect(lambda: (self.lbSnackBarLogin.hide(), self.pbFechaSnackBarLogin.hide()))
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
            self.snackBar("Digite um usuário")
            return False
        if not buscaUsuario(strNomeUsuario):
            print("Não foi encontrado nenhum usuário com o nome cadastrado")
            self.snackBar("Usuário Não Cadastrado")
        else:
            if confereSenha(strNomeUsuario, self.leSenha.text()):
                self.snackBar('Usuário(a) confirmado(a)!')
                print('Usuário(a) confirmado(a)!')
                self.stkLogin.setCurrentIndex(2)
            else:
                print('Senha inválida!')
                self.snackBar("Senha Inválida")

    def snackBar(self, mensagem):
        self.lbSnackBarLogin.setText(mensagem)
        self.lbSnackBarLogin.show()
        self.pbFechaSnackBarLogin.show()


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = brainLogin()
    ui.show()
    sys.exit(app.exec_())
