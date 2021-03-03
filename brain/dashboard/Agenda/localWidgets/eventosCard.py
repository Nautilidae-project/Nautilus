import os
from datetime import datetime

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
        # self.dashboard = parent.parent

        self.styleEdicao = """
                    #frGrupoCard {
        	            background-color: #990100;
                    }"""

        self.calendar = CalendarioController(db=self.db)

        self.frInfosEdicoes.hide()

        # Dao's
        self.daoEvento = DaoEvento(self.db)
        # self.daoGrupo = DaoGrupo(self.db)
        self.daoParticipantes = DaoParticipantes(self.db)

        self.parent = parent
        self.sinais = Sinais()

        # # Declarando Botões de manipulação do CardEvento
        self.pbEditarEvento.clicked.connect(self.editarEvento)
        self.pbEmailEvento.clicked.connect(self.emailEvento)
        self.pbDeletarEvento.clicked.connect(self.excluirEvento)

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

    def carregaInfosEvento(self):
        self.frInfosEdicoes.show()

        horaInicio = datetime.time(self.evento.horaInicio[0])
        horaFim = datetime.time(self.evento.horaFim[0])

        self.lbTituloCard.setText(self.evento.titulo[0])
        self.lbDescricao.setPlainText(self.evento.detalhe[0])
        self.lbDescricao.setStyleSheet('background-color: #fafafa;')
        self.lbDescricao.setReadOnly(False)

        self.deDataEvento.setDate(self.evento.dataEvento[0])
        self.cbxDiaInteiro.setCurrentIndex(int(self.evento.diaInteiro))

        self.teHoraInicioEvento.setTime(horaInicio)
        self.teHoraFimEvento.setTime(horaFim)


    def editarEvento(self):
        # self.parent.editarEvento(self.evento)

        self.frGrupoCard.setStyleSheet(self.styleEdicao)
        self.carregaInfosEvento()


    def emailEvento(self):
        print('FAlta implementar Envio de Email')

    def excluirEvento(self):
        # TODO: Lembrar de  comentar e descomentar todas as self.dashboard quando rodar o programa direto

        # self.dashboard.loading(20)

        print("Esse é o evento ---> ", self.evento.eventoId[0], self.evento.titulo)

        self.daoEvento.excluirEventoEParticipantes(self.evento.eventoId[0])

        # self.dashboard.loading(40)

        print('Evento Excluido Com Sucesso!!!!!!!!!!!!')

        self.parent.atualizaMarcacoesNoCalendario()

        # self.dashboard.loading(80)

        # self.dashboard.menssagemSistema('Evento Excluido Com Sucesso!!!!!!!!!!!!')

        # self.dashboard.loading(100)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ui = EventosCard()
    ui.show()
    sys.exit(app.exec_())