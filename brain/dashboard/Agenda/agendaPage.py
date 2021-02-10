from datetime import datetime
from math import ceil

from PyQt5 import QtWidgets
from PyQt5.QtCore import QDate, Qt, QSize, QPropertyAnimation
from Telas.dashAgenda import Ui_wdgAgenda
from PyQt5.QtWidgets import QWidget, QGridLayout, QVBoxLayout, QLabel
from brain.DAOs.daoGrupo import DaoGrupo
from brain.dashboard.Agenda.agendaController import CalendarioController
from brain.DAOs.daoEvento import DaoEvento
from brain.dashboard.Agenda.localWidgets.eventosCard import EventosCard
from modelos.eventoModel import EventoModelo
from modelos.efeitosModel import Efeitos


class AgendaPage(Ui_wdgAgenda, QWidget):

    def __init__(self, parent=None, db=None):
        super(AgendaPage, self).__init__(parent)
        self.db = db

        self.setupUi(self)

        self.calendario = CalendarioController(db=db)

        self.vlAgenda.addWidget(self.calendario)

        # ---- Configurações  e Chamadas ---- #
        # Dao's
        self.daoEvento = DaoEvento(self.db)
        self.daoGrupo = DaoGrupo(self.db)

        self.gridBox = QGridLayout()
        self.efeito = Efeitos()

        self.eventoModelo = EventoModelo()

        # Chamando e escondendo a Tela de inserção de eventos
        self.frInserirEvento.hide()
        self.pbCriarEvento.clicked.connect(self.chamaTelaAddEventos)

        # Adiciona os Grupos na ComboBox
        self.cbxGrupos.addItems(self.dictDosGruposFormados().keys())

        # Atualiza e Adiciona os Cards dos Eventos No GridLayout
        # self.AddCardEventosNoGrid()
        self.calendario.clicked.connect(lambda: self.AddCardEventosNoGrid())

        # Ajustando as datas da seleção de datas
        self.deDataEvento.setDate(self.calendario.selectedDate())
        self.calendario.selectionChanged.connect(self.selectedDateChanged)

        # self.calendario.mouseDoubleClickEvent.connect(self.addData)

        # Criando um Evento
        self.pbAddEvento.clicked.connect(self.criaEvento)

        # self.calendario.clicked[QDate].connect(self.printDataSelecionada)
        # self.calendario.clicked[QDate].connect(lambda: self.dataSelecionada(self.calendario.selectedDate())) # ---- Esse deu certo Eu Acho

        self.enable = False

    def selectedDateChanged(self):
        # self.deDataEvento.setDate(self.calendario.selectedDate())
        self.teHoraInicioEvento.setDate(self.calendario.selectedDate())
        self.teHoraFimEvento.setDate(self.calendario.selectedDate())

    def AddCardEventosNoGrid(self):

        self.removeCardsDoGrid()
        
        # if self.calendario.selectedDate() in DaoEvento(self.db).buscaDatasEventos().values():
        if self.calendario.selectedDate() in self.calendario.datasSelecionadas.values():
            colunas = 1

            # Busca no banco de dados todos os eventos criados com em relação a data informada
            dataSelecionada = self.dataSelecionada(self.calendario.selectedDate())

            eventosCadastrados = DaoEvento(self.db).findAllDataSelecionada(dataSelecionada)
            # print(eventosCadastrados)

            linhas = ceil(len(eventosCadastrados) / colunas)
            # print(linhas, ' ------')

            # Cria um lista contendo o modelo de cada grupo buscado no banco de dados
            eventoModelos = [EventoModelo(eventosCadastrados[i]) for i in range(0, len(eventosCadastrados))]
            # print(eventoModelos)

            # Cria uma lista contendo os layouts dos cards com as informações dos modelos contidos no eventoModelos
            listaEventosCards = [EventosCard(parent=self, evento=eventoModelos[i], db=self.db) for i in range(0, len(eventosCadastrados))]
            # listaEventosCards = (EventosCard(parent=self, evento=eventoModelos[i], db=self.db) for i in range(0, len(eventosCadastrados)))

            # Cria uma matriz das posições nas quais os cards serão apresentados
            posicoes = [(linha, coluna) for linha in range(linhas) for coluna in range(colunas)]

            for card, posicao in zip(listaEventosCards, posicoes):
                self.efeito.shadowCards([card], color=(105, 210, 231, 80))
                self.gridBox.addWidget(card, *posicao)
            # self.gridBox.setSpacing(32)

            if self.gridBox.count():
                self.saEventosCard.setLayout(self.gridBox)

            print('---- Tem Eventos')
        elif self.gridBox.count() > 0:
            self.removeCardsDoGrid()
            print('Limpei os Cards !!!!')
            print(self.gridBox.count())
        else:
            print(')))) Passei e Não tem Nada ((((')
            pass

    def dataSelecionada(self, data: QDate):
        """
        Retorna a data selecionado no calendario formatada para Python
        :return: Data formatada --> yyuy/mm/dd
        """
        return data.toPyDate()

    def removeCardsDoGrid(self):
            """
            Remove Os Cards que estão no grid layout
            """
            for i in reversed(range(self.gridBox.count())):
                self.gridBox.itemAt(i).widget().deleteLater()

    def criaEvento(self):
        """
        Adiciona um eventos no banco de dados
        """

        self.eventoModelo.titulo = self.leTituloEvento.text()
        self.eventoModelo.detalhe = self.teDetalhesEvento.toPlainText()
        self.eventoModelo.grupoId = self.dictDosGruposFormados()[self.cbxGrupos.currentText()]
        self.eventoModelo.dataEvento = self.deDataEvento.date().toPyDate()
        self.eventoModelo.dataCadastro = None
        self.eventoModelo.horaInicio = self.teHoraInicioEvento.dateTime().toPyDateTime()
        self.eventoModelo.horaFim = self.teHoraFimEvento.dateTime().toPyDateTime()
        self.eventoModelo.diaInteiro = True

        self.daoEvento.insereEvento(self.eventoModelo)


    def dictDosGruposFormados(self) -> dict:
        """
        Retorna um dicionário com todos grupos cadastrados
        :return: dict{'Nome_do_Grupo': id_do_Grupo}
        """
        banco = self.daoGrupo.findAll()
        grupos = {grupo[1]: grupo[0] for grupo in banco}
        return grupos

    def chamaTelaAddEventos(self):
        """
        Faz aparecer a tela com as informações editaveis para cadastrar os eventos
        """
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