import base64

from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QMessageBox
from PyQt5.QtCore import pyqtSignal, Qt
from Telas.dashCliente import Ui_wdgCliente
from brain.DAOs.daoCliente import findAll, buscaPorId
from brain.funcoesAuxiliares import mascaraCelular, macaraFormaPagamento
from modelos.cliente import Cliente


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

        self.pbConfirmarAtualizacao.clicked.connect(lambda: self.showPopup('As atualizações podem ser efetivadas?\nEssa ação não pode ser desfeita.'))

        self.tblClientes.doubleClicked.connect(self.carregaInfoCliente)

    def atualizaTabela(self):
        clientes = findAll()
        self.tblClientes.setRowCount(0)

        for rowCount, rowData in enumerate(clientes):
            self.tblClientes.insertRow(rowCount)
            for columnNumber, data in enumerate(rowData):
                if columnNumber == 2:
                    self.tblClientes.setItem(rowCount, columnNumber, QTableWidgetItem(str(mascaraCelular(data))))
                elif columnNumber == 3:
                    self.tblClientes.setItem(rowCount, columnNumber, QTableWidgetItem(str(macaraFormaPagamento(data))))
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
            if [bool(i) for i in listCliente[11]][0]:
                self.cliente.ativo = 1
            else:
                self.cliente.ativo = 0

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
        print(args[0] == QMessageBox.Yes)

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



