from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSignal
from Telas.tabClientes import Ui_wdgClientes


class brainTabClientes(Ui_wdgClientes, QMainWindow):
    home = pyqtSignal()

    def __init__(self, parent=None):
        super(brainTabClientes, self).__init__(parent)
        self.setupUi(self)
