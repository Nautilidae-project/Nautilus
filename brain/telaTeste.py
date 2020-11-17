from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSignal
from Telas.telaTeste import Ui_wdgBackground


class telaTeste(Ui_wdgBackground, QMainWindow):
    home = pyqtSignal()

    def __init__(self, parent=None):
        super(telaTeste, self).__init__(parent)
        self.setupUi(self)
