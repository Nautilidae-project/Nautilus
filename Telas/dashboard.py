# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dashboard.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mwDash(object):
    def setupUi(self, mwDash):
        mwDash.setObjectName("mwDash")
        mwDash.resize(1000, 826)
        mwDash.setMinimumSize(QtCore.QSize(1000, 500))
        mwDash.setStyleSheet("QWidget {\n"
"    background-color: #0E90AD;\n"
"}\n"
"\n"
"#frPrincipalDash{\n"
"background-color: #0E90AD;\n"
"\n"
"border-radius: 60%;\n"
"}\n"
"\n"
"QFrame  {\n"
"    background: transparent;\n"
"\n"
"    border-radius: 25%;\n"
"}\n"
"QPushButton {\n"
"    background-color: #DFD880;\n"
"    border-top-right-radius: 10px;\n"
"    border-bottom-right-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #80CCE1;\n"
"}\n"
"\n"
"#frAgenda, #frHome  {\n"
"    background-color: rgb(223, 216, 128);\n"
"    border-radius: 0px;\n"
"    border-top-right-radius: 10px;\n"
"    border-bottom-right-radius: 10px;\n"
"}\n"
"\n"
"#frAgenda:hover, #frHome:hover  {\n"
"    background-color: #80CCE1;\n"
"    border-radius: 0px;\n"
"    border-top-right-radius: 10px;\n"
"    border-bottom-right-radius: 10px;\n"
"}\n"
"\n"
"#frIconAgenda {\n"
"    background-image: url(:/iconAgenda/calendar.png);\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"}\n"
"\n"
"#frIconHome {\n"
"    background-image: url(:/iconHome/home.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"}\n"
"\n"
"")
        self.wdgDash = QtWidgets.QWidget(mwDash)
        self.wdgDash.setObjectName("wdgDash")
        self.gridLayout = QtWidgets.QGridLayout(self.wdgDash)
        self.gridLayout.setContentsMargins(0, -1, -1, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.frPrincipalDash = QtWidgets.QFrame(self.wdgDash)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frPrincipalDash.sizePolicy().hasHeightForWidth())
        self.frPrincipalDash.setSizePolicy(sizePolicy)
        self.frPrincipalDash.setMinimumSize(QtCore.QSize(900, 400))
        self.frPrincipalDash.setStyleSheet("")
        self.frPrincipalDash.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frPrincipalDash.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frPrincipalDash.setObjectName("frPrincipalDash")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frPrincipalDash)
        self.horizontalLayout.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frMenu = QtWidgets.QFrame(self.frPrincipalDash)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frMenu.sizePolicy().hasHeightForWidth())
        self.frMenu.setSizePolicy(sizePolicy)
        self.frMenu.setMinimumSize(QtCore.QSize(80, 0))
        self.frMenu.setMaximumSize(QtCore.QSize(70, 16777215))
        self.frMenu.setStyleSheet("")
        self.frMenu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frMenu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frMenu.setObjectName("frMenu")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frMenu)
        self.verticalLayout.setContentsMargins(0, 9, 9, 9)
        self.verticalLayout.setSpacing(9)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frAvatar = QtWidgets.QFrame(self.frMenu)
        self.frAvatar.setMinimumSize(QtCore.QSize(0, 100))
        self.frAvatar.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frAvatar.setStyleSheet("background-color: rgba(238, 238, 236,0);\n"
"")
        self.frAvatar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frAvatar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frAvatar.setLineWidth(0)
        self.frAvatar.setObjectName("frAvatar")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frAvatar)
        self.horizontalLayout_2.setContentsMargins(9, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pbDash = QtWidgets.QPushButton(self.frAvatar)
        self.pbDash.setMinimumSize(QtCore.QSize(60, 60))
        self.pbDash.setStyleSheet("#pbDash {    \n"
"    background-image: url(:/logoDash/nautilusDash.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"}")
        self.pbDash.setText("")
        self.pbDash.setObjectName("pbDash")
        self.horizontalLayout_2.addWidget(self.pbDash)
        self.verticalLayout.addWidget(self.frAvatar)
        self.frHome = QtWidgets.QFrame(self.frMenu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frHome.sizePolicy().hasHeightForWidth())
        self.frHome.setSizePolicy(sizePolicy)
        self.frHome.setMinimumSize(QtCore.QSize(0, 60))
        self.frHome.setStyleSheet("")
        self.frHome.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frHome.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frHome.setObjectName("frHome")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frHome)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frIconHome = QtWidgets.QFrame(self.frHome)
        self.frIconHome.setMinimumSize(QtCore.QSize(40, 50))
        self.frIconHome.setMaximumSize(QtCore.QSize(40, 50))
        self.frIconHome.setStyleSheet("")
        self.frIconHome.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frIconHome.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frIconHome.setObjectName("frIconHome")
        self.horizontalLayout_3.addWidget(self.frIconHome)
        self.pbHome = QtWidgets.QPushButton(self.frHome)
        self.pbHome.setMinimumSize(QtCore.QSize(50, 50))
        self.pbHome.setStyleSheet("")
        self.pbHome.setObjectName("pbHome")
        self.horizontalLayout_3.addWidget(self.pbHome)
        self.verticalLayout.addWidget(self.frHome, 0, QtCore.Qt.AlignHCenter)
        self.frAgenda = QtWidgets.QFrame(self.frMenu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frAgenda.sizePolicy().hasHeightForWidth())
        self.frAgenda.setSizePolicy(sizePolicy)
        self.frAgenda.setMinimumSize(QtCore.QSize(0, 60))
        self.frAgenda.setStyleSheet("")
        self.frAgenda.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frAgenda.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frAgenda.setObjectName("frAgenda")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frAgenda)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frIconAgenda = QtWidgets.QFrame(self.frAgenda)
        self.frIconAgenda.setMinimumSize(QtCore.QSize(40, 50))
        self.frIconAgenda.setMaximumSize(QtCore.QSize(40, 50))
        self.frIconAgenda.setStyleSheet("")
        self.frIconAgenda.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frIconAgenda.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frIconAgenda.setObjectName("frIconAgenda")
        self.horizontalLayout_4.addWidget(self.frIconAgenda)
        self.pbAgenda = QtWidgets.QPushButton(self.frAgenda)
        self.pbAgenda.setMinimumSize(QtCore.QSize(0, 50))
        self.pbAgenda.setStyleSheet("#pbAgenda {\n"
"    background-color: rgba(238, 238, 236,0);\n"
"}")
        self.pbAgenda.setObjectName("pbAgenda")
        self.horizontalLayout_4.addWidget(self.pbAgenda)
        self.verticalLayout.addWidget(self.frAgenda, 0, QtCore.Qt.AlignHCenter)
        self.pbCliente = QtWidgets.QPushButton(self.frMenu)
        self.pbCliente.setMinimumSize(QtCore.QSize(0, 60))
        self.pbCliente.setObjectName("pbCliente")
        self.verticalLayout.addWidget(self.pbCliente)
        self.pbFinanceiro = QtWidgets.QPushButton(self.frMenu)
        self.pbFinanceiro.setMinimumSize(QtCore.QSize(0, 60))
        self.pbFinanceiro.setObjectName("pbFinanceiro")
        self.verticalLayout.addWidget(self.pbFinanceiro)
        self.pbConfig = QtWidgets.QPushButton(self.frMenu)
        self.pbConfig.setMinimumSize(QtCore.QSize(0, 60))
        self.pbConfig.setObjectName("pbConfig")
        self.verticalLayout.addWidget(self.pbConfig)
        spacerItem = QtWidgets.QSpacerItem(20, 200, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.pbSairDash = QtWidgets.QPushButton(self.frMenu)
        self.pbSairDash.setMinimumSize(QtCore.QSize(0, 60))
        self.pbSairDash.setObjectName("pbSairDash")
        self.verticalLayout.addWidget(self.pbSairDash)
        self.horizontalLayout.addWidget(self.frMenu, 0, QtCore.Qt.AlignTop)
        self.frStakeds = QtWidgets.QFrame(self.frPrincipalDash)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frStakeds.sizePolicy().hasHeightForWidth())
        self.frStakeds.setSizePolicy(sizePolicy)
        self.frStakeds.setMinimumSize(QtCore.QSize(0, 0))
        self.frStakeds.setStyleSheet("background-color: #fff;")
        self.frStakeds.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frStakeds.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frStakeds.setObjectName("frStakeds")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frStakeds)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.stkDash = QtWidgets.QStackedWidget(self.frStakeds)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stkDash.sizePolicy().hasHeightForWidth())
        self.stkDash.setSizePolicy(sizePolicy)
        self.stkDash.setStyleSheet("background-color: #fafafa;")
        self.stkDash.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.stkDash.setFrameShadow(QtWidgets.QFrame.Plain)
        self.stkDash.setObjectName("stkDash")
        self.gridLayout_2.addWidget(self.stkDash, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.frStakeds)
        self.gridLayout.addWidget(self.frPrincipalDash, 0, 0, 1, 1)
        mwDash.setCentralWidget(self.wdgDash)

        self.retranslateUi(mwDash)
        self.stkDash.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(mwDash)

    def retranslateUi(self, mwDash):
        _translate = QtCore.QCoreApplication.translate
        mwDash.setWindowTitle(_translate("mwDash", "MainWindow"))
        self.pbHome.setText(_translate("mwDash", "Home"))
        self.pbAgenda.setText(_translate("mwDash", "Agenda"))
        self.pbCliente.setText(_translate("mwDash", "Cliente"))
        self.pbFinanceiro.setText(_translate("mwDash", "Financeiro"))
        self.pbConfig.setText(_translate("mwDash", "Config"))
        self.pbSairDash.setText(_translate("mwDash", "Sair"))
import Telas.Imagens.img_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mwDash = QtWidgets.QMainWindow()
    ui = Ui_mwDash()
    ui.setupUi(mwDash)
    mwDash.show()
    sys.exit(app.exec_())
