from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow
from Telas.login import Ui_mwLogin
from brain.cadastraUser import brainCadastro
from brain.dashboard.dashboardStk import brainDashboard
from brain.DAOs.UserConfig import *


class LoginPage(Ui_mwLogin, QMainWindow):

    def __init__(self):
        super(LoginPage, self).__init__()
        self.daoConfig = DaoConfiguracoes()

        self.setupUi(self)
        self.center()

        # Ao abrir a janela, dá o focus e coloca ela em primeiro plano
        self.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)

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

        self.leUsuario.setFocus()
        # self.leUsuario.setText('renan')
        # self.leSenha.setText('123456')
        self.leUsuario.setText('israeldev')
        self.leSenha.setText('123')

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
        if not self.daoConfig.verificaUsuario(strNomeUsuario):
            print("Não foi encontrado nenhum usuário com o nome cadastrado")
            self.snackBar("Usuário Não Cadastrado")
        else:
            if self.daoConfig.confereSenha(strNomeUsuario, self.leSenha.text()):
                self.snackBar('Usuário(a) confirmado(a)!')
                self.stkLogin.setCurrentIndex(2)
            else:
                print('Senha inválida!')
                self.snackBar("Senha Inválida")

    def snackBar(self, mensagem):
        self.lbSnackBarLogin.setText(mensagem)
        self.lbSnackBarLogin.show()
        self.pbFechaSnackBarLogin.show()

    def center(self):
        frameGm = self.frameGeometry()
        screen = QtWidgets.QApplication.desktop().screenNumber(QtWidgets.QApplication.desktop().cursor().pos())
        centerPoint = QtWidgets.QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = LoginPage()
    ui.show()
    sys.exit(app.exec_())
