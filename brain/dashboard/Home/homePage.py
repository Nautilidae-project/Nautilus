from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget

from Telas.dashHome import Ui_wdgHome


class HomePage(Ui_wdgHome, QWidget):
    def __init__(self, parent=None):
        super(HomePage, self).__init__(parent)

        self.setupUi(self)


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = HomePage()
    ui.show()
    sys.exit(app.exec_())