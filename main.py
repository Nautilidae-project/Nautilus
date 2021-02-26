import pymysql
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow

from Telas.SplashScreen.splashScreen import Ui_MainWindow
from brain.DAOs.UserConfig import DaoConfiguracoes
from brain.loginPage import LoginPage
from configBD import ConfigDB


class Main(Ui_MainWindow, QMainWindow):

    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)
        self.contador = 0
        self.config = ConfigDB(carregaBanco=True)
        self.db = self.getDB()
        self.daoConfigs = DaoConfiguracoes(self.db)
        self.center()
        self.show()

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progresso)
        self.timer.start(25)

    def progresso(self, add=None):
        if add is None:
            self.contador += 1
        else:
            self.contador += add

        self.pbarSplash.setValue(self.contador)

        if self.contador == 10:
            self.timer.stop()
            self.iniciaBancos()

        if self.contador == 100:
            self.lbInfo.setText('INICIANDO SUBMERSAO...')

    def iniciaBancos(self):

        self.lbInfo.setText('CRIANDO BANCO DO USUÁRIO...')
        if self.daoConfigs.criaTblUsuario():
            self.progresso(add=10)

        self.lbInfo.setText('CRIANDO BANCO DO CLIENTE...')
        if self.daoConfigs.criaTblCliente():
            self.progresso(add=10)

        self.lbInfo.setText('CRIANDO BANCO DO EVENTO...')
        if self.daoConfigs.criaTblEvento():
            self.progresso(add=10)

        self.lbInfo.setText('CRIANDO BANCO DAS GRUPOS...')
        if self.daoConfigs.criaTblGrupo():
            self.progresso(add=10)

        self.lbInfo.setText('CRIANDO BANCO DOS PARTICIPANTES...')
        if self.daoConfigs.criaTblParticipantes():
            self.progresso(add=10)

        self.lbInfo.setText('CRIANDO BANCO DAS CATEGORIAS...')
        if self.daoConfigs.criaTblCategoria():
            self.progresso(add=10)

        self.lbInfo.setText('CRIANDO BANCO DOS ESTADOS...')
        if self.daoConfigs.criaTblEstado():
            self.progresso(add=10)

        self.lbInfo.setText('CRIANDO BANCO DOS PLANOS...')
        if self.daoConfigs.criaTblPlanos():
            self.progresso(add=10)

        self.lbInfo.setText('CRIANDO BANCO DOS PAGAMENTOS...')
        if self.daoConfigs.criaTblPagamentos():
            self.progresso(add=10)

        self.lbInfo.setText('LEMBRANDO DOS ESTADOS DO BRASIL...')
        # Se alguma coisa de errada acontecer com a table a "estados"
        # ele deleta a tabela (DROP TABLE), recria e insere todos os estados de novo
        if not self.daoConfigs.verificaEstados():
            self.lbInfo.setText('EITA! DEU PROBLEMA NA TABELA. VOU ARRUMAR...')
            self.progresso(add=5)
            self.daoConfigs.criaTblEstado()
            self.lbInfo.setText('ESTOU ARRUMANDO RAPIDINHO...')
            if self.daoConfigs.addEstados():
                self.lbInfo.setText('PRONTO! TUDO CERO!')
                self.progresso(add=5)
        else:
            self.progresso(add=10)

        self.iniciaNautilus()

    def iniciaNautilus(self):
        self.close()
        LoginPage(self.db).show()

    def center(self):
        frameGm = self.frameGeometry()
        screen = QtWidgets.QApplication.desktop().screenNumber(QtWidgets.QApplication.desktop().cursor().pos())
        centerPoint = QtWidgets.QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

    def getDB(self):

        return pymysql.connect(
            host=self.config.host,
            user=self.config.user,
            passwd=self.config.passwd,
            db=self.config.banco,
            port=self.config.port
            )


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Main()
    ui.show()
    sys.exit(app.exec_())