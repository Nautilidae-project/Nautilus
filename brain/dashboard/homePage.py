from PyQt5.QtWidgets import QWidget

from Telas.dashHome import Ui_wdgHome


class HomePage(Ui_wdgHome, QWidget):
    def __init__(self, parent=None):
        super(HomePage, self).__init__(parent)

        self.setupUi(self)