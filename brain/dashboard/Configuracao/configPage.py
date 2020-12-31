from PyQt5.QtWidgets import QWidget

from Telas.dashConfig import Ui_wdgConfig


class ConfigPage(Ui_wdgConfig, QWidget):
    def __init__(self, parent=None):
        super(ConfigPage, self).__init__(parent)

        self.setupUi(self)
