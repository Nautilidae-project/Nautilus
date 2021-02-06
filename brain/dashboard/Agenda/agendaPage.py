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

    def __init__(self, parent=None, db=None):
        super(AgendaPage, self).__init__(parent)
        self.db = db

        self.setupUi(self)

        self.calendario = CalendarioController(db=db)

        self.vlAgenda.addWidget(self.calendario)

        self.evento = EventoModelo()

        self.gridBox = QGridLayout()
        self.efeito = Efeitos()

        self.atualizaGruposCards()

        self.colunas = 0

        # Ajustando as datas da seleção de datas
        self.deDataEvento.setDate(self.calendario.selectedDate())

        self.calendario.selectionChanged.connect(self.selectedDateChanged)

        #Dao's
        self.daoEvento = DaoEvento(self.db)
        self.daoGrupo = DaoGrupo(self.db)

        # self.calendario.calendarWidget.clicked.connect(self.printDateInfo)

        # Chamando Tela de inserção de eventos
        self.frInserirEvento.hide()
        self.pbCriarEvento.clicked.connect(self.chamaTelaAddEventos)

        # self.calendario.mouseDoubleClickEvent.connect(self.addData)

        # Criando um Evento
        self.pbAddEvento.clicked.connect(self.criaEvento)

        # Adiciona os Grupos na ComboBox
        self.cbxGrupos.addItems(self.dictDosGruposFormados().keys())

        # self.calendario.clicked[QDate].connect(self.printDataSelecionada)

        # print(self.calendario.selectedDate())
        (self.calendario.clicked[QDate].connect(lambda: print(self.calendario.selectedDate()))) # ---- Esse deu certo Eu Acho

        # print(DaoEvento(self.db).findAllDataSelecionada(self.calendario.selectedDate))
        # print(DaoEvento(self.db).findAllDataSelecionada('2021-02-03'))
        # print(DaoEvento(self.db).findAllDataSelecionada(str(self.calendario.selectedDate())))


    def selectedDateChanged(self):
        # self.deDataEvento.setDate(self.calendario.selectedDate())
        self.teHoraInicioEvento.setDate(self.calendario.selectedDate())
        self.teHoraFimEvento.setDate(self.calendario.selectedDate())

    def atualizaGruposCards(self):

        # Se já houverem widgets na tela, reinicia o layout
        if self.gridBox.count():
            self.limpaLayout()

        colunas = 1

        # Busca no banco de dados todos os grupos criados

        eventosCadastrados = DaoEvento(self.db).findAll()

        # widthCard = self.saEventosCard.sizeHint().width() + 20
        # widthScreen = self.window().size().width()
        #
        # if len(eventosCadastrados) > 8 and 3 * widthCard < widthScreen:
        #     colunas = 2
        # elif len(eventosCadastrados) > 3 and 2 * widthCard < widthScreen:
        #     colunas = 1

        self.colunas = colunas

        linhas = ceil(len(eventosCadastrados) / colunas)
        # print(linhas, ' ------')

        # Cria um lista contendo o modelo de cada grupo buscado no banco de dados

        eventoModelos = [EventoModelo(eventosCadastrados[i]) for i in range(0, len(eventosCadastrados))]
        # print(eventoModelos)

        # Cria uma lista contendo os layouts dos cards com as informações dos modelos contidos no eventoModelos
        listaEventosCards = [EventosCard(parent=self, evento=eventoModelos[i], db=self.db) for i in range(0, len(eventosCadastrados))]

        # Cria uma matriz das posições nas quais os cards serão apresentados
        posicoes = [(linha, coluna) for linha in range(linhas) for coluna in range(colunas)]

        for card, posicao in zip(listaEventosCards, posicoes):
            self.efeito.shadowCards([card], color=(105, 210, 231, 80))
            self.gridBox.addWidget(card, *posicao)
        # self.gridBox.setSpacing(32)

        if self.gridBox.count():
            self.saEventosCard.setLayout(self.gridBox)


    def printDataSelecionada(self):
        for data in DaoEvento(db).buscaDatasEventos().values():
            if self.calendario.selectedDate() == data:
                print(data, ' ---')

    def criaEvento(self):

        # datas = []
        # for data in [self.deDataEvento.text(), self.teHoraInicioEvento.text(), self.teHoraFimEvento.text()]:
        #     data = data.split()
        #     data = f'{data[0][-4:]}-{data[0][3:5]}-{data[0][0:2]} {data[1]}'
        #     datas.append(data)

        self.evento.titulo = self.leTituloEvento.text()
        self.evento.detalhe = self.teDetalhesEvento.toPlainText()
        self.evento.grupoId = self.dictDosGruposFormados()[self.cbxGrupos.currentText()]

        # self.evento.dataEvento = datas[0]
        self.evento.dataEvento = self.deDataEvento.date().toPyDate()
        print(self.evento.dataEvento)

        self.evento.dataCadastro = None

        # self.evento.horaInicio = datas[1]
        self.evento.horaInicio = self.teHoraInicioEvento.dateTime().toPyDateTime()

        # self.evento.horaFim = datas[2]
        self.evento.horaFim = self.teHoraFimEvento.dateTime().toPyDateTime()

        self.evento.diaInteiro = True

        self.daoEvento.insereEvento(self.evento)

    def dictDosGruposFormados(self) -> dict:
        banco = self.daoGrupo.findAll()
        grupos = {grupo[1]: grupo[0] for grupo in banco}
        return grupos

    def printDateInfo(self, qDate):
        x = datetime.now().strftime("%B")
        y = datetime(year=qDate.year(), month=qDate.dayOfWeek(), day=qDate.day())
        # print('{0}/{1}/{2}'.format(qDate.month(), qDate.day(), qDate.year()))
        # print(f'Numero de dias do ano: {qDate.dayOfYear()}')
        # print(f'Numero de dias do mÊs: {qDate.dayOfWeek()}')
        # print(f'Numero do dia da semana ano: {qDate.day()}')
        # print(x)
        # print(y)
        # print(y.strftime("%Y %B"))
        # print(self.calendario.calendarWidget.selectedDate())
        self.lbData.setText(str(y))

    def chamaTelaAddEventos(self):
        self.frInserirEvento.setHidden(not self.frInserirEvento.isHidden())


if __name__ == '__main__':
    import sys
    import pymysql
    from configBD import ConfigDB

    app = QtWidgets.QApplication(sys.argv)
    # db = getDB()
    config = ConfigDB(carregaBanco=True)
    db = pymysql.connect(
            host=config.host,
            user=config.user,
            passwd=config.passwd,
            db=config.banco,
            port=config.port
            )
    ui = AgendaPage(db=db)
    ui.show()
    sys.exit(app.exec_())