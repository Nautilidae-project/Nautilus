from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QPropertyAnimation
from PyQt5 import QtCore

from Telas.dashboard import Ui_mwDash
from brain.dashboard.Agenda.agendaPage import AgendaPage
from brain.dashboard.Configuracao.configPage import ConfigPage
from brain.dashboard.Financeiro.financeiroPage import FinanceiroPage
from brain.dashboard.Home.homePage import HomePage
from brain.dashboard.Cliente.infoCliente import brainCliente
from brain.dashboard.Sinais import Sinais

import asyncio

from brain.DAOs.daoCliente import DaoCliente
import requests


class mainDashboard(Ui_mwDash, QMainWindow):

    def __init__(self, parent=None, db=None):
        super(mainDashboard, self).__init__(parent)
        self.parent = parent
        self.setupUi(self)
        self.db = db

        # Inicializando as telas e stacks =================================================
        self.pgHome = HomePage(self, db=db)
        self.pgAgenda = AgendaPage(self, db=db)
        self.pgCliente = brainCliente(self, db=db)
        self.pgFinanceiro = FinanceiroPage(self, db=db)
        self.pgConfig = ConfigPage(self, db=db)

        # Iniciando as telas com async
        # loopIniciandoTelas = asyncio.get_event_loop()
        # tarefas = [loopIniciandoTelas.create_task(self.carregaLayout('home')),
        #            loopIniciandoTelas.create_task(self.carregaLayout('agenda')),
        #            loopIniciandoTelas.create_task(self.carregaLayout('cliente')),
        #            loopIniciandoTelas.create_task(self.carregaLayout('financeiro')),
        #            loopIniciandoTelas.create_task(self.carregaLayout('configuracoes'))]
        #
        # esperaTarefas = asyncio.wait(tarefas)
        # loopIniciandoTelas.run_until_complete(esperaTarefas)
        #
        # loopIniciandoTelas.close()

        # Iniciaizando sinais =============================================================
        self.sinais = Sinais()
        self.sinais.sBackLoginPage.connect(self.logoff)
        self.sinais.sSistemInfo.connect(self.informacaoSistema)
        self.sinais.sSistemLoading.connect(self.sistemLoading)

        # Iniciaizando ProgressBar ========================================================
        self.pbarProgress.hide()

        # Iniciaizando DAOs ===============================================================
        self.daoCliente = DaoCliente(db)

        # Adição das páginas na sacked Widget =============================================
        self.stkDash.addWidget(self.pgHome)
        self.stkDash.addWidget(self.pgAgenda)
        self.stkDash.addWidget(self.pgCliente)
        self.stkDash.addWidget(self.pgFinanceiro)
        self.stkDash.addWidget(self.pgConfig)

        # Definindo funcionalidades dos cliques dos botões =================================
        self.pbHome.clicked.connect(lambda: self.stkDash.setCurrentIndex(0))
        self.pbAgenda.clicked.connect(lambda: self.stkDash.setCurrentIndex(1))
        self.pbCliente.clicked.connect(lambda: self.stkDash.setCurrentIndex(2))
        self.pbFinanceiro.clicked.connect(lambda: self.stkDash.setCurrentIndex(3))
        self.pbConfig.clicked.connect(lambda: self.stkDash.setCurrentIndex(4))
        self.pbSairDash.clicked.connect(lambda: self.sairApp())
        self.pbHome.setText('')
        self.pbAgenda.setText('')
        self.pbDash.clicked.connect(self.animationDash)

        # Inicializando QTimer ===============================================================
        self.timerMsg = QtCore.QTimer()
        self.timerLoading = QtCore.QTimer()
        self.timerMsg.timeout.connect(lambda: self.informacaoSistema('', desliga=True))
        self.timerLoading.timeout.connect(lambda: self.pbarProgress.hide())

        # Inicializando outras variaveis =====================================================
        self.enable = False

    def animationDash(self):

        if self.enable:
            multBy = 1/1.4
            self.pbHome.setText('')
            self.pbAgenda.setText('')
        else:
            multBy = 1.4
            self.pbHome.setText('Home')
            self.pbAgenda.setText('Agenda')

        widthStart = self.frMenu.width()

        self.animSideBar = QPropertyAnimation(self.frMenu, b"minimumWidth")
        self.animSideBar.setDuration(200)
        self.animSideBar.setStartValue(widthStart)
        self.animSideBar.setEndValue(widthStart*multBy)
        self.animSideBar.start()

        self.enable = not self.enable

    def sairApp(self):
        self.sinais.sBackLoginPage.emit()

    def logoff(self):
        self.parent.backHome()

    def informacaoSistema(self, mensagem: str, desliga: bool = False):
        if desliga:
            self.lbSistemInfo.clear()
        else:
            self.lbSistemInfo.setText(mensagem)
            self.timerMsg.start(6500)

    def menssagemSistema(self, mensagem):
        self.sinais.sSistemInfo.emit(mensagem)

    def loading(self, intLoading:int):
        self.sinais.sSistemLoading.emit(intLoading)

    def sistemLoading(self, intProgress:int):
        self.pbarProgress.show()
        self.pbarProgress.setValue(intProgress)

        if self.pbarProgress.value() >= 100:
            self.timerLoading.start(3000)

    async def carregaLayout(self, tela: str):
        if tela is not None:
            if tela == 'home':
                self.pgHome = HomePage(self, db=self.db)
                self.stkDash.addWidget(self.pgHome)

            if tela == 'agenda':
                self.pgAgenda = AgendaPage(self, db=self.db)
                self.stkDash.addWidget(self.pgAgenda)

            if tela == 'cliente':
                self.pgCliente = brainCliente(self, db=self.db)
                self.stkDash.addWidget(self.pgCliente)

            if tela == 'financeiro':
                self.pgFinanceiro = FinanceiroPage(self, db=self.db)
                self.stkDash.addWidget(self.pgFinanceiro)

            if tela == 'configuracao':
                self.pgConfig = ConfigPage(self, db=self.db)
                self.stkDash.addWidget(self.pgConfig)
        else:
            return None



if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = mainDashboard()
    ui.show()
    sys.exit(app.exec_())