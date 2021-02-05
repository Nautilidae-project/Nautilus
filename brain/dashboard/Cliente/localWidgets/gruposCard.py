from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QTableWidgetItem

from Telas.cardGrupo import Ui_wdgGrupoCard
from brain.DAOs.daoCliente import DaoCliente
from brain.DAOs.daoGrupo import DaoGrupo
from brain.dashboard.Sinais import Sinais
from brain.delegates.alinhamento import AlinhamentoEsq
from brain.envioDeMensagens import Mensagens
from modelos.efeitosModel import Efeitos
from modelos.grupoModel import GrupoModelo


class GruposCard(Ui_wdgGrupoCard, QWidget):

    def __init__(self, parent=None, grupo: GrupoModelo = None, db=None):
        super(GruposCard, self).__init__()
        self.setupUi(self)
        self.db = db

        self.grupo = grupo
        self.parent = parent
        self.sinais = Sinais()
        self.enviarEmail = Mensagens()
        self.tblGrupoItem.setColumnHidden(0, True)
        self.tblGrupoItem.setItemDelegate(AlinhamentoEsq())
        Efeitos().shadowCards([self.tblGrupoItem])

        self.styleNormal = """
                    #frGrupoCard {
                        background-color: #0e90ad;
                    }"""
        self.styleEdicao = """
                    #frGrupoCard {
        	            background-color: #990100;
                    }"""

        self.sinais.sAtualizarTela.connect(self.atualizarCards)
        self.sinais.sEditarGrupo.connect(self.editarGrupo)

        self.pbEditar.clicked.connect(self.editarGrupo)
        self.pbExcluir.clicked.connect(self.excluirGrupo)
        self.pbEmailCard.clicked.connect(self.emailGrupo)

        if grupo is not None:
            self.populaTblParticipantes()

        if grupo is not None:
            self.lbTituloCard.setText(grupo.titulo)
            self.lbDescricao.setText(grupo.descricao)

    def populaTblParticipantes(self):
        daoGrupo = DaoGrupo(self.db)

        listaParticipantes = daoGrupo.buscaParticipantesGrupo(self.grupo.grupoId)

        self.tblGrupoItem.setRowCount(0)
        for rowCount, rowData in enumerate(listaParticipantes):
            self.tblGrupoItem.insertRow(rowCount)
            for columnCount, data in enumerate(rowData):
                strItem = QTableWidgetItem(str(data))
                strItem.setFont(QFont('Ubuntu', pointSize=12, italic=True))
                self.tblGrupoItem.setItem(rowCount, columnCount, strItem)

    def excluirGrupo(self):
        daoGrupo = DaoGrupo(self.db)
        intLoading = 0

        intLoading += 20
        self.parent.parent.loading(intLoading)
        daoGrupo.excluirGrupoEParticipantes(self.grupo.grupoId)

        intLoading += 20
        self.parent.parent.loading(intLoading)
        self.sinais.sAtualizarTela.emit()

        intLoading += 20
        self.parent.parent.loading(intLoading)
        self.sinais.sAtualizarTela.disconnect()

        intLoading += 20
        self.parent.parent.loading(intLoading)
        self.sinais.sAtualizarTela.connect(self.atualizarCards)

        intLoading += 20
        self.parent.parent.loading(intLoading)

        self.parent.parent.menssagemSistema(f'Grupo "{self.grupo.titulo}" excluído com sucesso.')

    def atualizarCards(self):
        self.parent.atualizaGruposCards()

    def editarGrupo(self):
        self.frGrupoCard.setStyleSheet(self.styleEdicao)
        self.parent.editarGrupo(self.grupo)

    def emailGrupo(self):
        daoGrupo = DaoGrupo(self.db).buscaParticipantesGrupo(self.grupo.grupoId)
        emailParticipantes = ''
        idParticipantes = ''
        nomeParticipantes = ''
        for cliente in daoGrupo:
            #print(DaoCliente().buscaPorId(cliente[0])[0])  # Indexs --> [2 tuplas], [1 tupla], [campo especifico]

            idParticipantes += str(DaoCliente(self.db).buscaPorId(cliente[0])[0][0]) + ', '

            nomeParticipantes += f"{DaoCliente(self.db).buscaPorId(cliente[0])[0][1]} {DaoCliente().buscaPorId(cliente[0])[0][2]}, "

            emailParticipantes += DaoCliente(self.db).buscaPorId(cliente[0])[0][4] + ', '

        self.enviarEmail.leId.setText(idParticipantes[0:-2])
        self.enviarEmail.leNome.setText(nomeParticipantes[0:-2])
        self.enviarEmail.leEmail.setText(emailParticipantes[0:-2])

        self.enviarEmail.show()

