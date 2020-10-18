from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSignal
from Telas.arquivos_front_end.cadastro import Ui_mwCadastro
from modelos.usuario import Usuario
from brain.DAOs.brainUserConfig import getEstados


class brainCadastro(Ui_mwCadastro, QMainWindow):
    home = pyqtSignal()

    def __init__(self, parent=None):
        super(Ui_mwCadastro, self).__init__(parent)
        self.setupUi(self)
        self.pbVoltarLogin.clicked.connect(self.goHome)
        self.home.connect(self.parent().backHome)

        self.usuario = Usuario()

        self.leNomeEmpresa.textChanged.connect(self.exibe)

        self.cmbEstados.addItems(getEstados())

    def goHome(self):
        self.home.emit()

    def exibe(self, texto):
        print(texto)
