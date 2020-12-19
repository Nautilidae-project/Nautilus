import base64

from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QMessageBox, QCheckBox
from PyQt5.QtWidgets import QWidget, QTableWidgetItem
from PyQt5.QtCore import pyqtSignal

from Telas.dashCliente import Ui_wdgCliente
from brain.DAOs.daoCliente import findAll, buscaPorId
from brain.delegates.alinhamento import AlinhamentoDelegate
from brain.funcoesAuxiliares import mascaraCelular, macaraFormaPagamento, isTrueBool, isTrueInt
from modelos.cliente import Cliente
from brain.DAOs.daoCliente import findAll, buscaCliente



class brainCliente(Ui_wdgCliente, QWidget):
    home = pyqtSignal()

    def __init__(self, parent=None):
        super(brainCliente, self).__init__(parent)
        self.setupUi(self)
        self.cliente = Cliente()

        self.pbFuncionalidade1.clicked.connect(self.atualizaTabela)
        self.atualizaTabela()
        self.frInfoCliente.hide()
        self.tblClientes.setColumnHidden(0, True)
        self.tblClientes.setItemDelegate(AlinhamentoDelegate())

        self.pbConfirmarAtualizacao.clicked.connect(lambda: self.showPopup('As atualizações podem ser efetivadas?\nEssa ação não pode ser desfeita.'))
        self.leSearchCliente.textEdited.connect(lambda: self.busca())

        self.tblClientes.doubleClicked.connect(self.carregaInfoCliente)

    def busca(self):
        clientes = buscaCliente(self.leSearchCliente.text())

        self.atualizaTabela(clientes)

    def atualizaTabela(self, clientes=None):

        if clientes is None:
            clientes = findAll()

        self.tblClientes.setRowCount(0)

        for rowCount, rowData in enumerate(clientes):
            self.tblClientes.insertRow(rowCount)
            for columnNumber, data in enumerate(rowData):
                if columnNumber == 2:
                    self.tblClientes.setItem(rowCount, columnNumber, QTableWidgetItem(str(mascaraCelular(data))))
                elif columnNumber == 3:
                    self.tblClientes.setItem(rowCount, columnNumber, QTableWidgetItem(str(macaraFormaPagamento(data))))
                elif columnNumber == 4:
                    cbItemTbl = QTableWidgetItem()
                    cbItemTbl.setFlags(QtCore.Qt.ItemIsEnabled)
                    cbItemTbl.setText('')

                    if isTrueBool(data):
                        cbItemTbl.setCheckState(QtCore.Qt.Unchecked)
                    else:
                        cbItemTbl.setCheckState(QtCore.Qt.Checked)
                    self.tblClientes.setItem(rowCount, columnNumber, cbItemTbl)
                else:
                    self.tblClientes.setItem(rowCount, columnNumber, QTableWidgetItem(str(data)))

        self.tblClientes.resizeColumnsToContents()

    def carregaInfoCliente(self, *args):
        intClienteId = int(self.tblClientes.item(args[0].row(), 0).text())
        listCliente = buscaPorId(intClienteId)[0]
        if len(listCliente) == 0:
            print('Não encontrei o cliente')
        # elif len(listCliente) > 1:
        #     print('O SELECT trouxe mais do que um cliente')
        else:
            self.cliente.clienteId = listCliente[0]
            self.cliente.nomeCliente = listCliente[1]
            self.cliente.sobrenomeCliente = listCliente[2]
            self.cliente.telefone = listCliente[3]
            self.cliente.email = listCliente[4]
            self.cliente.cpf = listCliente[5]
            self.cliente.endereco = listCliente[6]
            self.cliente.complemento = listCliente[7]
            self.cliente.cep = listCliente[8]
            self.cliente.bairro = listCliente[9]
            self.cliente.meioPagamento = listCliente[10]
            self.cliente.ativo = isTrueInt(listCliente)

            self.leInfoNome.setText(self.cliente.nomeCliente)
            self.leInfoSobrenome.setText(self.cliente.sobrenomeCliente)
            self.leInfoTel.setText(self.cliente.telefone)
            self.leInfoEmail.setText(self.cliente.email)
            self.leInfoCpf.setText(self.cliente.cpf)
            self.leInfoEndereco.setText(self.cliente.endereco)
            self.leInfoComplemento.setText(self.cliente.complemento)
            self.leInfoCep.setText(self.cliente.cep)
            self.leInfoBairro.setText(self.cliente.bairro)
            # self.leInfoMeioPag.setText(self.cliente.meioPagamento)
            self.cbInfoAtivo.setChecked(self.cliente.ativo)

            self.frInfoCliente.show()

    # def trataAtualização(self):
    #     dictLinesEdit = {
    #         'Nome': self.leInfoNome,
    #         'Sobrenome': self.leInfoSobrenome,
    #         'Telefone': self.leInfoTel,
    #         'Email':  self.leInfoEmail,
    #         'CPF': self.leInfoCpf,
    #         'Endereco': self.leInfoEndereco,
    #         'Complemento': self.leInfoComplemento,
    #         'CEP': self.leInfoCep,
    #         'Bairro': self.leInfoBairro,
    #         'Ativo': self.cbInfoAtivo
    #     }
    #     for chave, valor in dictLinesEdit.values():
    #         if len(valor.text()) == 0:


    def atualizaCliente(self, *args):
        print(f'args[0] == QMessageBox.Yes: {args[0]}')

    def animationInfo(self):
        pass

    def showPopup(self, mensagem, titulo='Atenção!'):
        dialogPopup = QMessageBox()
        dialogPopup.setWindowTitle(titulo)
        dialogPopup.setText(mensagem)
        dialogPopup.setIcon(QMessageBox.Warning)
        dialogPopup.setStandardButtons(QMessageBox.Cancel | QMessageBox.Yes)

        dialogPopup.buttonClicked.connect(self.atualizaCliente)
        close = dialogPopup.exec_()



