# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dashHome.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_wdgHome(object):
    def setupUi(self, wdgHome):
        wdgHome.setObjectName("wdgHome")
        wdgHome.resize(970, 718)
        self.gridLayout = QtWidgets.QGridLayout(wdgHome)
        self.gridLayout.setObjectName("gridLayout")
        self.frCompromisso = QtWidgets.QFrame(wdgHome)
        self.frCompromisso.setMinimumSize(QtCore.QSize(260, 700))
        self.frCompromisso.setStyleSheet("#frCompromisso{\n"
"    \n"
"    background-color: rgb(114, 159, 207);\n"
"}\n"
"\n"
"#leCard1Compromiso, #leCard2Compromiso, #leCard3Compromiso, #leCard4Compromiso  {\n"
"    \n"
"    background-color: rgb(120, 200, 190);\n"
"}")
        self.frCompromisso.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frCompromisso.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frCompromisso.setObjectName("frCompromisso")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frCompromisso)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.leCard3Compromiso = QtWidgets.QLabel(self.frCompromisso)
        self.leCard3Compromiso.setObjectName("leCard3Compromiso")
        self.gridLayout_2.addWidget(self.leCard3Compromiso, 4, 0, 1, 1)
        self.leCard4Compromiso = QtWidgets.QLabel(self.frCompromisso)
        self.leCard4Compromiso.setObjectName("leCard4Compromiso")
        self.gridLayout_2.addWidget(self.leCard4Compromiso, 5, 0, 1, 1)
        self.leCard1Compromiso = QtWidgets.QLabel(self.frCompromisso)
        self.leCard1Compromiso.setObjectName("leCard1Compromiso")
        self.gridLayout_2.addWidget(self.leCard1Compromiso, 1, 0, 1, 1)
        self.leInfoCompromisso = QtWidgets.QLabel(self.frCompromisso)
        self.leInfoCompromisso.setMinimumSize(QtCore.QSize(0, 150))
        self.leInfoCompromisso.setMaximumSize(QtCore.QSize(16777215, 150))
        self.leInfoCompromisso.setObjectName("leInfoCompromisso")
        self.gridLayout_2.addWidget(self.leInfoCompromisso, 0, 0, 1, 1)
        self.leCard2Compromiso = QtWidgets.QLabel(self.frCompromisso)
        self.leCard2Compromiso.setObjectName("leCard2Compromiso")
        self.gridLayout_2.addWidget(self.leCard2Compromiso, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.frCompromisso, 0, 0, 1, 1)
        self.frFinanceiro = QtWidgets.QFrame(wdgHome)
        self.frFinanceiro.setMinimumSize(QtCore.QSize(260, 700))
        self.frFinanceiro.setStyleSheet("#frFinanceiro {\n"
"    \n"
"    background-color: rgb(173, 127, 168);\n"
"}\n"
"\n"
"#leCard1Financeiro, #leCard2Financeiro, #leCard3Financeiro, #leCard4Financeiro {\n"
"    \n"
"    background-color: rgb(183, 137, 158);\n"
"}\n"
"")
        self.frFinanceiro.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frFinanceiro.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frFinanceiro.setObjectName("frFinanceiro")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frFinanceiro)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.leInfoFinanceiro = QtWidgets.QLabel(self.frFinanceiro)
        self.leInfoFinanceiro.setMinimumSize(QtCore.QSize(0, 150))
        self.leInfoFinanceiro.setMaximumSize(QtCore.QSize(16777215, 150))
        self.leInfoFinanceiro.setObjectName("leInfoFinanceiro")
        self.gridLayout_3.addWidget(self.leInfoFinanceiro, 0, 0, 1, 1)
        self.leCard1Financeiro = QtWidgets.QLabel(self.frFinanceiro)
        self.leCard1Financeiro.setObjectName("leCard1Financeiro")
        self.gridLayout_3.addWidget(self.leCard1Financeiro, 1, 0, 1, 1)
        self.leCard2Financeiro = QtWidgets.QLabel(self.frFinanceiro)
        self.leCard2Financeiro.setObjectName("leCard2Financeiro")
        self.gridLayout_3.addWidget(self.leCard2Financeiro, 2, 0, 1, 1)
        self.leCard3Financeiro = QtWidgets.QLabel(self.frFinanceiro)
        self.leCard3Financeiro.setObjectName("leCard3Financeiro")
        self.gridLayout_3.addWidget(self.leCard3Financeiro, 3, 0, 1, 1)
        self.leCard4Financeiro = QtWidgets.QLabel(self.frFinanceiro)
        self.leCard4Financeiro.setObjectName("leCard4Financeiro")
        self.gridLayout_3.addWidget(self.leCard4Financeiro, 4, 0, 1, 1)
        self.gridLayout.addWidget(self.frFinanceiro, 0, 1, 1, 1)
        self.frCalendario = QtWidgets.QFrame(wdgHome)
        self.frCalendario.setStyleSheet("#frCalendario {\n"
"    \n"
"    background-color: rgb(233, 185, 110);\n"
"}")
        self.frCalendario.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frCalendario.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frCalendario.setObjectName("frCalendario")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frCalendario)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.leInfoFinanceiro_2 = QtWidgets.QLabel(self.frCalendario)
        self.leInfoFinanceiro_2.setMinimumSize(QtCore.QSize(0, 150))
        self.leInfoFinanceiro_2.setMaximumSize(QtCore.QSize(16777215, 150))
        self.leInfoFinanceiro_2.setObjectName("leInfoFinanceiro_2")
        self.gridLayout_4.addWidget(self.leInfoFinanceiro_2, 0, 0, 1, 1)
        self.calendarWidget = QtWidgets.QCalendarWidget(self.frCalendario)
        self.calendarWidget.setMinimumSize(QtCore.QSize(400, 300))
        self.calendarWidget.setMaximumSize(QtCore.QSize(400, 300))
        self.calendarWidget.setObjectName("calendarWidget")
        self.gridLayout_4.addWidget(self.calendarWidget, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.frCalendario)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.frCalendario, 0, 2, 1, 1)

        self.retranslateUi(wdgHome)
        QtCore.QMetaObject.connectSlotsByName(wdgHome)

    def retranslateUi(self, wdgHome):
        _translate = QtCore.QCoreApplication.translate
        wdgHome.setWindowTitle(_translate("wdgHome", "Form"))
        self.leCard3Compromiso.setText(_translate("wdgHome", "<html><head/><body><p align=\"center\">hjhjhjhjhjhjhjhj</p></body></html>"))
        self.leCard4Compromiso.setText(_translate("wdgHome", "<html><head/><body><p align=\"center\">hjhjhjhjhjhjhjhj</p></body></html>"))
        self.leCard1Compromiso.setText(_translate("wdgHome", "<html><head/><body><p align=\"center\">afafsafafasfasfasf</p></body></html>"))
        self.leInfoCompromisso.setText(_translate("wdgHome", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Próximos Compromissos</span></p></body></html>"))
        self.leCard2Compromiso.setText(_translate("wdgHome", "<html><head/><body><p align=\"center\">fasfafaffghghhgjgh</p></body></html>"))
        self.leInfoFinanceiro.setText(_translate("wdgHome", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">Financeiro</span></p></body></html>"))
        self.leCard1Financeiro.setText(_translate("wdgHome", "<html><head/><body><p align=\"center\">afafsafafasfasfasf</p></body></html>"))
        self.leCard2Financeiro.setText(_translate("wdgHome", "<html><head/><body><p align=\"center\">afafsafafasfasfasf</p></body></html>"))
        self.leCard3Financeiro.setText(_translate("wdgHome", "<html><head/><body><p align=\"center\">afafsafafasfasfasf</p></body></html>"))
        self.leCard4Financeiro.setText(_translate("wdgHome", "<html><head/><body><p align=\"center\">afafsafafasfasfasf</p></body></html>"))
        self.leInfoFinanceiro_2.setText(_translate("wdgHome", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">Calendário</span></p></body></html>"))
        self.label.setText(_translate("wdgHome", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Compromissos </span></p><p align=\"center\"><span style=\" font-size:12pt;\">do</span></p><p align=\"center\"><span style=\" font-size:12pt;\"> Dia </span></p><p align=\"center\"><span style=\" font-size:12pt;\">Ao </span></p><p align=\"center\"><span style=\" font-size:12pt;\">clicar </span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    wdgHome = QtWidgets.QWidget()
    ui = Ui_wdgHome()
    ui.setupUi(wdgHome)
    wdgHome.show()
    sys.exit(app.exec_())
