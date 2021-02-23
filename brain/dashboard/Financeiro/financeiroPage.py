from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal, QPropertyAnimation

import pandas as pd

from Telas.dashFinanceiro import Ui_wdgFinanceiro
from brain.DAOs.daoFinanceiro import DaoFinanceiro


class FinanceiroPage(Ui_wdgFinanceiro, QWidget):
    home = pyqtSignal()

    def __init__(self, parent=None, db=None):
        super(FinanceiroPage, self).__init__(parent)
        self.setupUi(self)
        self.db = db
        self.daoFinanceiro = DaoFinanceiro(db=db)

        self.calculaFaturamento()

    def calculaFaturamento(self):
        valores = self.daoFinanceiro.getFaturamentoMensal()
        itemReceita = {
            'valor': [],
            'dataCadastro': []
        }

        # print(len(*valores))
        # index, valor, dataCadastro

        for index in range(0, len(valores)-1):
            itemReceita['valor'].append(valores[index][0])
            itemReceita['dataCadastro'].append(valores[index][1].date())

        df = pd.DataFrame.from_dict(itemReceita)
        groupDate = df.groupby(by='dataCadastro')

        for g in groupDate:
            print(g)


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = FinanceiroPage()
    ui.show()
    sys.exit(app.exec_())