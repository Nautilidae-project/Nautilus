from datetime import datetime

from PyQt5 import QtWidgets
from PyQt5.QtCore import QDate
from PyQt5.QtGui import QMouseEvent

from Telas.dashAgenda import Ui_wdgAgenda

from PyQt5.QtWidgets import QWidget

from brain.DAOs.daoGrupo import DaoGrupo
from brain.dashboard.Agenda.agendaController import CalendarioController
from brain.DAOs.daoEvento import DaoEvento
from modelos import eventoModel
from modelos.eventoModel import EventoModelo


class AgendaPage(Ui_wdgAgenda, QWidget):

    def __init__(self, parent=None):
        super(AgendaPage, self).__init__(parent)

        self.setupUi(self)

        self.calendario = CalendarioController()

        self.vlAgenda.addWidget(self.calendario)

        self.evento = EventoModelo()

        #Dao's
        self.daoEvento = DaoEvento()
        self.daoGrupo = DaoGrupo()

        # self.calendario.calendarWidget.clicked.connect(self.printDateInfo)

        # Chamando Tela de inserção de eventos
        self.frInserirEvento.hide()
        self.pbCriarEvento.clicked.connect(self.chamaTelaAddEventos)

        # self.calendario.mouseDoubleClickEvent.connect(self.addData)

        # Criando um Evento
        self.pbAddEvento.clicked.connect(lambda : self.criaEvento())

        # Adiciona os Grupos na ComboBox
        self.cbxGrupos.addItems(self.dictDosGruposFormados().keys())

    def criaEvento(self):

        daoEvento = DaoEvento()
        dictEvento = {
            'eventoId': None,
            'titulo': self.leTituloEvento.text()[0],
            'detalhe': self.teDetalhesEvento.toPlainText()[0],
            'grupoId': '1',
            'dataEvento': '2021-02-02 14:00',
            'dataCadastro': '2021-02-02 14:00',
            'horaInicio': '2021-02-02 14:00',
            'horaFim': '2021-02-02 14:00',
            'diaInteiro': False,
        }

        datas = []
        for data in [self.deDataEvento.text(), self.teHoraInicioEvento.text(), self.teHoraFimEvento.text()]:
            data = data.split()
            data = f'{data[0][-4:]}-{data[0][3:5]}-{data[0][0:2]} {data[1]}'
            datas.append(data)

        self.evento.titulo = self.leTituloEvento.text()
        self.evento.detalhe = self.teDetalhesEvento.toPlainText()
        self.evento.grupoId = self.dictDosGruposFormados()[self.cbxGrupos.currentText()]
        self.evento.dataEvento = datas[0]
        self.evento.dataCadastro = None
        self.evento.horaInicio = datas[1]
        self.evento.horaFim = datas[2]
        self.evento.diaInteiro = True

        # daoEvento.insereEvento(self.evento)

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