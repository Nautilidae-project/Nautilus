from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QTableWidgetItem

from Telas.cardGrupo import Ui_wdgGrupoCard
from brain.DAOs.daoGrupo import DaoGrupo
from brain.dashboard.Sinais import Sinais
from brain.delegates.alinhamento import AlinhamentoDelegate
from modelos.efeitosModel import Efeitos
from modelos.grupoModel import GrupoModelo


class GruposCard(Ui_wdgGrupoCard, QWidget):

    def __init__(self, parent=None, grupo: GrupoModelo = None):
        super(GruposCard, self).__init__()
        self.setupUi(self)
        self.grupo = grupo
        self.parent = parent
        self.sinais = Sinais()
        self.tblGrupoItem.setColumnHidden(0, True)
        self.tblGrupoItem.setItemDelegate(AlinhamentoDelegate())
        Efeitos().shadowCards([self.tblGrupoItem])

        self.sinais.sAtualizarTela.connect(self.atualizarCards)

        self.pbEditar.clicked.connect(self.editarGrupo)
        self.pbExcluir.clicked.connect(self.excluirGrupo)

        if grupo is not None:
            self.populaTblParticipantes()

        if grupo is not None:
            self.lbTituloCard.setText(grupo.titulo)
            self.lbDescricao.setText(grupo.descricao)

    def populaTblParticipantes(self):
        daoGrupo = DaoGrupo()

        listaParticipantes = daoGrupo.buscaParticipantesGrupo(self.grupo.grupoId)
        
        self.tblGrupoItem.setRowCount(0)
        for rowCount, rowData in enumerate(listaParticipantes):
            self.tblGrupoItem.insertRow(rowCount)
            for columnCount, data in enumerate(rowData):
                strItem = QTableWidgetItem(str(data))
                strItem.setFont(QFont('Ubuntu', pointSize=14, italic=True))
                self.tblGrupoItem.setItem(rowCount, columnCount, strItem)

    def excluirGrupo(self):
        print(f'Você acabou de excluir o grupo: {self.grupo.titulo}')
        daoGrupo = DaoGrupo()

        # daoGrupo.excluirGrupoEParticipantes(self.grupo.grupoId)
        self.sinais.sAtualizarTela.emit()
        self.sinais.disconnect()

    def atualizarCards(self):
        print('Recebi um sinaaaaal!')
        self.parent.adicionaGruposCards()



    def editarGrupo(self):
        print(f'Você quer editar o grupo: {self.grupo.titulo}')

