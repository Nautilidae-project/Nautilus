from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QTableWidgetItem
from PyQt5.QtCore import QDateTime

from datetime import datetime

from Telas.tabFinanceiro import Ui_tabFinanceiroGeral
from brain.DAOs.daoPlanos import DaoPlanos
from modelos.planoModel import PlanoModelo


class FinanceiroController(Ui_tabFinanceiroGeral, QWidget):

    def __init__(self, parent=None, db=None):
        super(FinanceiroController, self).__init__(parent)
        self.db = db
        self.parent = parent
        self.dashboard = parent.parent
        self.plano = PlanoModelo()
        self.setupUi(self)
        self.daoPlanos = DaoPlanos(db=db)

        self.tblPlanos.setColumnHidden(0, True)

        self.carregaTabelaPlanos()

        self.pbInserir.clicked.connect(lambda: self.inserePlano() if self.verificaCampos() else None)
        self.pbCancelar.clicked.connect(self.limpaCampos)
        self.cbInativos.setChecked(True)

        self.leValor.textEdited.connect(lambda: self.definePlano('valor'))
        self.leNomePlano.textEdited.connect(lambda: self.definePlano('nomePlano'))
        self.cbxFreq.currentTextChanged.connect(lambda: self.definePlano('frequencia'))
        self.dtInicio.dateChanged.connect(lambda: self.definePlano('dataInicio'))
        self.dtTermino.dateChanged.connect(lambda: self.definePlano('dataFim'))
        self.cbPresencial.stateChanged.connect(lambda: self.definePlano('presencial'))
        self.teDescricaoPlano.textChanged.connect(lambda: self.definePlano('descricao'))

        self.cbInativos.stateChanged.connect(lambda: self.recarregaTabela(ativo=self.cbInativos.isChecked()))

        self.cbxFreq.addItems(['Semanal', 'Mensal'])

    def verificaCampos(self):
        if self.leValor.text().strip() == '':
            self.dashboard.menssagemSistema('É preciso definir um valor para o plano')
            return False
        elif self.leNomePlano.text().strip() == '':
            self.dashboard.menssagemSistema('É preciso definir um nome para o plano')
            return False
        else:
            return True

    def definePlano(self, campo: str):

        if campo == 'valor':
            self.plano.valor = float(self.leValor.text().replace(',', '.'))
        elif campo == 'nomePlano':
            self.plano.nomePlano = self.leNomePlano.text()
        elif campo == 'frequencia':
            self.plano.periodoUnidade = self.cbxFreq.currentText()
        elif campo == 'dataInicio':
            self.plano.dataInicio = self.dtInicio.date().toPyDate()
        elif campo == 'dataFim':
            self.plano.dataFim = self.dtTermino.date().toPyDate()
        elif campo == 'descricao':
            self.plano.descricao = self.teDescricaoPlano.toPlainText()
        elif campo == 'presencial':
            self.plano.presencial = self.cbPresencial.isChecked()

    def inserePlano(self):
        self.dashboard.loading(20)
        self.plano.dataInicio = self.dtInicio.date().toPyDate()
        self.plano.dataFim = self.dtTermino.date().toPyDate()
        self.plano.periodoUnidade = self.cbxFreq.currentText()
        print(f"self.cbxFreq.currentText(): {self.cbxFreq.currentText()}")
        self.dashboard.loading(45)

        if self.daoPlanos.inserePlano(self.plano):
            self.dashboard.menssagemSistema('Plano cadastrado com sucesso!')
            self.limpaCampos()
            self.recarregaTabela(ativo=self.cbInativos.isChecked())
            self.dashboard.loading(100)
            self.plano = PlanoModelo()
        else:
            self.dashboard.menssagemSistema('O plano não pode ser inserido. Tente novamente.')
            self.dashboard.loading(100)

    def carregaTabelaPlanos(self, ativo: bool = True):
        infoPlanos = self.daoPlanos.getAll(ativo=ativo)

        self.tblPlanos.setRowCount(0)

        for numLinha, infoLinha in enumerate(infoPlanos):
            self.tblPlanos.insertRow(numLinha)
            for numCol, infoCol in enumerate(infoLinha):

                if numCol == 1:
                    strItem = QTableWidgetItem(str(infoCol))
                    strItem.setFont(QFont('Ubuntu', pointSize=12, italic=True, weight=25))
                    self.tblPlanos.setItem(numLinha, numCol, strItem)

                elif numCol == 2:
                    strItem = QTableWidgetItem(str(f"R$ {infoCol}"))
                    strItem.setFont(QFont('Ubuntu', pointSize=12, italic=True, weight=25))
                    self.tblPlanos.setItem(numLinha, numCol, strItem)

                elif numCol == 3:
                    strItem = QTableWidgetItem(str(infoCol.title()))
                    strItem.setFont(QFont('Ubuntu', pointSize=12, italic=True, weight=25))
                    self.tblPlanos.setItem(numLinha, numCol, strItem)

                elif numCol == 4:
                    strItem = QTableWidgetItem(f'{infoLinha[8]}')
                    strItem.setFont(QFont('Ubuntu', pointSize=12, italic=True, weight=25))
                    self.tblPlanos.setItem(numLinha, numCol, strItem)

        self.tblPlanos.resizeColumnsToContents()

    def limpaCampos(self):
        self.leValor.clear()
        self.leNomePlano.clear()
        self.teDescricaoPlano.clear()
        self.cbPresencial.setChecked(False)

    def recarregaTabela(self, ativo=False):
        self.carregaTabelaPlanos(ativo=ativo)





if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = FinanceiroController()
    ui.show()
    sys.exit(app.exec_())