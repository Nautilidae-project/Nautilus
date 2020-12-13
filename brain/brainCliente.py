from PyQt5.QtWidgets import QWidget, QTableWidgetItem
from PyQt5.QtCore import pyqtSignal
from PyQt5.Qt import Qt
from Telas.dashCliente import Ui_wdgCliente
from brain.DAOs.daoCliente import findAll, buscaCliente
from modelos.cliente import ClientTableModel


class brainCliente(Ui_wdgCliente, QWidget):
    home = pyqtSignal()

    def __init__(self, parent=None):
        super(brainCliente, self).__init__(parent)
        self.setupUi(self)

        self.pbFuncionalidade1.clicked.connect(self.atualizaTabela)
        self.atualizaTabela()

        self.leSearchCliente.textEdited.connect(lambda: self.busca())

    def busca(self):
        print(self.leSearchCliente.text())

        clientes = buscaCliente(self.leSearchCliente.text())

        self.tblClientes.setRowCount(0)

        for rowCount, rowData in enumerate(clientes):
            self.tblClientes.insertRow(rowCount)
            for columnNumber, data in enumerate(rowData):
                self.tblClientes.setItem(rowCount, columnNumber, QTableWidgetItem(str(data)))
                print(f'Count -> {rowCount}     rowData -> {rowData}      columnNumber -> {columnNumber}     Data -> {data} ')

        self.tblClientes.resizeColumnsToContents()

    def atualizaTabela(self):
        clientes = findAll()
        self.tblClientes.setRowCount(0)

        for rowCount, rowData in enumerate(clientes):
            self.tblClientes.insertRow(rowCount)
            for columnNumber, data in enumerate(rowData):
                self.tblClientes.setItem(rowCount, columnNumber, QTableWidgetItem(str(data)))

        self.tblClientes.resizeColumnsToContents()
