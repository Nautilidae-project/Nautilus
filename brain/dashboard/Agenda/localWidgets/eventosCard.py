from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QApplication

from Telas.cardEvento import Ui_wdgEventoCard
from brain.DAOs.daoEvento import DaoEvento

from modelos.eventoModel import EventoModelo


class EventosCard(Ui_wdgEventoCard, QWidget):

    def __init__(self, parent=None, evento: EventoModelo = None, db=None):
        super(EventosCard, self).__init__()
        self.setupUi(self)
        self.db = db
        self.evento = evento
        self.parent = parent
        self.db = db
        # self.tblGrupoItem.setColumnHidden(0, True)
        # self.tblGrupoItem.setItemDelegate(AlinhamentoEsq())
        # Efeitos().shadowCards([self.tblGrupoItem])

        self.styleNormal = """
                    #frGrupoCard {
                        background-color: #0e90ad;
                    }"""
        self.styleEdicao = """
                    #frGrupoCard {
        	            background-color: #990100;
                    }"""

        # self.pbEditar.clicked.connect(self.editarGrupo)
        # self.pbExcluir.clicked.connect(self.excluirGrupo)
        # self.pbEmailCard.clicked.connect(self.emailGrupo)

        # self.daoEvento = DaoEvento()
        # print(self.daoEvento.findAll())
        #
        # if self.evento is not None:
        #     self.lbTituloCard.setText(self.evento.titulo[0])
        #     self.lbDescricao.setText(self.evento.detalhe[0])

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




if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ui = EventosCard()
    ui.show()
    sys.exit(app.exec_())