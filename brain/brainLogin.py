from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow
from Telas.arquivos_front_end.login import Ui_mwLogin
from brain.brainCadastro import brainCadastro
from brain.DAOs.brainUserConfig import *

class brainLogin(Ui_mwLogin, QMainWindow):

    def __init__(self):
        import Telas.arquivos_front_end.image_rc
        super(brainLogin, self).__init__()
        self.setupUi(self)
        self.telaCadastro = brainCadastro(self)
        self.stkLogin.addWidget(self.telaCadastro)
        self.pbCadastro.clicked.connect(self.navigate)
        self.pbLogin.clicked.connect(self.trataLogin)

    def navigate(self):
        self.stkLogin.setCurrentIndex(1)

    def backHome(self):
        self.stkLogin.setCurrentIndex(0)

    def trataLogin(self):
        strNomeUsuario = self.leUsuario.text()
        if not strNomeUsuario:
            print("Digite um usuário")
            return False
        if not buscaBanco(strNomeUsuario):
            print("Não foi encontrado nenhum usuário com o nome cadastrado")
        else:
            print('Banco de dados encontrado')


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = brainLogin()
    ui.show()
    sys.exit(app.exec_())