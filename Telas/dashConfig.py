# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dashConfig.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_wdgConfig(object):
    def setupUi(self, wdgConfig):
        wdgConfig.setObjectName("wdgConfig")
        wdgConfig.resize(1092, 787)
        wdgConfig.setStyleSheet("/*-----------------------Labels------------------------------*/\n"
"\n"
"#lbTitulo {\n"
"    border: 0px;\n"
"    background-color: transparent;\n"
"    font-family: Ubuntu;\n"
"    font-size: 14pt;\n"
"    font-weight: bold;\n"
"    color: rgb(46, 52, 54);\n"
"}\n"
"\n"
"#lbDescricao {\n"
"    border: 0px;\n"
"    background-color: transparent;\n"
"    font-family: Ubuntu;\n"
"    font-size: 12pt;\n"
"    font-style: italic;\n"
"    color: rgb(85, 87, 83)\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(wdgConfig)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frCabecalho = QtWidgets.QFrame(wdgConfig)
        self.frCabecalho.setMinimumSize(QtCore.QSize(0, 60))
        self.frCabecalho.setMaximumSize(QtCore.QSize(16777215, 75))
        self.frCabecalho.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frCabecalho.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frCabecalho.setObjectName("frCabecalho")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frCabecalho)
        self.horizontalLayout.setContentsMargins(4, 0, 4, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frTextoCabecalho = QtWidgets.QFrame(self.frCabecalho)
        self.frTextoCabecalho.setMinimumSize(QtCore.QSize(250, 0))
        self.frTextoCabecalho.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frTextoCabecalho.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frTextoCabecalho.setObjectName("frTextoCabecalho")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frTextoCabecalho)
        self.verticalLayout_2.setContentsMargins(2, 0, 2, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lbTitulo = QtWidgets.QLabel(self.frTextoCabecalho)
        self.lbTitulo.setObjectName("lbTitulo")
        self.verticalLayout_2.addWidget(self.lbTitulo)
        self.lbDescricao = QtWidgets.QLabel(self.frTextoCabecalho)
        self.lbDescricao.setObjectName("lbDescricao")
        self.verticalLayout_2.addWidget(self.lbDescricao)
        self.horizontalLayout.addWidget(self.frTextoCabecalho)
        spacerItem = QtWidgets.QSpacerItem(524, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addWidget(self.frCabecalho)
        self.tabConfiguracoes = QtWidgets.QTabWidget(wdgConfig)
        self.tabConfiguracoes.setObjectName("tabConfiguracoes")
        self.tabUsuario = QtWidgets.QWidget()
        self.tabUsuario.setStyleSheet("/****************** Labels ************************/\n"
"\n"
"#frLogo {\n"
"    border: none;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/****************** Frames ************************/\n"
"\n"
"#lbLogo {\n"
"    border: none;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/****************** Buttons ************************/\n"
"\n"
"#pbInsereImg {\n"
"    background-color: rgb(14, 144, 173);\n"
"    color: white;\n"
"    font-family: Ubuntu;\n"
"    font-size: 12pt;\n"
"}\n"
"\n"
"#pbInsereImg::hover {\n"
"    background-color: white;\n"
"    color: rgb(14, 144, 173);\n"
"    font-family: Ubuntu;\n"
"    font-size: 12pt;\n"
"}\n"
"\n"
"#pbExcluiImg {\n"
"    background-color: rgb(255, 204, 204);\n"
"    color: rgb(80, 80, 80);\n"
"    font-family: Ubuntu;\n"
"    font-size: 12pt;\n"
"}\n"
"\n"
"#pbExcluiImg::hover {\n"
"    background-color: white;\n"
"    color: rgb(255, 204, 204);\n"
"    font-family: Ubuntu;\n"
"    font-size: 12pt;\n"
"}\n"
"")
        self.tabUsuario.setObjectName("tabUsuario")
        self.frInfoLogo = QtWidgets.QFrame(self.tabUsuario)
        self.frInfoLogo.setGeometry(QtCore.QRect(20, 20, 282, 96))
        self.frInfoLogo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frInfoLogo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frInfoLogo.setObjectName("frInfoLogo")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frInfoLogo)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frLogo = QtWidgets.QFrame(self.frInfoLogo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frLogo.sizePolicy().hasHeightForWidth())
        self.frLogo.setSizePolicy(sizePolicy)
        self.frLogo.setMinimumSize(QtCore.QSize(64, 64))
        self.frLogo.setMaximumSize(QtCore.QSize(80, 80))
        self.frLogo.setBaseSize(QtCore.QSize(64, 64))
        self.frLogo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frLogo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frLogo.setObjectName("frLogo")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frLogo)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lbLogo = QtWidgets.QLabel(self.frLogo)
        self.lbLogo.setBaseSize(QtCore.QSize(64, 64))
        self.lbLogo.setText("")
        self.lbLogo.setObjectName("lbLogo")
        self.horizontalLayout_2.addWidget(self.lbLogo)
        self.horizontalLayout_3.addWidget(self.frLogo)
        self.frBotoes = QtWidgets.QFrame(self.frInfoLogo)
        self.frBotoes.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frBotoes.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frBotoes.setObjectName("frBotoes")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frBotoes)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pbInsereImg = QtWidgets.QPushButton(self.frBotoes)
        self.pbInsereImg.setObjectName("pbInsereImg")
        self.verticalLayout_3.addWidget(self.pbInsereImg)
        self.pbExcluiImg = QtWidgets.QPushButton(self.frBotoes)
        self.pbExcluiImg.setObjectName("pbExcluiImg")
        self.verticalLayout_3.addWidget(self.pbExcluiImg)
        self.horizontalLayout_3.addWidget(self.frBotoes)
        self.tabConfiguracoes.addTab(self.tabUsuario, "")
        self.tabClientes = QtWidgets.QWidget()
        self.tabClientes.setObjectName("tabClientes")
        self.tabConfiguracoes.addTab(self.tabClientes, "")
        self.tabAgenda = QtWidgets.QWidget()
        self.tabAgenda.setObjectName("tabAgenda")
        self.tabConfiguracoes.addTab(self.tabAgenda, "")
        self.tabFinanceiro = QtWidgets.QWidget()
        self.tabFinanceiro.setObjectName("tabFinanceiro")
        self.tabConfiguracoes.addTab(self.tabFinanceiro, "")
        self.verticalLayout.addWidget(self.tabConfiguracoes)

        self.retranslateUi(wdgConfig)
        self.tabConfiguracoes.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(wdgConfig)

    def retranslateUi(self, wdgConfig):
        _translate = QtCore.QCoreApplication.translate
        wdgConfig.setWindowTitle(_translate("wdgConfig", "Form"))
        self.lbTitulo.setText(_translate("wdgConfig", "Configurações do usuário"))
        self.lbDescricao.setText(_translate("wdgConfig", "Nesta página você pode alterar as configurações referentes ao seu cadastro."))
        self.pbInsereImg.setText(_translate("wdgConfig", "Inserir logo"))
        self.pbExcluiImg.setText(_translate("wdgConfig", "Excluir logo"))
        self.tabConfiguracoes.setTabText(self.tabConfiguracoes.indexOf(self.tabUsuario), _translate("wdgConfig", "Usuário"))
        self.tabConfiguracoes.setTabText(self.tabConfiguracoes.indexOf(self.tabClientes), _translate("wdgConfig", "Clientes"))
        self.tabConfiguracoes.setTabText(self.tabConfiguracoes.indexOf(self.tabAgenda), _translate("wdgConfig", "Agenda"))
        self.tabConfiguracoes.setTabText(self.tabConfiguracoes.indexOf(self.tabFinanceiro), _translate("wdgConfig", "Financeiro"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    wdgConfig = QtWidgets.QWidget()
    ui = Ui_wdgConfig()
    ui.setupUi(wdgConfig)
    wdgConfig.show()
    sys.exit(app.exec_())
