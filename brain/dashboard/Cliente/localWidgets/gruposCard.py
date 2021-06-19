from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QTableWidgetItem

from Telas.cardGrupo import Ui_wdgGrupoCard
from brain.DAOs.daoCliente import DaoCliente
from brain.DAOs.daoGrupo import DaoGrupo
from brain.dashboard.Cliente.localStyleSheets.grupoCards import frameCategoriaCard, labelCard
from brain.dashboard.Sinais import Sinais
from brain.delegates.alinhamento import AlinhamentoEsq
from brain.envioDeMensagens import Mensagens
from modelos.efeitosModel import Efeitos
from modelos.grupoModel import GrupoModelo

from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager


class GruposCard(Ui_wdgGrupoCard, QWidget):

    def __init__(self, parent=None, grupo: GrupoModelo = None, db=None):
        super(GruposCard, self).__init__(parent=parent)
        self.setupUi(self)
        self.db = db
        if parent is not None:
            self.dashboard = parent.parent
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
        self.pbZap.clicked.connect(self.enviarWhatsapp)

        if grupo is not None:
            self.populaTblParticipantes()
            self.defineCategoriaNomeStyle()
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

    def enviarWhatsapp(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get('https://www.whatsapp.com/')

        time.sleep(30)

        driver.find_element_by_xpath()

    def excluirGrupo(self):
        daoGrupo = DaoGrupo(self.db)
        intLoading = 0

        intLoading += 20
        self.dashboard.loading(intLoading)
        daoGrupo.excluirGrupoEParticipantes(self.grupo.grupoId)

        intLoading += 20
        self.dashboard.loading(intLoading)
        self.sinais.sAtualizarTela.emit()

        intLoading += 20
        self.dashboard.loading(intLoading)
        self.sinais.sAtualizarTela.disconnect()

        intLoading += 20
        self.dashboard.loading(intLoading)
        self.sinais.sAtualizarTela.connect(self.atualizarCards)

        intLoading += 20
        self.dashboard.loading(intLoading)

        self.dashboard.part.menssagemSistema(f'Grupo "{self.grupo.titulo}" excluído com sucesso.')

    def atualizarCards(self):
        self.dashboard.atualizaGruposCards()

    def editarGrupo(self):
        self.frGrupoCard.setStyleSheet(self.styleEdicao)
        self.dashboard.editarGrupo(self.grupo)

    def emailGrupo(self):
        self.dashboard.loading(10)
        daoGrupo = DaoGrupo(self.db).buscaParticipantesGrupo(self.grupo.grupoId)
        self.dashboard.loading(30)
        emailParticipantes = ''
        self.dashboard.loading(40)
        idParticipantes = ''
        self.dashboard.loading(50)
        nomeParticipantes = ''
        self.dashboard.loading(60)
        for cliente in daoGrupo:

            idParticipantes += str(DaoCliente(self.db).buscaPorId(cliente[0])[0][0]) + ', '

            nomeParticipantes += f"{DaoCliente(self.db).buscaPorId(cliente[0])[0][1]} {DaoCliente(db=self.db).buscaPorId(cliente[0])[0][2]}, "

            emailParticipantes += DaoCliente(self.db).buscaPorId(cliente[0])[0][4] + ', '

        self.dashboard.loading(70)
        self.enviarEmail.leId.setText(idParticipantes[0:-2])
        self.dashboard.loading(80)
        self.enviarEmail.leNome.setText(nomeParticipantes[0:-2])
        self.dashboard.loading(90)
        self.enviarEmail.leEmail.setText(emailParticipantes[0:-2])
        self.dashboard.loading(100)

        self.enviarEmail.show()

    def defineCategoriaNomeStyle(self):
        self.lbCategoria.setText(self.grupo.nomeCategoria)
        self.lbCategoria.setStyleSheet(labelCard(categoriaColor="black"))
        self.frCategoria.setStyleSheet(frameCategoriaCard(categoriaColor=self.grupo.corCategoria))

