# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telaTeste.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_wdgBackground(object):
    def setupUi(self, wdgBackground):
        wdgBackground.setObjectName("wdgBackground")
        wdgBackground.resize(870, 619)
        wdgBackground.setStyleSheet("#wdgBackground{\n"
"    background-color: qlineargradient(spread:pad, x1:0.493, y1:0, x2:0.498, y2:1, stop:0.0895522 rgba(54, 153, 148, 185), stop:0.930348 rgba(255, 189, 144, 255))\n"
"}")
        self.horizontalLayout = QtWidgets.QHBoxLayout(wdgBackground)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.fr1 = QtWidgets.QFrame(wdgBackground)
        self.fr1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr1.setObjectName("fr1")
        self.pb1 = QtWidgets.QPushButton(self.fr1)
        self.pb1.setGeometry(QtCore.QRect(150, 220, 89, 25))
        self.pb1.setObjectName("pb1")
        self.horizontalLayout.addWidget(self.fr1)
        self.fr2 = QtWidgets.QFrame(wdgBackground)
        self.fr2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr2.setObjectName("fr2")
        self.pb2 = QtWidgets.QPushButton(self.fr2)
        self.pb2.setGeometry(QtCore.QRect(120, 230, 89, 25))
        self.pb2.setObjectName("pb2")
        self.horizontalLayout.addWidget(self.fr2)

        self.retranslateUi(wdgBackground)
        QtCore.QMetaObject.connectSlotsByName(wdgBackground)

    def retranslateUi(self, wdgBackground):
        _translate = QtCore.QCoreApplication.translate
        wdgBackground.setWindowTitle(_translate("wdgBackground", "Form"))
        self.pb1.setText(_translate("wdgBackground", "pb1"))
        self.pb2.setText(_translate("wdgBackground", "pb2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    wdgBackground = QtWidgets.QWidget()
    ui = Ui_wdgBackground()
    ui.setupUi(wdgBackground)
    wdgBackground.show()
    sys.exit(app.exec_())
