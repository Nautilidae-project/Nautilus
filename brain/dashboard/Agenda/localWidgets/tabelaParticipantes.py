from PyQt5 import QtCore
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QRadioButton, QApplication, QTableWidgetItem
from PyQt5.uic.properties import QtWidgets

from Telas.tabelaParticipantes import Ui_wdgParticipantes
from brain.DAOs.daoCategoria import DaoCategoria
from brain.DAOs.daoCliente import DaoCliente
from brain.dashboard.Configuracao.localStyleSheets.CardCategoria import colors, botoesStyleSheet
from modelos.categoriaModel import CategoriaModel
from modelos.efeitosModel import Efeitos


class TabelaParticipantes(Ui_wdgParticipantes, QWidget):

    def __init__(self, parent=None, db=None):
        super(TabelaParticipantes, self).__init__(parent)
        self.setupUi(self)
        self.db = db
        self.parent = parent

        self.efeitos = Efeitos()

        self.daoCliente = DaoCliente(self.db)

        self.populaTblParticipantes()
        self.tblClientes.setColumnHidden(0, True)
        # self.tblClientes.clicked.connect(self.check)
        self.tblClientes.cellClicked.connect(self.check)
        self.tblClientes.itemChanged.connect(self.itemChanged)

    def flags(self, index):
        if not index.isValid():
            return None

        if index.column() == 3:
            return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsUserCheckable
        else:
            return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable

    def check(self, linha, _):
        cliente = self.tblClientes
        print(cliente.column)
        # for i in range(self.tblClientes.rowCount()):
        #     print(i)

        # print(cliente.item(row, 0).text())
        # if self.tblClientes.item(row, 3).checkState():
        #     print('Check')


        # Potenciaç
        # print(cliente.hideRow(linha))


    def itemChanged(self, item):
        print("Item {!r} checkState: {}".format(item.text(), item.checkState()))

    def populaTblParticipantes(self):

        listaClientes = self.daoCliente.findAllNomeSobrenome()

        self.tblClientes.setRowCount(0)

        for linhaNum, conteudoLinha in enumerate(listaClientes):
            self.tblClientes.insertRow(linhaNum)

            for colunaNum, data in enumerate(conteudoLinha):
                if colunaNum == 3:
                    cbItemParticipante = QTableWidgetItem()
                    cbItemParticipante.setFlags(
                        QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsUserCheckable)
                    cbItemParticipante.setCheckState(QtCore.Qt.Unchecked)
                    self.tblClientes.setItem(linhaNum, colunaNum, cbItemParticipante)
                else:
                    strItem = QTableWidgetItem(str(data))
                    strItem.setFont(QFont('Ubuntu', pointSize=12, italic=True, weight=25))
                    self.tblClientes.setItem(linhaNum, colunaNum, strItem)

        self.tblClientes.resizeColumnsToContents()


if __name__ == '__main__':
    import sys
    import pymysql
    from configBD import ConfigDB

    app = QApplication(sys.argv)
    # db = getDB()
    config = ConfigDB(carregaBanco=True)
    db = pymysql.connect(
        host=config.host,
        user=config.user,
        passwd=config.passwd,
        db=config.banco,
        port=config.port
    )
    ui = TabelaParticipantes(db=db)
    ui.show()
    sys.exit(app.exec_())
