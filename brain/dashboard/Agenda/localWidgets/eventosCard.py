import os

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QApplication

from Telas.cardEvento import Ui_wdgEventoCard
from brain.DAOs.daoEvento import DaoEvento
from brain.DAOs.daoParticipantes import DaoParticipantes
from brain.dashboard.Sinais import Sinais

from modelos.eventoModel import EventoModelo

from brain.dashboard.Agenda.agendaController import CalendarioController


class EventosCard(Ui_wdgEventoCard, QWidget):

    def __init__(self, parent=None, evento: EventoModelo = None, db=None):
        super(EventosCard, self).__init__()
        self.setupUi(self)
        self.db = db
        self.evento = evento
        self.parent = parent
        self.db = db

        self.styleNormal = """
                    #frGrupoCard {
                        background-color: #0e90ad;
                    }"""
        self.styleEdicao = """
                    #frGrupoCard {
        	            background-color: #990100;
                    }"""

        self.calendar = CalendarioController(db=self.db)

        # Dao's
        self.daoEvento = DaoEvento(self.db)
        # self.daoGrupo = DaoGrupo(self.db)
        self.daoParticipantes = DaoParticipantes(self.db)

        self.parent = parent
        self.sinais = Sinais()

        # # Declarando Botões de manipulação do CardEvento
        self.pbEditarEvento.clicked.connect(self.editarEvento)
        self.pbEmailEvento.clicked.connect(self.emailEvento)
        self.pbDeletarEvento.clicked.connect(self.excluirGrupo)

        if self.evento is not None:
            self.popularGrid()

        if self.evento is not None:
            self.lbTituloCard.setText(self.evento.titulo[0])
            self.lbDescricao.setText(self.evento.detalhe[0])

    def popularGrid(self):
        daoEvento = DaoEvento(self.db)
        participante = daoEvento.buscaPorId(self.evento.eventoId[0])
        # print(participante)
        return participante

    def editarEvento(self):
        print('FAlta implementar Edição de Evento')
        print('Evento', self.evento)

    def emailEvento(self):
        print('FAlta implementar Envio de Email')

    def excluirGrupo(self):
        # 1 - Excluir participante do evento
        # 2 - Excluir evento em si
        intLoading = 20

        print("Esse é o evento ---> ", self.evento.eventoId[0], self.evento.titulo)

        intLoading += 20

        self.daoEvento.excluirEventoEParticipantes(self.evento.eventoId[0])

        print('Evento Excluido Com Sucesso!!!!!!!!!!!!11')

        self.parent.atualizaMarcacoesNoCalendario()



if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ui = EventosCard()
    ui.show()
    sys.exit(app.exec_())