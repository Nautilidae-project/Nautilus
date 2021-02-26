from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal, QPropertyAnimation

from datetime import datetime, timedelta
import pandas as pd

from Telas.dashFinanceiro import Ui_wdgFinanceiro
from brain.DAOs.daoFinanceiro import DaoFinanceiro
from brain.DAOs.daoPlanos import DaoPlanos


class FinanceiroPage(Ui_wdgFinanceiro, QWidget):
    home = pyqtSignal()

    def __init__(self, parent=None, db=None):
        super(FinanceiroPage, self).__init__(parent)
        self.setupUi(self)
        self.db = db
        self.daoFinanceiro = DaoFinanceiro(db=db)
        self.daoPlanos = DaoPlanos(db=db)

        self.calculaFaturamento(datetime(2020, 1, 10), datetime(2021, 1, 1))

    def calculaFaturamento(self, dataInicial: datetime, dataFinal: datetime):

        valores = self.daoFinanceiro.getFaturamentoMensal()
        itemReceita = {
            'nomePlano': [],
            'valor': [],
            'qtdInscritos': [],
            'dataInicio': [],
            'dataFim': []
        }

        for index in range(0, len(valores)-1):
            itemReceita['nomePlano'].append(valores[index][0])
            itemReceita['valor'].append(valores[index][1])
            itemReceita['qtdInscritos'].append(valores[index][2])
            itemReceita['dataInicio'].append(valores[index][3].date())
            itemReceita['dataFim'].append(valores[index][4].date())

        dfTotal = pd.DataFrame.from_dict(itemReceita)

        print(dfTotal.head())

        hoje = datetime.now().date()
        for mes in range(6):
            soma = 0
            for nomePlano, valor, qtdInscritos, dataInicio, dataFim in zip(itemReceita['nomePlano'], itemReceita['valor'], itemReceita['qtdInscritos'], itemReceita['dataInicio'], itemReceita['dataFim']):
                if dataInicio < hoje < dataFim:
                    print(nomePlano)
                    soma += round(float(valor)*float(qtdInscritos), 2)

            print(f"Mês: {hoje.month} - Faturamento: {soma}")
            hoje += timedelta(days=30)


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = FinanceiroPage()
    ui.show()
    sys.exit(app.exec_())