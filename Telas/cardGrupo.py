# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cardGrupo.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_wdgGrupoCard(object):
    def setupUi(self, wdgGrupoCard):
        wdgGrupoCard.setObjectName("wdgGrupoCard")
        wdgGrupoCard.resize(440, 320)
        wdgGrupoCard.setMinimumSize(QtCore.QSize(440, 320))
        wdgGrupoCard.setMaximumSize(QtCore.QSize(440, 320))
        wdgGrupoCard.setStyleSheet("/*----------------------------------- Frames ------------------------------------*/\n"
"#frCategoria {\n"
"    background-color: rgb(52, 101, 164);\n"
"    \n"
"    border-bottom-left-radius: 12px;\n"
"    border-bottom-right-radius: 12px;\n"
"    border-top-left-radius: 0px;\n"
"    border-top-right-radius: 0px;    \n"
"}\n"
"\n"
"/*-------------------------------- Label --------------------------------------*/\n"
"#lbCategoria {\n"
"    color: #fff;\n"
"    background-color: transparent;\n"
"    border: 0px;\n"
"    font-size: 16pt;\n"
"    font-family: Ubuntu;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/*------------------------------- Tabela --------------------------------------*/\n"
"\n"
"#tblGrupoItem {\n"
"    background-color: rgba(233, 185, 110, 200);\n"
"    /*border: none;*/\n"
"    color: #444;\n"
"    margin-bottom: 8px;\n"
"    padding-right: 4px;\n"
"    padding-top: 4px;\n"
"    padding-left: 12px;\n"
"    margin-top: 8px;\n"
"}\n"
"\n"
"#tblGrupoItem::item {\n"
"    color: #fff;\n"
"}")
        self.frGrupoCard = QtWidgets.QFrame(wdgGrupoCard)
        self.frGrupoCard.setGeometry(QtCore.QRect(0, 0, 400, 280))
        self.frGrupoCard.setMaximumSize(QtCore.QSize(16777215, 280))
        self.frGrupoCard.setStyleSheet("#frGrupoCard {\n"
"    background-color: #0e90ad;\n"
"}")
        self.frGrupoCard.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frGrupoCard.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frGrupoCard.setObjectName("frGrupoCard")
        self.gridLayout = QtWidgets.QGridLayout(self.frGrupoCard)
        self.gridLayout.setContentsMargins(15, 0, 15, 0)
        self.gridLayout.setVerticalSpacing(2)
        self.gridLayout.setObjectName("gridLayout")
        self.frBottom = QtWidgets.QFrame(self.frGrupoCard)
        self.frBottom.setStyleSheet("#frBottom {\n"
"    background-color: transparent;\n"
"}")
        self.frBottom.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frBottom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frBottom.setObjectName("frBottom")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frBottom)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setHorizontalSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tblGrupoItem = QtWidgets.QTableWidget(self.frBottom)
        self.tblGrupoItem.setMinimumSize(QtCore.QSize(0, 150))
        self.tblGrupoItem.setMaximumSize(QtCore.QSize(16777215, 200))
        self.tblGrupoItem.setStyleSheet("")
        self.tblGrupoItem.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tblGrupoItem.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblGrupoItem.setAlternatingRowColors(False)
        self.tblGrupoItem.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tblGrupoItem.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tblGrupoItem.setShowGrid(False)
        self.tblGrupoItem.setObjectName("tblGrupoItem")
        self.tblGrupoItem.setColumnCount(3)
        self.tblGrupoItem.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tblGrupoItem.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblGrupoItem.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblGrupoItem.setHorizontalHeaderItem(2, item)
        self.tblGrupoItem.horizontalHeader().setVisible(False)
        self.tblGrupoItem.horizontalHeader().setStretchLastSection(True)
        self.tblGrupoItem.verticalHeader().setVisible(False)
        self.gridLayout_3.addWidget(self.tblGrupoItem, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frBottom, 2, 0, 1, 1)
        self.lbDescricao = QtWidgets.QTextEdit(self.frGrupoCard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbDescricao.sizePolicy().hasHeightForWidth())
        self.lbDescricao.setSizePolicy(sizePolicy)
        self.lbDescricao.setMinimumSize(QtCore.QSize(0, 70))
        self.lbDescricao.setMaximumSize(QtCore.QSize(16777215, 100))
        self.lbDescricao.setStyleSheet("#lbDescricao {\n"
"    border: 0px;\n"
"    background-color: transparent;\n"
"    color: #fff;\n"
"    font-family: Ubuntu;\n"
"    font-size: 12pt;\n"
"    font-style: italic;\n"
"}")
        self.lbDescricao.setReadOnly(True)
        self.lbDescricao.setObjectName("lbDescricao")
        self.gridLayout.addWidget(self.lbDescricao, 1, 0, 1, 1)
        self.lbTituloCard = QtWidgets.QLabel(self.frGrupoCard)
        self.lbTituloCard.setMinimumSize(QtCore.QSize(0, 50))
        self.lbTituloCard.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbTituloCard.setFont(font)
        self.lbTituloCard.setStyleSheet("#lbTituloCard{\n"
"    color: #fff;\n"
"    background-color: transparent;\n"
"    border: 0px;\n"
"    font-size: 16pt;\n"
"    font-family: Ubuntu;\n"
"    font-weight: bold;\n"
"}")
        self.lbTituloCard.setObjectName("lbTituloCard")
        self.gridLayout.addWidget(self.lbTituloCard, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 4, 0, 1, 1)
        self.frCategoria = QtWidgets.QFrame(wdgGrupoCard)
        self.frCategoria.setGeometry(QtCore.QRect(7, 270, 161, 35))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frCategoria.sizePolicy().hasHeightForWidth())
        self.frCategoria.setSizePolicy(sizePolicy)
        self.frCategoria.setMinimumSize(QtCore.QSize(50, 24))
        self.frCategoria.setMaximumSize(QtCore.QSize(16777215, 36))
        self.frCategoria.setSizeIncrement(QtCore.QSize(60, 0))
        self.frCategoria.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frCategoria.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frCategoria.setObjectName("frCategoria")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frCategoria)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 4)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lbCategoria = QtWidgets.QLabel(self.frCategoria)
        self.lbCategoria.setObjectName("lbCategoria")
        self.horizontalLayout.addWidget(self.lbCategoria, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.frBotoes = QtWidgets.QFrame(wdgGrupoCard)
        self.frBotoes.setGeometry(QtCore.QRect(400, 20, 30, 220))
        self.frBotoes.setMinimumSize(QtCore.QSize(30, 220))
        self.frBotoes.setMaximumSize(QtCore.QSize(30, 220))
        self.frBotoes.setStyleSheet("/*------------------------------------ Frame ------------------------------------------*/\n"
"\n"
"#frBotoes{\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"\n"
"/*----------------------------- Push Buttons ------------------------------------------*/\n"
"\n"
"#pbEditar {\n"
"    background-image: url(:/Editar/cardEditar.png);\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"    background-color: white;\n"
"}\n"
"\n"
"#pbEditar:hover {\n"
"    background-image: url(:/Editar/cardEditar.png);\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"    background-color: rgb(221, 241, 255);\n"
"}\n"
"\n"
"#pbEmailCard {\n"
"    background-image: url(:/Email/cardEmail.png);\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"    background-color: white;\n"
"}\n"
"\n"
"#pbEmailCard:hover {\n"
"    background-image: url(:/Email/cardEmail.png);\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"    background-color: rgb(221, 241, 255);\n"
"}\n"
"\n"
"#pbExcluir {\n"
"    background-image: url(:/ExcluirR/cardExcluirRed.png);\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"    background-color: #fff;\n"
"}\n"
"\n"
"#pbExcluir::hover {\n"
"    background-image: url(:/ExcluirW/cardExcluirWhite.png);\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"    background-color: #ff8d74;\n"
"}\n"
"\n"
"#pbZap {\n"
"    background-image: url(:/Whatsapp/whatsapp.png);\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"    background-color: #fff;\n"
"}\n"
"\n"
"#pbZap::hover {\n"
"    background-image: url(:/Whatsapp/whatsapp.png);\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"    background-color: rgb(237, 255, 235);\n"
"}\n"
"")
        self.frBotoes.setObjectName("frBotoes")
        self.formLayout = QtWidgets.QFormLayout(self.frBotoes)
        self.formLayout.setContentsMargins(0, 0, 0, 4)
        self.formLayout.setHorizontalSpacing(0)
        self.formLayout.setVerticalSpacing(9)
        self.formLayout.setObjectName("formLayout")
        self.pbEditar = QtWidgets.QPushButton(self.frBotoes)
        self.pbEditar.setMinimumSize(QtCore.QSize(30, 30))
        self.pbEditar.setMaximumSize(QtCore.QSize(30, 30))
        self.pbEditar.setStyleSheet("")
        self.pbEditar.setText("")
        self.pbEditar.setObjectName("pbEditar")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.pbEditar)
        self.pbEmailCard = QtWidgets.QPushButton(self.frBotoes)
        self.pbEmailCard.setMinimumSize(QtCore.QSize(30, 30))
        self.pbEmailCard.setMaximumSize(QtCore.QSize(30, 30))
        self.pbEmailCard.setStyleSheet("")
        self.pbEmailCard.setText("")
        self.pbEmailCard.setObjectName("pbEmailCard")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.pbEmailCard)
        self.pbExcluir = QtWidgets.QPushButton(self.frBotoes)
        self.pbExcluir.setMinimumSize(QtCore.QSize(30, 30))
        self.pbExcluir.setMaximumSize(QtCore.QSize(30, 30))
        self.pbExcluir.setStyleSheet("")
        self.pbExcluir.setText("")
        self.pbExcluir.setObjectName("pbExcluir")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.pbExcluir)
        self.pbZap = QtWidgets.QPushButton(self.frBotoes)
        self.pbZap.setMinimumSize(QtCore.QSize(30, 30))
        self.pbZap.setMaximumSize(QtCore.QSize(30, 30))
        self.pbZap.setStyleSheet("")
        self.pbZap.setText("")
        self.pbZap.setObjectName("pbZap")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.pbZap)
        self.frBotoes.raise_()
        self.frCategoria.raise_()
        self.frGrupoCard.raise_()

        self.retranslateUi(wdgGrupoCard)
        QtCore.QMetaObject.connectSlotsByName(wdgGrupoCard)

    def retranslateUi(self, wdgGrupoCard):
        _translate = QtCore.QCoreApplication.translate
        wdgGrupoCard.setWindowTitle(_translate("wdgGrupoCard", "Form"))
        item = self.tblGrupoItem.horizontalHeaderItem(0)
        item.setText(_translate("wdgGrupoCard", "Id"))
        item = self.tblGrupoItem.horizontalHeaderItem(1)
        item.setText(_translate("wdgGrupoCard", "Nome"))
        item = self.tblGrupoItem.horizontalHeaderItem(2)
        item.setText(_translate("wdgGrupoCard", "Sobrenome"))
        self.lbDescricao.setPlaceholderText(_translate("wdgGrupoCard", "DESCRIÇÃO"))
        self.lbTituloCard.setText(_translate("wdgGrupoCard", "Titulo"))
        self.lbCategoria.setText(_translate("wdgGrupoCard", "TextLabel"))
import Telas.Resources.cardGrupoResources


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    wdgGrupoCard = QtWidgets.QWidget()
    ui = Ui_wdgGrupoCard()
    ui.setupUi(wdgGrupoCard)
    wdgGrupoCard.show()
    sys.exit(app.exec_())
