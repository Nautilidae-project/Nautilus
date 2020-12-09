# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dashCliente.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_wdgCliente(object):
    def setupUi(self, wdgCliente):
        wdgCliente.setObjectName("wdgCliente")
        wdgCliente.resize(1046, 537)
        wdgCliente.setStyleSheet("#wdgCliente {\n"
"    background-color: #80CCE1;\n"
"}\n"
"\n"
"/*------------------- Frame ---------------------*/\n"
"QFrame {\n"
"    background-color: #fafafa;\n"
"    border: none;\n"
"}\n"
"\n"
"/*------------------- Label ---------------------*/\n"
"QLabel {\n"
"    font: 150 14pt \"Fira Sans\" ;\n"
"\n"
"    border-radius: 10px;\n"
"    border: 2px solid  #fff;\n"
"    color: rgb(100, 100, 100);\n"
"    background-color: #DFD880;\n"
"}\n"
"\n"
"#lbTitulo{\n"
"        background-color: none;\n"
"        font: 300 22pt \"Fira Sans\" ;\n"
"}\n"
"\n"
"#lbCorpo{\n"
"        background-color: none;\n"
"        font: 200 18pt \"Fira Sans\" ;\n"
"}\n"
"\n"
"/*------------------- Line Edit ---------------------*/\n"
"QLineEdit {\n"
"    border: none;\n"
"    background-color: #fafafa;\n"
"    border-bottom: 2px solid #444444;\n"
"    \n"
"    font: 80 14pt \"Fira Sans\" ;\n"
"\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    border: 2px solid 444444;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"/*------------------- Push Buttom ---------------------*/\n"
"QPushButton{\n"
"    background-color: #DFD880;\n"
"    border: 0px solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #8cdf80;\n"
"}\n"
"")
        self.gridLayout = QtWidgets.QGridLayout(wdgCliente)
        self.gridLayout.setContentsMargins(0, 9, 0, 30)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.tabsCliente = QtWidgets.QTabWidget(wdgCliente)
        self.tabsCliente.setStyleSheet("QTabWidget::pane {\n"
"    border-top: 3px solid;\n"
"}\n"
"\n"
"QTabWidget QStackedWidget > QWidget   \n"
"{    \n"
"    background-color: #fafafa;\n"
"}\n"
"\n"
"\n"
"/*-------------------------------------------------------------*/\n"
"\n"
"\n"
"QTabWidget::tab-bar {\n"
"    alignment: center;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    font: 80 14pt \"Fira Sans\" ;\n"
"    height: 25px;\n"
"    width: 125px;\n"
" \n"
"    border: 1px double transparent;\n"
"    border-top-left-radius: 14px;\n"
"    border-top-right-radius: 14px;\n"
"\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"    background-color: #DFD880;\n"
"    \n"
"}\n"
"\n"
"")
        self.tabsCliente.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabsCliente.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabsCliente.setObjectName("tabsCliente")
        self.tbInfosCliente = QtWidgets.QWidget()
        self.tbInfosCliente.setObjectName("tbInfosCliente")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tbInfosCliente)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frListButtons = QtWidgets.QFrame(self.tbInfosCliente)
        self.frListButtons.setMinimumSize(QtCore.QSize(700, 60))
        self.frListButtons.setMaximumSize(QtCore.QSize(700, 60))
        self.frListButtons.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frListButtons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frListButtons.setObjectName("frListButtons")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frListButtons)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.frNomeTabela = QtWidgets.QFrame(self.frListButtons)
        self.frNomeTabela.setMinimumSize(QtCore.QSize(200, 0))
        self.frNomeTabela.setMaximumSize(QtCore.QSize(200, 16777215))
        self.frNomeTabela.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frNomeTabela.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frNomeTabela.setObjectName("frNomeTabela")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frNomeTabela)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lbNomeTabela = QtWidgets.QLabel(self.frNomeTabela)
        self.lbNomeTabela.setMinimumSize(QtCore.QSize(180, 30))
        self.lbNomeTabela.setMaximumSize(QtCore.QSize(180, 16777215))
        self.lbNomeTabela.setAlignment(QtCore.Qt.AlignCenter)
        self.lbNomeTabela.setObjectName("lbNomeTabela")
        self.horizontalLayout_4.addWidget(self.lbNomeTabela)
        self.gridLayout_4.addWidget(self.frNomeTabela, 0, 0, 1, 1)
        self.frSearch = QtWidgets.QFrame(self.frListButtons)
        self.frSearch.setMinimumSize(QtCore.QSize(160, 0))
        self.frSearch.setMaximumSize(QtCore.QSize(160, 60))
        self.frSearch.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frSearch.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frSearch.setObjectName("frSearch")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.frSearch)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.leSearchCliente = QtWidgets.QLineEdit(self.frSearch)
        self.leSearchCliente.setMinimumSize(QtCore.QSize(150, 30))
        self.leSearchCliente.setMaximumSize(QtCore.QSize(150, 16777215))
        self.leSearchCliente.setText("")
        self.leSearchCliente.setObjectName("leSearchCliente")
        self.horizontalLayout_17.addWidget(self.leSearchCliente)
        self.gridLayout_4.addWidget(self.frSearch, 0, 1, 1, 1)
        self.frCmbFilter = QtWidgets.QFrame(self.frListButtons)
        self.frCmbFilter.setMinimumSize(QtCore.QSize(150, 0))
        self.frCmbFilter.setMaximumSize(QtCore.QSize(150, 60))
        self.frCmbFilter.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frCmbFilter.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frCmbFilter.setObjectName("frCmbFilter")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.frCmbFilter)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.comboBox = QtWidgets.QComboBox(self.frCmbFilter)
        self.comboBox.setMaximumSize(QtCore.QSize(200, 16777215))
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_18.addWidget(self.comboBox)
        self.gridLayout_4.addWidget(self.frCmbFilter, 0, 2, 1, 1)
        self.frRightButtons = QtWidgets.QFrame(self.frListButtons)
        self.frRightButtons.setMinimumSize(QtCore.QSize(100, 0))
        self.frRightButtons.setMaximumSize(QtCore.QSize(160, 60))
        self.frRightButtons.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frRightButtons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frRightButtons.setObjectName("frRightButtons")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.frRightButtons)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.pbFuncionalidade1 = QtWidgets.QPushButton(self.frRightButtons)
        self.pbFuncionalidade1.setMinimumSize(QtCore.QSize(50, 30))
        self.pbFuncionalidade1.setMaximumSize(QtCore.QSize(70, 16777215))
        self.pbFuncionalidade1.setObjectName("pbFuncionalidade1")
        self.horizontalLayout_19.addWidget(self.pbFuncionalidade1)
        self.pbFuncionalidade2 = QtWidgets.QPushButton(self.frRightButtons)
        self.pbFuncionalidade2.setMinimumSize(QtCore.QSize(50, 30))
        self.pbFuncionalidade2.setMaximumSize(QtCore.QSize(70, 16777215))
        self.pbFuncionalidade2.setObjectName("pbFuncionalidade2")
        self.horizontalLayout_19.addWidget(self.pbFuncionalidade2)
        self.gridLayout_4.addWidget(self.frRightButtons, 0, 3, 1, 1)
        self.gridLayout_3.addWidget(self.frListButtons, 1, 0, 1, 1)
        self.frClientsList = QtWidgets.QFrame(self.tbInfosCliente)
        self.frClientsList.setMaximumSize(QtCore.QSize(700, 16777215))
        self.frClientsList.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frClientsList.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frClientsList.setObjectName("frClientsList")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frClientsList)
        self.gridLayout_5.setContentsMargins(10, 10, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.tblClientes = QtWidgets.QTableWidget(self.frClientsList)
        self.tblClientes.setMinimumSize(QtCore.QSize(600, 0))
        self.tblClientes.setMaximumSize(QtCore.QSize(600, 16777215))
        self.tblClientes.setStyleSheet("QHeaderView::section {\n"
"   \n"
"    background-color: #fafafa;\n"
"        \n"
"    color: white;\n"
"    padding-left: 4px;\n"
"\n"
"    border: none;\n"
"    border-bottom: 2px solid;\n"
"    color: #444;\n"
"}\n"
"\n"
"QHeaderView::section:checked\n"
"{\n"
"    background-color: red;\n"
"    border-radius: 10%;\n"
"}\n"
"\n"
"QTableView {\n"
"    selection-background-color: rgb(251, 184, 108);\n"
"    \n"
"    alternate-background-color: rgb(108, 251, 208);\n"
"}\n"
"")
        self.tblClientes.setLocale(QtCore.QLocale(QtCore.QLocale.Portuguese, QtCore.QLocale.Brazil))
        self.tblClientes.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tblClientes.setLineWidth(0)
        self.tblClientes.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.tblClientes.setAlternatingRowColors(True)
        self.tblClientes.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tblClientes.setShowGrid(False)
        self.tblClientes.setWordWrap(True)
        self.tblClientes.setCornerButtonEnabled(True)
        self.tblClientes.setRowCount(5)
        self.tblClientes.setColumnCount(4)
        self.tblClientes.setObjectName("tblClientes")
        item = QtWidgets.QTableWidgetItem()
        self.tblClientes.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblClientes.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblClientes.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblClientes.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblClientes.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Fira Sans")
        font.setPointSize(14)
        item.setFont(font)
        self.tblClientes.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Fira Sans")
        font.setPointSize(14)
        item.setFont(font)
        self.tblClientes.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Fira Sans")
        font.setPointSize(14)
        item.setFont(font)
        self.tblClientes.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Fira Sans")
        font.setPointSize(14)
        item.setFont(font)
        self.tblClientes.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblClientes.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblClientes.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblClientes.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblClientes.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblClientes.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblClientes.setItem(3, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblClientes.setItem(3, 3, item)
        self.tblClientes.horizontalHeader().setVisible(True)
        self.tblClientes.horizontalHeader().setDefaultSectionSize(150)
        self.tblClientes.horizontalHeader().setMinimumSectionSize(140)
        self.tblClientes.verticalHeader().setVisible(False)
        self.gridLayout_5.addWidget(self.tblClientes, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.frClientsList, 2, 0, 1, 1)
        self.frTopTabMenu = QtWidgets.QFrame(self.tbInfosCliente)
        self.frTopTabMenu.setMinimumSize(QtCore.QSize(0, 90))
        self.frTopTabMenu.setMaximumSize(QtCore.QSize(16777215, 110))
        self.frTopTabMenu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frTopTabMenu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frTopTabMenu.setObjectName("frTopTabMenu")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frTopTabMenu)
        self.horizontalLayout_2.setContentsMargins(12, 0, 12, 0)
        self.horizontalLayout_2.setSpacing(24)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frLeftInfo = QtWidgets.QFrame(self.frTopTabMenu)
        self.frLeftInfo.setStyleSheet("background-color: rgb(239, 41, 41);")
        self.frLeftInfo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frLeftInfo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frLeftInfo.setObjectName("frLeftInfo")
        self.horizontalLayout_2.addWidget(self.frLeftInfo)
        self.frCenterInfo = QtWidgets.QFrame(self.frTopTabMenu)
        self.frCenterInfo.setStyleSheet("background-color: rgb(138, 226, 52);")
        self.frCenterInfo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frCenterInfo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frCenterInfo.setObjectName("frCenterInfo")
        self.horizontalLayout_2.addWidget(self.frCenterInfo)
        self.frRightInfo = QtWidgets.QFrame(self.frTopTabMenu)
        self.frRightInfo.setStyleSheet("background-color: rgb(252, 233, 79);")
        self.frRightInfo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frRightInfo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frRightInfo.setObjectName("frRightInfo")
        self.horizontalLayout_2.addWidget(self.frRightInfo)
        self.gridLayout_3.addWidget(self.frTopTabMenu, 0, 0, 1, 2)
        self.frame_2 = QtWidgets.QFrame(self.tbInfosCliente)
        self.frame_2.setStyleSheet("background-color: rgb(108, 251, 208);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_3.addWidget(self.frame_2, 1, 1, 2, 1)
        self.tabsCliente.addTab(self.tbInfosCliente, "")
        self.tbCadastraCliente = QtWidgets.QWidget()
        self.tbCadastraCliente.setStyleSheet("")
        self.tbCadastraCliente.setObjectName("tbCadastraCliente")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tbCadastraCliente)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frCabecalho = QtWidgets.QFrame(self.tbCadastraCliente)
        self.frCabecalho.setMinimumSize(QtCore.QSize(600, 100))
        self.frCabecalho.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frCabecalho.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frCabecalho.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frCabecalho.setObjectName("frCabecalho")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frCabecalho)
        self.verticalLayout_3.setContentsMargins(9, 9, -1, -1)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lbTitulo = QtWidgets.QLabel(self.frCabecalho)
        font = QtGui.QFont()
        font.setFamily("Fira Sans")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(37)
        self.lbTitulo.setFont(font)
        self.lbTitulo.setStyleSheet("color: rgb(46, 52, 54)")
        self.lbTitulo.setObjectName("lbTitulo")
        self.verticalLayout_3.addWidget(self.lbTitulo)
        self.lbCorpo = QtWidgets.QLabel(self.frCabecalho)
        self.lbCorpo.setStyleSheet("color: rgb(46, 52, 54)")
        self.lbCorpo.setObjectName("lbCorpo")
        self.verticalLayout_3.addWidget(self.lbCorpo)
        self.gridLayout_2.addWidget(self.frCabecalho, 0, 0, 1, 1)
        self.frNomeSobrenome = QtWidgets.QFrame(self.tbCadastraCliente)
        self.frNomeSobrenome.setMinimumSize(QtCore.QSize(600, 60))
        self.frNomeSobrenome.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frNomeSobrenome.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frNomeSobrenome.setObjectName("frNomeSobrenome")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frNomeSobrenome)
        self.horizontalLayout_5.setContentsMargins(0, 0, 9, 0)
        self.horizontalLayout_5.setSpacing(50)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frNome = QtWidgets.QFrame(self.frNomeSobrenome)
        self.frNome.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frNome.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frNome.setObjectName("frNome")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frNome)
        self.horizontalLayout_9.setContentsMargins(9, -1, -1, -1)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.lbNome = QtWidgets.QLabel(self.frNome)
        self.lbNome.setMinimumSize(QtCore.QSize(130, 0))
        self.lbNome.setMaximumSize(QtCore.QSize(150, 30))
        self.lbNome.setStyleSheet("color: rgb(46, 52, 54)")
        self.lbNome.setTextFormat(QtCore.Qt.RichText)
        self.lbNome.setAlignment(QtCore.Qt.AlignCenter)
        self.lbNome.setObjectName("lbNome")
        self.horizontalLayout_9.addWidget(self.lbNome)
        self.leNome = QtWidgets.QLineEdit(self.frNome)
        self.leNome.setMinimumSize(QtCore.QSize(0, 30))
        self.leNome.setMaximumSize(QtCore.QSize(600, 16777215))
        self.leNome.setStyleSheet("")
        self.leNome.setInputMask("")
        self.leNome.setText("")
        self.leNome.setObjectName("leNome")
        self.horizontalLayout_9.addWidget(self.leNome)
        self.leNome.raise_()
        self.lbNome.raise_()
        self.horizontalLayout_5.addWidget(self.frNome)
        self.frSobrenome = QtWidgets.QFrame(self.frNomeSobrenome)
        self.frSobrenome.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frSobrenome.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frSobrenome.setObjectName("frSobrenome")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frSobrenome)
        self.horizontalLayout_10.setContentsMargins(9, -1, -1, -1)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.lbSobrenome = QtWidgets.QLabel(self.frSobrenome)
        self.lbSobrenome.setMinimumSize(QtCore.QSize(130, 30))
        self.lbSobrenome.setMaximumSize(QtCore.QSize(150, 30))
        self.lbSobrenome.setStyleSheet("color: rgb(46, 52, 54)")
        self.lbSobrenome.setTextFormat(QtCore.Qt.RichText)
        self.lbSobrenome.setAlignment(QtCore.Qt.AlignCenter)
        self.lbSobrenome.setObjectName("lbSobrenome")
        self.horizontalLayout_10.addWidget(self.lbSobrenome)
        self.leSobrenome = QtWidgets.QLineEdit(self.frSobrenome)
        self.leSobrenome.setMinimumSize(QtCore.QSize(0, 30))
        self.leSobrenome.setMaximumSize(QtCore.QSize(600, 16777215))
        self.leSobrenome.setStyleSheet("")
        self.leSobrenome.setObjectName("leSobrenome")
        self.horizontalLayout_10.addWidget(self.leSobrenome)
        self.leSobrenome.raise_()
        self.lbSobrenome.raise_()
        self.horizontalLayout_5.addWidget(self.frSobrenome)
        spacerItem = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.gridLayout_2.addWidget(self.frNomeSobrenome, 1, 0, 1, 1)
        self.frame = QtWidgets.QFrame(self.tbCadastraCliente)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(9, -1, -1, 0)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pbCadastrar = QtWidgets.QPushButton(self.frame)
        self.pbCadastrar.setMinimumSize(QtCore.QSize(80, 50))
        self.pbCadastrar.setMaximumSize(QtCore.QSize(200, 50))
        self.pbCadastrar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pbCadastrar.setStyleSheet("")
        self.pbCadastrar.setObjectName("pbCadastrar")
        self.horizontalLayout.addWidget(self.pbCadastrar)
        self.gridLayout_2.addWidget(self.frame, 5, 0, 1, 1)
        self.frEmailTel = QtWidgets.QFrame(self.tbCadastraCliente)
        self.frEmailTel.setMinimumSize(QtCore.QSize(600, 60))
        self.frEmailTel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frEmailTel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frEmailTel.setObjectName("frEmailTel")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frEmailTel)
        self.horizontalLayout_6.setContentsMargins(0, 0, 9, 0)
        self.horizontalLayout_6.setSpacing(50)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.frTel = QtWidgets.QFrame(self.frEmailTel)
        self.frTel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frTel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frTel.setObjectName("frTel")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frTel)
        self.horizontalLayout_11.setContentsMargins(9, -1, -1, -1)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.lbTel = QtWidgets.QLabel(self.frTel)
        self.lbTel.setMinimumSize(QtCore.QSize(130, 0))
        self.lbTel.setMaximumSize(QtCore.QSize(150, 30))
        self.lbTel.setStyleSheet("color: rgb(46, 52, 54)")
        self.lbTel.setTextFormat(QtCore.Qt.RichText)
        self.lbTel.setAlignment(QtCore.Qt.AlignCenter)
        self.lbTel.setObjectName("lbTel")
        self.horizontalLayout_11.addWidget(self.lbTel)
        self.leTel = QtWidgets.QLineEdit(self.frTel)
        self.leTel.setMinimumSize(QtCore.QSize(0, 30))
        self.leTel.setMaximumSize(QtCore.QSize(600, 16777215))
        self.leTel.setStyleSheet("")
        self.leTel.setObjectName("leTel")
        self.horizontalLayout_11.addWidget(self.leTel)
        self.horizontalLayout_6.addWidget(self.frTel)
        self.frEmail = QtWidgets.QFrame(self.frEmailTel)
        self.frEmail.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frEmail.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frEmail.setObjectName("frEmail")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frEmail)
        self.horizontalLayout_12.setContentsMargins(9, -1, -1, -1)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.lbEmail = QtWidgets.QLabel(self.frEmail)
        self.lbEmail.setMinimumSize(QtCore.QSize(130, 0))
        self.lbEmail.setMaximumSize(QtCore.QSize(150, 30))
        self.lbEmail.setStyleSheet("color: rgb(46, 52, 54)")
        self.lbEmail.setTextFormat(QtCore.Qt.RichText)
        self.lbEmail.setAlignment(QtCore.Qt.AlignCenter)
        self.lbEmail.setObjectName("lbEmail")
        self.horizontalLayout_12.addWidget(self.lbEmail)
        self.leEmail = QtWidgets.QLineEdit(self.frEmail)
        self.leEmail.setMinimumSize(QtCore.QSize(0, 30))
        self.leEmail.setMaximumSize(QtCore.QSize(600, 16777215))
        self.leEmail.setStyleSheet("")
        self.leEmail.setObjectName("leEmail")
        self.horizontalLayout_12.addWidget(self.leEmail)
        self.horizontalLayout_6.addWidget(self.frEmail)
        spacerItem1 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.gridLayout_2.addWidget(self.frEmailTel, 2, 0, 1, 1)
        self.frCepEnd = QtWidgets.QFrame(self.tbCadastraCliente)
        self.frCepEnd.setMinimumSize(QtCore.QSize(600, 60))
        self.frCepEnd.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frCepEnd.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frCepEnd.setObjectName("frCepEnd")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frCepEnd)
        self.horizontalLayout_7.setContentsMargins(0, 0, 9, 0)
        self.horizontalLayout_7.setSpacing(50)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.frCep = QtWidgets.QFrame(self.frCepEnd)
        self.frCep.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frCep.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frCep.setObjectName("frCep")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.frCep)
        self.horizontalLayout_13.setContentsMargins(9, -1, -1, -1)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.lbCep = QtWidgets.QLabel(self.frCep)
        self.lbCep.setMinimumSize(QtCore.QSize(130, 0))
        self.lbCep.setMaximumSize(QtCore.QSize(150, 30))
        self.lbCep.setStyleSheet("color: rgb(46, 52, 54)")
        self.lbCep.setTextFormat(QtCore.Qt.RichText)
        self.lbCep.setAlignment(QtCore.Qt.AlignCenter)
        self.lbCep.setObjectName("lbCep")
        self.horizontalLayout_13.addWidget(self.lbCep)
        self.leCep = QtWidgets.QLineEdit(self.frCep)
        self.leCep.setMinimumSize(QtCore.QSize(0, 30))
        self.leCep.setMaximumSize(QtCore.QSize(600, 16777215))
        self.leCep.setStyleSheet("")
        self.leCep.setObjectName("leCep")
        self.horizontalLayout_13.addWidget(self.leCep)
        self.horizontalLayout_7.addWidget(self.frCep)
        self.frEndereco = QtWidgets.QFrame(self.frCepEnd)
        self.frEndereco.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frEndereco.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frEndereco.setObjectName("frEndereco")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.frEndereco)
        self.horizontalLayout_14.setContentsMargins(9, -1, -1, -1)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.lbEnd = QtWidgets.QLabel(self.frEndereco)
        self.lbEnd.setMinimumSize(QtCore.QSize(130, 0))
        self.lbEnd.setMaximumSize(QtCore.QSize(150, 30))
        self.lbEnd.setStyleSheet("color: rgb(46, 52, 54)")
        self.lbEnd.setTextFormat(QtCore.Qt.RichText)
        self.lbEnd.setAlignment(QtCore.Qt.AlignCenter)
        self.lbEnd.setObjectName("lbEnd")
        self.horizontalLayout_14.addWidget(self.lbEnd)
        self.leEnd = QtWidgets.QLineEdit(self.frEndereco)
        self.leEnd.setMinimumSize(QtCore.QSize(0, 30))
        self.leEnd.setMaximumSize(QtCore.QSize(600, 16777215))
        self.leEnd.setStyleSheet("")
        self.leEnd.setObjectName("leEnd")
        self.horizontalLayout_14.addWidget(self.leEnd)
        self.horizontalLayout_7.addWidget(self.frEndereco)
        spacerItem2 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem2)
        self.gridLayout_2.addWidget(self.frCepEnd, 3, 0, 1, 1)
        self.frBairroCompl = QtWidgets.QFrame(self.tbCadastraCliente)
        self.frBairroCompl.setMinimumSize(QtCore.QSize(600, 60))
        self.frBairroCompl.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frBairroCompl.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frBairroCompl.setObjectName("frBairroCompl")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frBairroCompl)
        self.horizontalLayout_8.setContentsMargins(0, 0, 9, 0)
        self.horizontalLayout_8.setSpacing(50)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.frBairro = QtWidgets.QFrame(self.frBairroCompl)
        self.frBairro.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frBairro.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frBairro.setObjectName("frBairro")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.frBairro)
        self.horizontalLayout_15.setContentsMargins(9, -1, -1, -1)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.lbBairro = QtWidgets.QLabel(self.frBairro)
        self.lbBairro.setMinimumSize(QtCore.QSize(130, 0))
        self.lbBairro.setMaximumSize(QtCore.QSize(150, 30))
        self.lbBairro.setStyleSheet("color: rgb(46, 52, 54)")
        self.lbBairro.setTextFormat(QtCore.Qt.RichText)
        self.lbBairro.setAlignment(QtCore.Qt.AlignCenter)
        self.lbBairro.setObjectName("lbBairro")
        self.horizontalLayout_15.addWidget(self.lbBairro)
        self.leBairro = QtWidgets.QLineEdit(self.frBairro)
        self.leBairro.setMinimumSize(QtCore.QSize(0, 30))
        self.leBairro.setMaximumSize(QtCore.QSize(600, 16777215))
        self.leBairro.setStyleSheet("")
        self.leBairro.setObjectName("leBairro")
        self.horizontalLayout_15.addWidget(self.leBairro)
        self.horizontalLayout_8.addWidget(self.frBairro)
        self.frComplemento = QtWidgets.QFrame(self.frBairroCompl)
        self.frComplemento.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frComplemento.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frComplemento.setObjectName("frComplemento")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.frComplemento)
        self.horizontalLayout_16.setContentsMargins(9, -1, -1, -1)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.lbCompl = QtWidgets.QLabel(self.frComplemento)
        self.lbCompl.setMinimumSize(QtCore.QSize(130, 0))
        self.lbCompl.setMaximumSize(QtCore.QSize(150, 30))
        self.lbCompl.setStyleSheet("color: rgb(46, 52, 54)")
        self.lbCompl.setTextFormat(QtCore.Qt.RichText)
        self.lbCompl.setAlignment(QtCore.Qt.AlignCenter)
        self.lbCompl.setObjectName("lbCompl")
        self.horizontalLayout_16.addWidget(self.lbCompl)
        self.leCompl = QtWidgets.QLineEdit(self.frComplemento)
        self.leCompl.setMinimumSize(QtCore.QSize(0, 30))
        self.leCompl.setMaximumSize(QtCore.QSize(600, 16777215))
        self.leCompl.setStyleSheet("")
        self.leCompl.setObjectName("leCompl")
        self.horizontalLayout_16.addWidget(self.leCompl)
        self.horizontalLayout_8.addWidget(self.frComplemento)
        spacerItem3 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem3)
        self.gridLayout_2.addWidget(self.frBairroCompl, 4, 0, 1, 1)
        self.tabsCliente.addTab(self.tbCadastraCliente, "")
        self.tbCronogramaCliente = QtWidgets.QWidget()
        self.tbCronogramaCliente.setObjectName("tbCronogramaCliente")
        self.tabsCliente.addTab(self.tbCronogramaCliente, "")
        self.tbBoletoCliente = QtWidgets.QWidget()
        self.tbBoletoCliente.setObjectName("tbBoletoCliente")
        self.tabsCliente.addTab(self.tbBoletoCliente, "")
        self.gridLayout.addWidget(self.tabsCliente, 0, 0, 1, 1)

        self.retranslateUi(wdgCliente)
        self.tabsCliente.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(wdgCliente)

    def retranslateUi(self, wdgCliente):
        _translate = QtCore.QCoreApplication.translate
        wdgCliente.setWindowTitle(_translate("wdgCliente", "Form"))
        self.lbNomeTabela.setText(_translate("wdgCliente", "Todos os clientes"))
        self.pbFuncionalidade1.setText(_translate("wdgCliente", "Função 1"))
        self.pbFuncionalidade2.setText(_translate("wdgCliente", "Função 2"))
        item = self.tblClientes.verticalHeaderItem(0)
        item.setText(_translate("wdgCliente", "New Row"))
        item = self.tblClientes.verticalHeaderItem(1)
        item.setText(_translate("wdgCliente", "New Row"))
        item = self.tblClientes.verticalHeaderItem(2)
        item.setText(_translate("wdgCliente", "New Row"))
        item = self.tblClientes.verticalHeaderItem(3)
        item.setText(_translate("wdgCliente", "New Row"))
        item = self.tblClientes.verticalHeaderItem(4)
        item.setText(_translate("wdgCliente", "New Row"))
        item = self.tblClientes.horizontalHeaderItem(0)
        item.setText(_translate("wdgCliente", "Nome"))
        item = self.tblClientes.horizontalHeaderItem(1)
        item.setText(_translate("wdgCliente", "CPF"))
        item = self.tblClientes.horizontalHeaderItem(2)
        item.setText(_translate("wdgCliente", "Meio de pagamento"))
        item = self.tblClientes.horizontalHeaderItem(3)
        item.setText(_translate("wdgCliente", "Ativo"))
        __sortingEnabled = self.tblClientes.isSortingEnabled()
        self.tblClientes.setSortingEnabled(False)
        item = self.tblClientes.item(1, 0)
        item.setText(_translate("wdgCliente", "s"))
        item = self.tblClientes.item(1, 2)
        item.setText(_translate("wdgCliente", "s"))
        item = self.tblClientes.item(2, 1)
        item.setText(_translate("wdgCliente", "s"))
        item = self.tblClientes.item(3, 0)
        item.setText(_translate("wdgCliente", "s"))
        item = self.tblClientes.item(3, 1)
        item.setText(_translate("wdgCliente", "s"))
        item = self.tblClientes.item(3, 2)
        item.setText(_translate("wdgCliente", "s"))
        item = self.tblClientes.item(3, 3)
        item.setText(_translate("wdgCliente", "ss"))
        self.tblClientes.setSortingEnabled(__sortingEnabled)
        self.tabsCliente.setTabText(self.tabsCliente.indexOf(self.tbInfosCliente), _translate("wdgCliente", "Informações"))
        self.lbTitulo.setText(_translate("wdgCliente", "Cadastro de clientes"))
        self.lbCorpo.setText(_translate("wdgCliente", "Cadastre seus clientes para poder gerenciar seus créditos, débitos e grupos."))
        self.lbNome.setText(_translate("wdgCliente", "Nome:    "))
        self.leNome.setPlaceholderText(_translate("wdgCliente", "Nome"))
        self.lbSobrenome.setText(_translate("wdgCliente", "Sobrenome:    "))
        self.leSobrenome.setPlaceholderText(_translate("wdgCliente", "Sobrenome"))
        self.pbCadastrar.setText(_translate("wdgCliente", "Cadastrar"))
        self.lbTel.setText(_translate("wdgCliente", "Telefone:    "))
        self.leTel.setPlaceholderText(_translate("wdgCliente", "Celular"))
        self.lbEmail.setText(_translate("wdgCliente", "<html><head/><body><p align=\"center\">E-mail:    </p></body></html>"))
        self.leEmail.setPlaceholderText(_translate("wdgCliente", "E - mail"))
        self.lbCep.setText(_translate("wdgCliente", "<html><head/><body><p align=\"center\">CEP:    </p></body></html>"))
        self.leCep.setPlaceholderText(_translate("wdgCliente", "CEP"))
        self.lbEnd.setText(_translate("wdgCliente", "<html><head/><body><p align=\"center\">Endereço:     </p></body></html>"))
        self.leEnd.setPlaceholderText(_translate("wdgCliente", "Endereco"))
        self.lbBairro.setText(_translate("wdgCliente", "Bairro:    "))
        self.leBairro.setPlaceholderText(_translate("wdgCliente", "Bairro"))
        self.lbCompl.setText(_translate("wdgCliente", "<html><head/><body><p align=\"center\">Complemento:    </p></body></html>"))
        self.leCompl.setPlaceholderText(_translate("wdgCliente", "Complemento"))
        self.tabsCliente.setTabText(self.tabsCliente.indexOf(self.tbCadastraCliente), _translate("wdgCliente", "Cadastro"))
        self.tabsCliente.setTabText(self.tabsCliente.indexOf(self.tbCronogramaCliente), _translate("wdgCliente", "Cronograma"))
        self.tabsCliente.setTabText(self.tabsCliente.indexOf(self.tbBoletoCliente), _translate("wdgCliente", "Boletos"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    wdgCliente = QtWidgets.QWidget()
    ui = Ui_wdgCliente()
    ui.setupUi(wdgCliente)
    wdgCliente.show()
    sys.exit(app.exec_())
