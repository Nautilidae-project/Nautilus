from PyQt5.QtCore import QObject
from PyQt5 import QtCore


class Sinais(QObject):
    sBackLoginPage = QtCore.pyqtSignal()
    sResizeWindow = QtCore.pyqtSignal()
    sAtualizarTela = QtCore.pyqtSignal()