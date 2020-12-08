from PyQt5.QtWidgets import QWidget, QTableWidgetItem
from PyQt5.QtCore import pyqtSignal
from Telas.dashCliente import Ui_wdgCliente
from brain.DAOs.daoCliente import findAll
from modelos.cliente import ClientTableModel


class brainCliente(Ui_wdgCliente, QWidget):
    home = pyqtSignal()

    def __init__(self, parent=None):
        super(brainCliente, self).__init__(parent)
        self.setupUi(self)

        self.pbFuncionalidade1.clicked.connect(self.atualizaTabela)
        self.atualizaTabela()


    def atualizaTabela(self):
        clientes = findAll()
        colunasTbl = ['Nome do Cliente', 'Telefone', 'Meio de Pagamento', 'Ativo']
        self.tblClientes.setRowCount(0)

        for rowCount, rowData in enumerate(clientes):
            self.tblClientes.insertRow(rowCount)
            for columnNumber, data in enumerate(rowData):
                self.tblClientes.setItem(rowCount, columnNumber, QTableWidgetItem(str(data)))

        self.tblClientes.resizeColumnsToContents()
