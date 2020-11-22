# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dashbord.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mwDash(object):
    def setupUi(self, mwDash):
        mwDash.setObjectName("mwDash")
        mwDash.resize(1000, 876)
        mwDash.setMinimumSize(QtCore.QSize(1000, 500))
        mwDash.setStyleSheet("QWidget {\n"
"    background-color: #80CCE1;\n"
"}\n"
"\n"
"")
        self.wdgDash = QtWidgets.QWidget(mwDash)
        self.wdgDash.setObjectName("wdgDash")
        self.gridLayout = QtWidgets.QGridLayout(self.wdgDash)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem1, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem3, 2, 1, 1, 1)
        self.frPrincipalDash = QtWidgets.QFrame(self.wdgDash)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frPrincipalDash.sizePolicy().hasHeightForWidth())
        self.frPrincipalDash.setSizePolicy(sizePolicy)
        self.frPrincipalDash.setMinimumSize(QtCore.QSize(900, 400))
        self.frPrincipalDash.setStyleSheet("\n"
"background-color: #0E90AD;\n"
"\n"
"border-radius: 60%;")
        self.frPrincipalDash.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frPrincipalDash.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frPrincipalDash.setObjectName("frPrincipalDash")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frPrincipalDash)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frMenu = QtWidgets.QFrame(self.frPrincipalDash)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frMenu.sizePolicy().hasHeightForWidth())
        self.frMenu.setSizePolicy(sizePolicy)
        self.frMenu.setMinimumSize(QtCore.QSize(80, 0))
        self.frMenu.setMaximumSize(QtCore.QSize(70, 16777215))
        self.frMenu.setStyleSheet("QFrame  {\n"
"    background: transparent;\n"
"\n"
"    border-radius: 25%;\n"
"}\n"
"QPushButton {\n"
"    background-color: #DFD880;\n"
"    border-top-right-radius: 18%;\n"
"    border-bottom-right-radius: 18%;\n"
"}\n"
"\n"
"")
        self.frMenu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frMenu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frMenu.setObjectName("frMenu")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frMenu)
        self.verticalLayout.setContentsMargins(9, 9, 9, 9)
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
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
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
        self.frHome.setMinimumSize(QtCore.QSize(0, 60))
        self.frHome.setStyleSheet("#frHome {\n"
"    background-color: rgb(223, 216, 128);\n"
"    border-radius: 0px;\n"
"    border-top-right-radius: 12px;\n"
"    border-bottom-right-radius: 12px;\n"
"}\n"
"\n"
"#frHome:hover {\n"
"    background-color: #80CCE1;\n"
"    border-radius: 0px;\n"
"    border-top-right-radius: 12px;\n"
"    border-bottom-right-radius: 12px;\n"
"}")
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
        self.frIconHome.setStyleSheet("#frIconHome {\n"
"    background-image: url(:/iconHome/home.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"}")
        self.frIconHome.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frIconHome.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frIconHome.setObjectName("frIconHome")
        self.horizontalLayout_3.addWidget(self.frIconHome)
        self.pbHome = QtWidgets.QPushButton(self.frHome)
        self.pbHome.setMinimumSize(QtCore.QSize(50, 50))
        self.pbHome.setStyleSheet("#pbHome {\n"
"    \n"
"    background-color: rgba(238, 238, 236,0);\n"
"}")
        self.pbHome.setObjectName("pbHome")
        self.horizontalLayout_3.addWidget(self.pbHome)
        self.verticalLayout.addWidget(self.frHome, 0, QtCore.Qt.AlignHCenter)
        self.frAgenda = QtWidgets.QFrame(self.frMenu)
        self.frAgenda.setMinimumSize(QtCore.QSize(0, 60))
        self.frAgenda.setStyleSheet("#frAgenda {\n"
"    background-color: rgb(223, 216, 128);\n"
"    border-radius: 0px;\n"
"    border-top-right-radius: 12px;\n"
"    border-bottom-right-radius: 12px;\n"
"}\n"
"\n"
"#frAgenda:hover {\n"
"    background-color: #80CCE1;\n"
"    border-radius: 0px;\n"
"    border-top-right-radius: 12px;\n"
"    border-bottom-right-radius: 12px;\n"
"}")
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
        self.frIconAgenda.setStyleSheet("#frIconAgenda {\n"
"    background-image: url(:/iconAgenda/calendar.png);\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"}")
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
        self.pbCliente.setMinimumSize(QtCore.QSize(0, 50))
        self.pbCliente.setObjectName("pbCliente")
        self.verticalLayout.addWidget(self.pbCliente)
        self.pbFuncionario = QtWidgets.QPushButton(self.frMenu)
        self.pbFuncionario.setMinimumSize(QtCore.QSize(0, 50))
        self.pbFuncionario.setObjectName("pbFuncionario")
        self.verticalLayout.addWidget(self.pbFuncionario)
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
        self.pgHome = QtWidgets.QWidget()
        self.pgHome.setStyleSheet("")
        self.pgHome.setObjectName("pgHome")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.pgHome)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.IGNORAR_2 = QtWidgets.QLabel(self.pgHome)
        font = QtGui.QFont()
        font.setPointSize(50)
        self.IGNORAR_2.setFont(font)
        self.IGNORAR_2.setAlignment(QtCore.Qt.AlignCenter)
        self.IGNORAR_2.setObjectName("IGNORAR_2")
        self.gridLayout_4.addWidget(self.IGNORAR_2, 0, 0, 1, 1)
        self.IGNORAR_1 = QtWidgets.QLabel(self.pgHome)
        font = QtGui.QFont()
        font.setPointSize(50)
        self.IGNORAR_1.setFont(font)
        self.IGNORAR_1.setAlignment(QtCore.Qt.AlignCenter)
        self.IGNORAR_1.setObjectName("IGNORAR_1")
        self.gridLayout_4.addWidget(self.IGNORAR_1, 1, 0, 1, 1)
        self.stkDash.addWidget(self.pgHome)
        self.pgCliente = QtWidgets.QWidget()
        self.pgCliente.setStyleSheet("")
        self.pgCliente.setObjectName("pgCliente")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.pgCliente)
        self.gridLayout_3.setContentsMargins(9, -1, -1, -1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tabsCliente = QtWidgets.QTabWidget(self.pgCliente)
        self.tabsCliente.setStyleSheet("QTabWidget::pane {border: 0px;}\n"
"\n"
"/*-------------------------------------------------------------*/\n"
"\n"
"\n"
"QTabWidget::tab-bar {\n"
"    alignment: center;\n"
"}\n"
"\n"
"\n"
"")
        self.tabsCliente.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabsCliente.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabsCliente.setObjectName("tabsCliente")
        self.tbCadastraCliente = QtWidgets.QWidget()
        self.tbCadastraCliente.setObjectName("tbCadastraCliente")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tbCadastraCliente)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frCabecalho = QtWidgets.QFrame(self.tbCadastraCliente)
        self.frCabecalho.setMinimumSize(QtCore.QSize(600, 100))
        self.frCabecalho.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frCabecalho.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frCabecalho.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frCabecalho.setObjectName("frCabecalho")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frCabecalho)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lbTitulo = QtWidgets.QLabel(self.frCabecalho)
        font = QtGui.QFont()
        font.setFamily("Linux Biolinum O")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.lbTitulo.setFont(font)
        self.lbTitulo.setStyleSheet("color: rgb(46, 52, 54)")
        self.lbTitulo.setObjectName("lbTitulo")
        self.verticalLayout_3.addWidget(self.lbTitulo)
        self.lbCorpo = QtWidgets.QLabel(self.frCabecalho)
        self.lbCorpo.setStyleSheet("color: rgb(46, 52, 54)")
        self.lbCorpo.setObjectName("lbCorpo")
        self.verticalLayout_3.addWidget(self.lbCorpo)
        self.verticalLayout_2.addWidget(self.frCabecalho)
        self.frNomeSobrenome = QtWidgets.QFrame(self.tbCadastraCliente)
        self.frNomeSobrenome.setMinimumSize(QtCore.QSize(600, 60))
        self.frNomeSobrenome.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frNomeSobrenome.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frNomeSobrenome.setObjectName("frNomeSobrenome")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frNomeSobrenome)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frNome = QtWidgets.QFrame(self.frNomeSobrenome)
        self.frNome.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frNome.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frNome.setObjectName("frNome")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frNome)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.lbNome = QtWidgets.QLabel(self.frNome)
        self.lbNome.setStyleSheet("color: rgb(46, 52, 54)")
        self.lbNome.setObjectName("lbNome")
        self.horizontalLayout_9.addWidget(self.lbNome)
        self.leNome = QtWidgets.QLineEdit(self.frNome)
        self.leNome.setStyleSheet("#leNome{\n"
"    border: 1px solid;\n"
"}")
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
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.lbSobrenome = QtWidgets.QLabel(self.frSobrenome)
        self.lbSobrenome.setStyleSheet("color: rgb(46, 52, 54)")
        self.lbSobrenome.setObjectName("lbSobrenome")
        self.horizontalLayout_10.addWidget(self.lbSobrenome)
        self.leSobrenome = QtWidgets.QLineEdit(self.frSobrenome)
        self.leSobrenome.setStyleSheet("#leSobrenome{\n"
"    border: 1px solid;\n"
"}")
        self.leSobrenome.setObjectName("leSobrenome")
        self.horizontalLayout_10.addWidget(self.leSobrenome)
        self.leSobrenome.raise_()
        self.lbSobrenome.raise_()
        self.horizontalLayout_5.addWidget(self.frSobrenome)
        self.verticalLayout_2.addWidget(self.frNomeSobrenome)
        self.frEmailTel = QtWidgets.QFrame(self.tbCadastraCliente)
        self.frEmailTel.setMinimumSize(QtCore.QSize(600, 60))
        self.frEmailTel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frEmailTel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frEmailTel.setObjectName("frEmailTel")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frEmailTel)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.frTel = QtWidgets.QFrame(self.frEmailTel)
        self.frTel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frTel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frTel.setObjectName("frTel")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frTel)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.lbTel = QtWidgets.QLabel(self.frTel)
        self.lbTel.setStyleSheet("color: rgb(46, 52, 54)")
        self.lbTel.setObjectName("lbTel")
        self.horizontalLayout_11.addWidget(self.lbTel)
        self.leTel = QtWidgets.QLineEdit(self.frTel)
        self.leTel.setStyleSheet("#leTel{\n"
"    border: 1px solid;\n"
"}")
        self.leTel.setObjectName("leTel")
        self.horizontalLayout_11.addWidget(self.leTel)
        self.horizontalLayout_6.addWidget(self.frTel)
        self.frEmail = QtWidgets.QFrame(self.frEmailTel)
        self.frEmail.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frEmail.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frEmail.setObjectName("frEmail")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frEmail)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.lbEmail = QtWidgets.QLabel(self.frEmail)
        self.lbEmail.setStyleSheet("color: rgb(46, 52, 54)")
        self.lbEmail.setObjectName("lbEmail")
        self.horizontalLayout_12.addWidget(self.lbEmail)
        self.leEmail = QtWidgets.QLineEdit(self.frEmail)
        self.leEmail.setStyleSheet("#leEmail{\n"
"    border: 1px solid;\n"
"}")
        self.leEmail.setObjectName("leEmail")
        self.horizontalLayout_12.addWidget(self.leEmail)
        self.horizontalLayout_6.addWidget(self.frEmail)
        self.verticalLayout_2.addWidget(self.frEmailTel)
        self.frCepEnd = QtWidgets.QFrame(self.tbCadastraCliente)
        self.frCepEnd.setMinimumSize(QtCore.QSize(600, 60))
        self.frCepEnd.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frCepEnd.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frCepEnd.setObjectName("frCepEnd")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frCepEnd)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.frCep = QtWidgets.QFrame(self.frCepEnd)
        self.frCep.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frCep.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frCep.setObjectName("frCep")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.frCep)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.lbCep = QtWidgets.QLabel(self.frCep)
        self.lbCep.setStyleSheet("color: rgb(46, 52, 54)")
        self.lbCep.setObjectName("lbCep")
        self.horizontalLayout_13.addWidget(self.lbCep)
        self.leCep = QtWidgets.QLineEdit(self.frCep)
        self.leCep.setStyleSheet("#leCep{\n"
"    border: 1px solid;\n"
"}")
        self.leCep.setObjectName("leCep")
        self.horizontalLayout_13.addWidget(self.leCep)
        self.horizontalLayout_7.addWidget(self.frCep)
        self.frEndereco = QtWidgets.QFrame(self.frCepEnd)
        self.frEndereco.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frEndereco.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frEndereco.setObjectName("frEndereco")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.frEndereco)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.lbEnd = QtWidgets.QLabel(self.frEndereco)
        self.lbEnd.setStyleSheet("color: rgb(46, 52, 54)")
        self.lbEnd.setObjectName("lbEnd")
        self.horizontalLayout_14.addWidget(self.lbEnd)
        self.leEnd = QtWidgets.QLineEdit(self.frEndereco)
        self.leEnd.setStyleSheet("#leEnd{\n"
"    border: 1px solid;\n"
"}")
        self.leEnd.setObjectName("leEnd")
        self.horizontalLayout_14.addWidget(self.leEnd)
        self.horizontalLayout_7.addWidget(self.frEndereco)
        self.verticalLayout_2.addWidget(self.frCepEnd)
        self.frBairroCompl = QtWidgets.QFrame(self.tbCadastraCliente)
        self.frBairroCompl.setMinimumSize(QtCore.QSize(600, 60))
        self.frBairroCompl.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frBairroCompl.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frBairroCompl.setObjectName("frBairroCompl")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frBairroCompl)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.frBairro = QtWidgets.QFrame(self.frBairroCompl)
        self.frBairro.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frBairro.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frBairro.setObjectName("frBairro")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.frBairro)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.lbBairro = QtWidgets.QLabel(self.frBairro)
        self.lbBairro.setStyleSheet("color: rgb(46, 52, 54)")
        self.lbBairro.setObjectName("lbBairro")
        self.horizontalLayout_15.addWidget(self.lbBairro)
        self.leBairro = QtWidgets.QLineEdit(self.frBairro)
        self.leBairro.setStyleSheet("#leBairro{\n"
"    border: 1px solid;\n"
"}")
        self.leBairro.setObjectName("leBairro")
        self.horizontalLayout_15.addWidget(self.leBairro)
        self.horizontalLayout_8.addWidget(self.frBairro)
        self.frComplemento = QtWidgets.QFrame(self.frBairroCompl)
        self.frComplemento.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frComplemento.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frComplemento.setObjectName("frComplemento")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.frComplemento)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.lbCompl = QtWidgets.QLabel(self.frComplemento)
        self.lbCompl.setStyleSheet("color: rgb(46, 52, 54)")
        self.lbCompl.setObjectName("lbCompl")
        self.horizontalLayout_16.addWidget(self.lbCompl)
        self.leCompl = QtWidgets.QLineEdit(self.frComplemento)
        self.leCompl.setStyleSheet("#leCompl{\n"
"    border: 1px solid;\n"
"}")
        self.leCompl.setObjectName("leCompl")
        self.horizontalLayout_16.addWidget(self.leCompl)
        self.horizontalLayout_8.addWidget(self.frComplemento)
        self.verticalLayout_2.addWidget(self.frBairroCompl)
        self.frame = QtWidgets.QFrame(self.tbCadastraCliente)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pbCadastrar = QtWidgets.QPushButton(self.frame)
        self.pbCadastrar.setMinimumSize(QtCore.QSize(80, 0))
        self.pbCadastrar.setMaximumSize(QtCore.QSize(150, 16777215))
        self.pbCadastrar.setStyleSheet("#pbCadastrar{\n"
"    background-color: #80CCE1;\n"
"}")
        self.pbCadastrar.setObjectName("pbCadastrar")
        self.verticalLayout_4.addWidget(self.pbCadastrar)
        self.verticalLayout_2.addWidget(self.frame, 0, QtCore.Qt.AlignRight)
        self.tabsCliente.addTab(self.tbCadastraCliente, "")
        self.tbInfosCliente = QtWidgets.QWidget()
        self.tbInfosCliente.setObjectName("tbInfosCliente")
        self.tabsCliente.addTab(self.tbInfosCliente, "")
        self.tbCronogramaCliente = QtWidgets.QWidget()
        self.tbCronogramaCliente.setObjectName("tbCronogramaCliente")
        self.tabsCliente.addTab(self.tbCronogramaCliente, "")
        self.tbBoletoCliente = QtWidgets.QWidget()
        self.tbBoletoCliente.setObjectName("tbBoletoCliente")
        self.tabsCliente.addTab(self.tbBoletoCliente, "")
        self.gridLayout_3.addWidget(self.tabsCliente, 0, 0, 1, 1)
        self.stkDash.addWidget(self.pgCliente)
        self.gridLayout_2.addWidget(self.stkDash, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.frStakeds)
        self.gridLayout.addWidget(self.frPrincipalDash, 1, 1, 1, 1)
        mwDash.setCentralWidget(self.wdgDash)

        self.retranslateUi(mwDash)
        self.stkDash.setCurrentIndex(1)
        self.tabsCliente.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(mwDash)

    def retranslateUi(self, mwDash):
        _translate = QtCore.QCoreApplication.translate
        mwDash.setWindowTitle(_translate("mwDash", "MainWindow"))
        self.pbHome.setText(_translate("mwDash", "Home"))
        self.pbAgenda.setText(_translate("mwDash", "Agenda"))
        self.pbCliente.setText(_translate("mwDash", "Cliente"))
        self.pbFuncionario.setText(_translate("mwDash", "funcionários"))
        self.IGNORAR_2.setText(_translate("mwDash", "DashBoard"))
        self.IGNORAR_1.setText(_translate("mwDash", "Home"))
        self.lbTitulo.setText(_translate("mwDash", "Cadastro de clientes"))
        self.lbCorpo.setText(_translate("mwDash", "Cadastre seus clientes para poder gerenciar seus créditos, débitos e grupos."))
        self.lbNome.setText(_translate("mwDash", "Nome:    "))
        self.leNome.setPlaceholderText(_translate("mwDash", "Nome"))
        self.lbSobrenome.setText(_translate("mwDash", "Sobrenome:    "))
        self.leSobrenome.setPlaceholderText(_translate("mwDash", "Sobrenome"))
        self.lbTel.setText(_translate("mwDash", "Telefone:    "))
        self.leTel.setPlaceholderText(_translate("mwDash", "Celular"))
        self.lbEmail.setText(_translate("mwDash", "E-mail:    "))
        self.leEmail.setPlaceholderText(_translate("mwDash", "E - mail"))
        self.lbCep.setText(_translate("mwDash", "CEP:    "))
        self.leCep.setPlaceholderText(_translate("mwDash", "CEP"))
        self.lbEnd.setText(_translate("mwDash", "Endereço:     "))
        self.leEnd.setPlaceholderText(_translate("mwDash", "Endereco"))
        self.lbBairro.setText(_translate("mwDash", "Bairro:    "))
        self.leBairro.setPlaceholderText(_translate("mwDash", "Bairro"))
        self.lbCompl.setText(_translate("mwDash", "Complemento:    "))
        self.leCompl.setPlaceholderText(_translate("mwDash", "Complemento"))
        self.pbCadastrar.setText(_translate("mwDash", "Cadastrar"))
        self.tabsCliente.setTabText(self.tabsCliente.indexOf(self.tbCadastraCliente), _translate("mwDash", "Cadastro"))
        self.tabsCliente.setTabText(self.tabsCliente.indexOf(self.tbInfosCliente), _translate("mwDash", "Informaçôes"))
        self.tabsCliente.setTabText(self.tabsCliente.indexOf(self.tbCronogramaCliente), _translate("mwDash", "Cronograma"))
        self.tabsCliente.setTabText(self.tabsCliente.indexOf(self.tbBoletoCliente), _translate("mwDash", "Boletos"))
import Telas.Imagens.img_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mwDash = QtWidgets.QMainWindow()
    ui = Ui_mwDash()
    ui.setupUi(mwDash)
    mwDash.show()
    sys.exit(app.exec_())
