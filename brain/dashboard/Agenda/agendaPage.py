from datetime import datetime
from math import ceil

from PyQt5 import QtWidgets
from PyQt5.QtCore import QDate, Qt, QSize, QPropertyAnimation
from Telas.dashAgenda import Ui_wdgAgenda
from PyQt5.QtWidgets import QWidget, QGridLayout, QVBoxLayout, QLabel
from brain.DAOs.daoGrupo import DaoGrupo
from brain.DAOs.daoEvento import DaoEvento
from brain.DAOs.daoParticipantes import DaoParticipantes
from brain.dashboard.Agenda.agendaController import CalendarioController
from brain.dashboard.Agenda.localWidgets.eventosCard import EventosCard
from modelos.eventoModel import EventoModelo
from modelos.efeitosModel import Efeitos


class AgendaPage(Ui_wdgAgenda, QWidget):

    def __init__(self, parent=None, db=None):
        super(AgendaPage, self).__init__(parent)
        self.db = db

        self.setupUi(self)
        self.parent = parent

        self.calendario = CalendarioController(db=db)

        self.vlAgenda.addWidget(self.calendario)

        # ---- Configurações  e Chamadas ---- #
        # ....................................................................................................... Dao's
        self.daoEvento = DaoEvento(self.db)
        self.daoGrupo = DaoGrupo(self.db)
        self.daoParticipantes = DaoParticipantes(self.db)

        self.gridBox = QGridLayout()
        self.efeito = Efeitos()

        self.eventoModelo = EventoModelo()

        # ...................................................................................... Verificações Booleanas
        self.animTela = False
        self.modoEdicao = False

        # ..................................................................... Escondendo e Manipulando Telas e Botôes
        self.frInserirEvento.hide()
        self.pbChamaInserirEvento.clicked.connect(self.chamaTelaAddEventos)

        self.pbCancelaEdicao.hide()
        self.pbCancelaEdicao.clicked.connect(self.sairModoEdicao)

        # .............................................................................. Adiciona os Grupos na ComboBox
        # self.cbxGrupos.addItem('Nenhum grupo')
        self.cbxGrupos.addItems(self.dictDosGruposFormados().keys())

        # ...................................................... Atualiza e Adiciona os Cards dos Eventos No GridLayout
        self.AddCardEventosNoGrid()
        self.calendario.clicked.connect(lambda: self.AddCardEventosNoGrid())

        # ...................................................................... Ajustando as datas da seleção de datas
        self.deDataEvento.setDate(self.calendario.selectedDate())
        self.calendario.selectionChanged.connect(self.selectedDateChanged)

        # ........................................................................................... Criando um Evento
        self.pbAddEvento.clicked.connect(lambda: self.criaEvento() if not self.modoEdicao else self.updateEvento)

        # Botões de manipulação do CardEvento ????????????????????????????????????????

        # self.calendario.clicked[QDate].connect(self.printDataSelecionada)
        # self.calendario.clicked[QDate].connect(lambda: self.dataSelecionada(self.calendario.selectedDate())) # ---- Esse deu certo Eu Acho

    def selectedDateChanged(self):
        self.deDataEvento.setDate(self.calendario.selectedDate())
        # self.teHoraInicioEvento.setDate(self.calendario.selectedDate())
        # self.teHoraFimEvento.setDate(self.calendario.selectedDate())

        self.leTituloEvento.setText(f"{self.calendario.selectedDate().toPyDate()}")
        self.teDetalhesEvento.setPlainText(f"{self.calendario.selectedDate().toPyDate()}")

    # ....................................................................... Criação e Manipulações dos Evento e cards
    def criaEvento(self):
        """
        Adiciona um eventos no banco de dados
        """

        self.eventoModelo.titulo = self.leTituloEvento.text()
        self.eventoModelo.detalhe = self.teDetalhesEvento.toPlainText()

        self.eventoModelo.grupoId = self.dictDosGruposFormados()[self.cbxGrupos.currentText()]\
            if self.cbxGrupos.currentIndex() != 0 else None
        #     TODO: Implementar Inserção de participantes sem grupo

        self.eventoModelo.dataEvento = self.deDataEvento.date().toPyDate()
        self.eventoModelo.dataCadastro = None
        self.eventoModelo.horaInicio = self.teHoraInicioEvento.dateTime().toPyDateTime()
        self.eventoModelo.horaFim = self.teHoraFimEvento.dateTime().toPyDateTime()
        self.eventoModelo.diaInteiro = False if self.cbxDiaInteiro.currentText() == "Não" else True

        # Add Participantes
        if self.eventoModelo.grupoId:
            eventoId = self.daoEvento.insereEvento(self.eventoModelo)
            particiopantesSelecionados = list(self.daoGrupo.buscaParticipantesGrupo(self.eventoModelo.grupoId))
            self.daoParticipantes.insereParticipantesEvento(eventoId, self.eventoModelo.grupoId, particiopantesSelecionados)

            self.atualizaMarcacoesNoCalendario()

            # TODO Esse código abaixo é referente a editar o evento de um grupo de participantes
            # for idCliente in range(len(particiopantesSelecionados)):
            #     self.daoParticipantes.insereParticipantesEvento(
            #         particiopantesSelecionados[idCliente][0], eventoId, self.eventoModelo.grupoId)
        else:
            # eventoId = self.daoEvento.insereEvento(self.eventoModelo, grupo=False)
            # self.daoParticipantes.insereParticipantesEvento(eventoId)
            pass

    def AddCardEventosNoGrid(self):

        self.removeCardsDoGrid()

        # if self.calendario.selectedDate() in DaoEvento(self.db).buscaDatasEventos().values():
        if self.calendario.selectedDate() in self.calendario.datasSelecionadas.values():
            colunas = 1

            # Busca no banco de dados todos os eventos criados com em relação a data informada
            dataSelecionada = self.dataSelecionadaToPy(self.calendario.selectedDate())

            eventosCadastrados = DaoEvento(self.db).findAllDataSelecionada(dataSelecionada)

            linhas = ceil(len(eventosCadastrados) / colunas)

            # Cria um lista contendo o modelo de cada grupo buscado no banco de dados
            eventoModelos = [EventoModelo(eventosCadastrados[i]) for i in range(0, len(eventosCadastrados))]

            # Cria uma lista contendo os layouts dos cards com as informações dos modelos contidos no eventoModelos
            listaEventosCards = [EventosCard(parent=self, evento=eventoModelos[i], db=self.db) for i in
                                 range(0, len(eventosCadastrados))]

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

    def removeCardsDoGrid(self):
        """
            Remove Os Cards que estão no grid layout
            """
        for i in reversed(range(self.gridBox.count())):
            self.gridBox.itemAt(i).widget().deleteLater()

    # ............................................................................. Edições dos Eventos e participantes
    def editarEvento(self, evento: EventoModelo):
        self.modoEdicao = True
        self.pbCancelaEdicao.show()
        self.eventoEdicao = evento
        self.pbAddEvento.setText('Confirmar')
        self.frInserirEvento.show()

    def updateEvento(self):
        print('Estou no update')
        self.sairModoEdicao()

    def sairModoEdicao(self):
        self.modoEdicao = False
        self.pbCancelaEdicao.hide()

        self.atualizaMarcacoesNoCalendario()

        self.pbAddEvento.setText("Adicionar Evento")
        # self.parent.menssagemSistema('Evento editado com sucesso.')

    # ............................................................................................. Manipulações Gerais
    def dataSelecionadaToPy(self, data: QDate):
        """
        Retorna a data selecionado no calendario formatada para Python
        :return: Data formatada --> yyuy/mm/dd
        """
        print('Essa é a data ---> ', data)
        return data.toPyDate()

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

    def atualizaMarcacoesNoCalendario(self):
        self.calendario.daoEvento = dict(enumerate(DaoEvento(self.db).buscaDatasEventosSemRepeticao()))
        self.calendario.datasSelecionadas = self.calendario.daoEvento
        self.AddCardEventosNoGrid()
        # print(self.calendario.daoEvento)
        # print(self.calendario.datasSelecionadas)

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
