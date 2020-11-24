# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dashAgenda.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_wdgAgenda(QtWidgets.QWidget):

    # ----------------------------------
    def __init__(self, parent=None):
        super(Ui_wdgAgenda, self).__init__()
        self.setupUi(self)
    # ----------------------------------

    def setupUi(self, wdgAgenda):
        wdgAgenda.setObjectName("wdgAgenda")
        wdgAgenda.resize(800, 588)
        self.gridLayout = QtWidgets.QGridLayout(wdgAgenda)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(wdgAgenda)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calendarWidget.sizePolicy().hasHeightForWidth())
        self.calendarWidget.setSizePolicy(sizePolicy)
        self.calendarWidget.setMinimumSize(QtCore.QSize(500, 550))
        self.calendarWidget.setMaximumSize(QtCore.QSize(1000, 16777215))
        self.calendarWidget.setSizeIncrement(QtCore.QSize(0, 0))
        self.calendarWidget.setStyleSheet("background-color: rgb(108, 251, 208);")
        self.calendarWidget.setObjectName("calendarWidget")
        self.horizontalLayout.addWidget(self.calendarWidget)
        self.frCompromisso = QtWidgets.QFrame(self.frame)
        self.frCompromisso.setMinimumSize(QtCore.QSize(210, 0))
        self.frCompromisso.setStyleSheet("#frCompromisso{\n"
"background-color: transparent;\n"
"border-left: 3px dashed rgb(108, 251, 208);\n"
"border-right: 3px dashed rgb(108, 251, 208);\n"
"}")
        self.frCompromisso.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frCompromisso.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frCompromisso.setObjectName("frCompromisso")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frCompromisso)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.frCompromisso)
        font = QtGui.QFont()
        font.setFamily("Fira Sans ExtraLight")
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(108, 251, 208);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 1, 1, 1, 1)
        self.horizontalLayout.addWidget(self.frCompromisso)
        self.gridLayout.addWidget(self.frame, 0, 2, 1, 1)

        self.retranslateUi(wdgAgenda)
        QtCore.QMetaObject.connectSlotsByName(wdgAgenda)

    def retranslateUi(self, wdgAgenda):
        _translate = QtCore.QCoreApplication.translate
        wdgAgenda.setWindowTitle(_translate("wdgAgenda", "Form"))
        self.label.setText(_translate("wdgAgenda", "Compromissos"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    wdgAgenda = QtWidgets.QWidget()
    ui = Ui_wdgAgenda()
    ui.setupUi(wdgAgenda)
    wdgAgenda.show()
    sys.exit(app.exec_())