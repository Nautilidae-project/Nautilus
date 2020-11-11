from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow
from Telas.arquivos_front_end.login import Ui_mwLogin
from brain.brainCadastro import brainCadastro
from brain.brainDashboard import brainDashboard
from brain.DAOs.brainUserConfig import *


class brainLogin(Ui_mwLogin, QMainWindow):

    def __init__(self):
        import Telas.arquivos_front_end.image_rc
        super(brainLogin, self).__init__()
        criaBanco()
        addEstados()

        self.setupUi(self)

        # Iniciando a tela cadastro e inserindo-a no stkWidget
        self.telaCadastro = brainCadastro(self)
        self.stkLogin.addWidget(self.telaCadastro)

        # Iniciando a dashboard e inserindo-o no StkWidget
        self.dashboard = brainDashboard(self)
        self.stkLogin.addWidget(self.dashboard)

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
