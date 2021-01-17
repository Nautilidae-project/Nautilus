# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cardGrupo1.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_wdgGrupoCard(object):
    def setupUi(self, wdgGrupoCard):
        wdgGrupoCard.setObjectName("wdgGrupoCard")
        wdgGrupoCard.resize(300, 200)
        wdgGrupoCard.setMinimumSize(QtCore.QSize(200, 200))
        wdgGrupoCard.setMaximumSize(QtCore.QSize(300, 200))
        wdgGrupoCard.setStyleSheet("/*#wdgGrupoCard {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(105, 33, 140, 60), stop:1 rgba(112, 237, 255, 60));    \n"
"}*/")
        self.verticalLayout = QtWidgets.QVBoxLayout(wdgGrupoCard)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frGrupoCard = QtWidgets.QFrame(wdgGrupoCard)
        self.frGrupoCard.setStyleSheet("#frGrupoCard {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(105, 33, 140, 60), stop:1 rgba(112, 237, 255, 60));    \n"
"}")
        self.frGrupoCard.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frGrupoCard.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frGrupoCard.setObjectName("frGrupoCard")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frGrupoCard)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lbTituloCard = QtWidgets.QLabel(self.frGrupoCard)
        self.lbTituloCard.setMinimumSize(QtCore.QSize(0, 50))
        self.lbTituloCard.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lbTituloCard.setFont(font)
        self.lbTituloCard.setStyleSheet("#lbTituloCard{\n"
"    background-color: rgba(211, 215, 207, 0);\n"
"}")
        self.lbTituloCard.setObjectName("lbTituloCard")
        self.verticalLayout_2.addWidget(self.lbTituloCard)
        self.lbDescricao = QtWidgets.QLabel(self.frGrupoCard)
        self.lbDescricao.setMinimumSize(QtCore.QSize(0, 24))
        self.lbDescricao.setMaximumSize(QtCore.QSize(16777215, 24))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(12)
        self.lbDescricao.setFont(font)
        self.lbDescricao.setStyleSheet("#lbDescricao{\n"
"    background-color: rgba(211, 215, 207, 0);\n"
"}")
        self.lbDescricao.setObjectName("lbDescricao")
        self.verticalLayout_2.addWidget(self.lbDescricao)
        self.pb1 = QtWidgets.QPushButton(self.frGrupoCard)
        self.pb1.setStyleSheet("#pb1{\n"
"    background-color: rgba(211, 215, 207, 0);\n"
"}")
        self.pb1.setObjectName("pb1")
        self.verticalLayout_2.addWidget(self.pb1)
        self.pb2 = QtWidgets.QPushButton(self.frGrupoCard)
        self.pb2.setStyleSheet("#pb2{\n"
"    background-color: rgba(211, 215, 207, 0);\n"
"}")
        self.pb2.setObjectName("pb2")
        self.verticalLayout_2.addWidget(self.pb2)
        self.verticalLayout.addWidget(self.frGrupoCard)

        self.retranslateUi(wdgGrupoCard)
        QtCore.QMetaObject.connectSlotsByName(wdgGrupoCard)

    def retranslateUi(self, wdgGrupoCard):
        _translate = QtCore.QCoreApplication.translate
        wdgGrupoCard.setWindowTitle(_translate("wdgGrupoCard", "Form"))
        self.lbTituloCard.setText(_translate("wdgGrupoCard", "Titulo"))
        self.lbDescricao.setText(_translate("wdgGrupoCard", "Descrição"))
        self.pb1.setText(_translate("wdgGrupoCard", "PushButton"))
        self.pb2.setText(_translate("wdgGrupoCard", "PushButton"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    wdgGrupoCard = QtWidgets.QWidget()
    ui = Ui_wdgGrupoCard()
    ui.setupUi(wdgGrupoCard)
    wdgGrupoCard.show()
    sys.exit(app.exec_())
