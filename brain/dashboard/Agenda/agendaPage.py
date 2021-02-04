from datetime import datetime
from math import ceil

from PyQt5 import QtWidgets
from PyQt5.QtCore import QDate, Qt, QSize
from PyQt5.QtGui import QMouseEvent

from Telas.dashAgenda import Ui_wdgAgenda

from PyQt5.QtWidgets import QWidget, QGridLayout, QVBoxLayout, QLabel

from brain.DAOs.daoGrupo import DaoGrupo
from brain.dashboard.Agenda.agendaController import CalendarioController
from brain.DAOs.daoEvento import DaoEvento
from brain.dashboard.Agenda.localWidgets.eventosCard import EventosCard
from brain.dashboard.Cliente.localWidgets.gruposCard import GruposCard
from modelos import eventoModel
from modelos.eventoModel import EventoModelo
from modelos.grupoModel import GrupoModelo
from modelos.efeitosModel import Efeitos


class AgendaPage(Ui_wdgAgenda, QWidget):

    def __init__(self, parent=None):
        super(AgendaPage, self).__init__(parent)

        self.setupUi(self)

        self.calendario = CalendarioController()

        self.vlAgenda.addWidget(self.calendario)

        self.evento = EventoModelo()

        self.gridBox = QGridLayout()
        self.efeito = Efeitos()

        self.atualizaGruposCards()

        self.colunas = 0

        #Dao's
        self.daoEvento = DaoEvento()
        self.daoGrupo = DaoGrupo()

        # self.calendario.calendarWidget.clicked.connect(self.printDateInfo)

        # Chamando Tela de inserção de eventos
        self.frInserirEvento.hide()
        self.pbCriarEvento.clicked.connect(self.chamaTelaAddEventos)

        # self.calendario.mouseDoubleClickEvent.connect(self.addData)

        # Criando um Evento
        self.pbAddEvento.clicked.connect(self.criaEvento)

        # Adiciona os Grupos na ComboBox
        self.cbxGrupos.addItems(self.dictDosGruposFormados().keys())

        self.calendario.clicked[QDate].connect(self.printDataSelecionada)

    def atualizaGruposCards(self):

        

        colunas = 1

        # Busca no banco de dados todos os grupos criados

        eventosCadastrados = DaoEvento().findAll()

        widthCard = self.saEventosCard.sizeHint().width() + 20
        widthScreen = self.window().size().width()

        if len(eventosCadastrados) > 8 and 3 * widthCard < widthScreen:
            colunas = 2
        elif len(eventosCadastrados) > 3 and 2 * widthCard < widthScreen:
            colunas = 1


        self.colunas = colunas

        linhas = ceil(len(eventosCadastrados) / colunas)
        print(linhas, ' ------')

        # Cria um lista contendo o modelo de cada grupo buscado no banco de dados

        eventoModelos = [EventoModelo(eventosCadastrados[i]) for i in range(0, len(eventosCadastrados))]

        # Cria uma lista contendo os layouts dos cards com as informações dos modelos contidos no eventoModelos
        listaEventosCards = [EventosCard(parent=self, evento=eventoModelos[i]) for i in range(0, len(eventosCadastrados))]
        print(len(listaEventosCards))

        # Cria uma matriz das posições nas quais os cards serão apresentados
        posicoes = [(linha, coluna) for linha in range(linhas) for coluna in range(colunas)]

        for card, posicao in zip(listaEventosCards, posicoes):
            self.efeito.shadowCards([card], color=(105, 210, 231, 80))
            self.gridBox.addWidget(card, *posicao)
        # self.gridBox.setSpacing(32)

        if self.gridBox.count():
            self.saEventosCard.setLayout(self.gridBox)


    def printDataSelecionada(self):
        for data in DaoEvento().buscaDatasEventos().values():
            if self.calendario.selectedDate() == data:
                print(data, ' ---')

    def redimensionaTela(self):
        sizeCard = EventosCard().sizeHint().width() + 20
        sizeArea = self.saEventosCard.size().width()

        if 3*sizeCard < sizeArea:
            colunas = 3
        elif 2*sizeCard < sizeArea:
            colunas = 2
        else:
            colunas = 1

        if colunas == self.colunas:
            return True
        else:
            self.colunas = colunas

            listaCards = list()

            for i in range(self.gridBox.count()):
                listaCards.append(self.gridBox.itemAt(i).widget())

            self.limpaLayout()

            linhas = ceil(len(listaCards) / colunas)

            posicoes = [(linha, coluna) for linha in range(linhas) for coluna in range(colunas)]

            for card, posicao in zip(listaCards, posicoes):
                self.efeito.shadowCards([card], color=(105, 210, 231, 80))
                self.gridBox.addWidget(card, *posicao)
            self.gridBox.setSpacing(32)

            if self.gridBox.count():
                self.scrollGrupos.setLayout(self.gridBox)

    def criaEvento(self):

        datas = []
        for data in [self.deDataEvento.text(), self.teHoraInicioEvento.text(), self.teHoraFimEvento.text()]:
            data = data.split()
            data = f'{data[0][-4:]}-{data[0][3:5]}-{data[0][0:2]} {data[1]}'
            datas.append(data)

        self.evento.titulo = self.leTituloEvento.text()
        self.evento.detalhe = self.teDetalhesEvento.toPlainText()
        self.evento.grupoId = self.dictDosGruposFormados()[self.cbxGrupos.currentText()]
        self.evento.dataEvento = datas[0]
        # self.evento.dataEvento = self.deDataEvento
        # a = self.deDataEvento.dateTime().toPyDateTime()
        # print(a)
        # print(QDate)
        self.evento.dataCadastro = None
        self.evento.horaInicio = datas[1]
        self.evento.horaFim = datas[2]
        self.evento.diaInteiro = True

        self.daoEvento.insereEvento(self.evento)

    def dictDosGruposFormados(self) -> dict:
        grupos = {grupo[1]: grupo[0] for grupo in self.daoGrupo.findAll()}

        return grupos

    def printDateInfo(self, qDate):
        x = datetime.now().strftime("%B")
        y = datetime(year=qDate.year(), month=qDate.dayOfWeek(), day=qDate.day())
        print('{0}/{1}/{2}'.format(qDate.month(), qDate.day(), qDate.year()))
        print(f'Numero de dias do ano: {qDate.dayOfYear()}')
        print(f'Numero de dias do mÊs: {qDate.dayOfWeek()}')
        print(f'Numero do dia da semana ano: {qDate.day()}')
        print(x)
        print(y)
        print(y.strftime("%Y %B"))
        print(self.calendario.calendarWidget.selectedDate())
        self.lbData.setText(str(y))

    def chamaTelaAddEventos(self):
        self.frInserirEvento.setHidden(not self.frInserirEvento.isHidden())


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = AgendaPage()
    ui.show()
    sys.exit(app.exec_())