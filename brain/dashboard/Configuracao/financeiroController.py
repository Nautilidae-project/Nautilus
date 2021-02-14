from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget

from Telas.tabFinanceiro import Ui_tabFinanceiroGeral
from brain.DAOs.daoPlanos import DaoPlanos


class FinanceiroController(Ui_tabFinanceiroGeral, QWidget):

    def __init__(self, parent=None, db=None):
        super(FinanceiroController, self).__init__(parent)
        self.db = db
        self.parent = parent
        self.dashboard = parent.parent
        self.setupUi(self)
        self.daoPlanos = DaoPlanos(db=db)

        self.pbInserir.clicked.connect(self.verificaCampos)
        self.pbCancelar.clicked.connect(self.limpaCampos)

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

    def limpaCampos(self):
        self.leValor.clear()
        self.leNomePlano.clear()
        self.teDescricaoPlano.clear()
        self.cbPresencial.setChecked(False)




if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = FinanceiroController()
    ui.show()
    sys.exit(app.exec_())