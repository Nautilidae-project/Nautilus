from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow
from Telas.login import Ui_mwLogin
from brain.DAOs.daoUsuario import DaoUsuario
from brain.cadastraUser import brainCadastro
from brain.dashboard.mainDashboard import mainDashboard
from brain.DAOs.UserConfig import *


class LoginPage(Ui_mwLogin, QMainWindow):

    def __init__(self, db):
        super(LoginPage, self).__init__()
        self.db = db
        self.userId = None

        # Inicia Daos=============================================================
        # self.daoConfig = DaoConfiguracoes(self.db)
        self.daoUsuario = DaoUsuario(self.db)

        self.setupUi(self)
        self.center()

        # Ao abrir a janela, dá o focus, coloca ela em primeiro plano e maximizada
        self.showMaximized()
        self.raise_()
        self.activateWindow()


        # Iniciando a tela cadastro e inserindo-a no stkWidget
        self.telaCadastro = brainCadastro(self, db=db)
        self.stkLogin.addWidget(self.telaCadastro)

        # Iniciando a tela cadastro e inserindo-a no stkWidget
        # self.telaDashboard = mainDashboard(self, db=db)
        # self.stkLogin.addWidget(self.telaDashboard)

        self.telaDashboard = None


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
        self.limpaCampos()
        self.stkLogin.setCurrentIndex(0)

    def trataLogin(self):
        strNomeUsuario = self.leUsuario.text()
        if strNomeUsuario == "":
            print("Digite um usuário")
            self.snackBar("Digite um usuário")
            return False
        if not self.daoUsuario.verificaUsuario(strNomeUsuario):
            print("Não foi encontrado nenhum usuário com o nome cadastrado")
            self.snackBar("Usuário Não Cadastrado")
        else:
            self.userId = self.daoUsuario.confereSenha(strNomeUsuario, self.leSenha.text())
            if self.userId is not None:
                self.snackBar('Usuário(a) confirmado(a)!')
                self.carregaDashboard()
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

    def carregaDashboard(self):
        usuario = self.daoUsuario.carregaUsrAtual(id=self.userId)
        self.telaDashboard = mainDashboard(self, db=self.db, usuario=usuario)
        self.stkLogin.addWidget(self.telaDashboard)

    def limpaCampos(self):
        print('IMPLEMENTAR LIMPAR CAMPOS')


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = LoginPage()
    ui.show()
    sys.exit(app.exec_())
