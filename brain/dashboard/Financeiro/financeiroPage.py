from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal, QPropertyAnimation

from Telas.dashFinanceiro import Ui_wdgFinanceiro

class FinanceiroPage(Ui_wdgFinanceiro, QWidget):
    home = pyqtSignal()

    def __init__(self, parent=None, db=None):
        super(FinanceiroPage, self).__init__(parent)
        self.setupUi(self)
        self.db = db

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = FinanceiroPage()
    ui.show()
    sys.exit(app.exec_())