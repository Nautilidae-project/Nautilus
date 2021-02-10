# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'criaCategoriaWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CategoriaCard(object):
    def setupUi(self, CategoriaCard):
        CategoriaCard.setObjectName("CategoriaCard")
        CategoriaCard.setEnabled(True)
        CategoriaCard.resize(280, 185)
        CategoriaCard.setStyleSheet("/*-------------------------------- Buttons --------------------------------------*/\n"
"\n"
"QPushButton {\n"
"    border: 1px solid transparent;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"#pbConfirmar {\n"
"    font-family: Ubuntu;\n"
"\n"
"    background-color: rgba(115, 210, 22, 180);\n"
"    border-radius: 6px;\n"
"    color: white;\n"
"}\n"
"\n"
"#pbConfirmar:hover {\n"
"    font-family: Ubuntu;\n"
"\n"
"    background-color: rgb(255, 253, 235);\n"
"    border-radius: 6px;\n"
"    border: 2px solid rgba(115, 210, 22, 180);\n"
"    color: rgb(85, 87, 83);\n"
"}\n"
"\n"
"#pbCancelar{\n"
"    font-family: Ubuntu;\n"
"\n"
"    background-color: rgb(255, 120, 120);\n"
"    border-radius: 6px;\n"
"    color: white;\n"
"}\n"
"\n"
"#pbCancelar:hover {\n"
"    font-family: Ubuntu;\n"
"\n"
"    background-color: rgb(255, 253, 235);\n"
"    border-radius: 6px;\n"
"    border: 2px solid rgb(255, 120, 120);\n"
"    color: rgb(85, 87, 83);\n"
"}\n"
"\n"
"/*--------------------------- Labels ---------------------------*/\n"
"\n"
"#lbTitulo {\n"
"    color: rgb(85, 87, 83);\n"
"/*    color: white;*/\n"
"    background-color: transparent;\n"
"    border: 0px;\n"
"    font-size: 16pt;\n"
"    font-family: Ubuntu;\n"
"\n"
"    margin-left: 4px;\n"
"}\n"
"\n"
"\n"
"/*------------------------- Frames -----------------------------------*/\n"
"#frTop {\n"
"    background-color: rgb(198, 179, 255);\n"
"    \n"
"    border-top-left-radius: 12px;\n"
"    border-bottom-right-radius: 12px;\n"
"    border-top-right-radius: 12px;\n"
"    border-bottom-left-radius: 2px;\n"
"}\n"
"\n"
"#frColors {\n"
"    background-color: rgb(174, 159, 221);\n"
"    \n"
"    border-bottom-left-radius: 12px;\n"
"    border-bottom-right-radius: 12px;\n"
"    border-top-left-radius: 0px;\n"
"    border-top-right-radius: 0px;    \n"
"}\n"
"\n"
"/*------------------------ Radio Button ----------------------------------\n"
"QRadioButton::indicator::unchecked {\n"
"    background-color: rgb(252, 233, 79);\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator::checked {\n"
"    background-color: rgb(252, 233, 79);\n"
"    border-radius: 6px;\n"
"    border: 3px solid white;\n"
"}*/")
        self.frTop = QtWidgets.QFrame(CategoriaCard)
        self.frTop.setGeometry(QtCore.QRect(0, 0, 280, 150))
        self.frTop.setMinimumSize(QtCore.QSize(280, 150))
        self.frTop.setMaximumSize(QtCore.QSize(150, 16777215))
        self.frTop.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frTop.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frTop.setObjectName("frTop")
        self.lbTitulo = QtWidgets.QLabel(self.frTop)
        self.lbTitulo.setGeometry(QtCore.QRect(0, 10, 281, 31))
        self.lbTitulo.setObjectName("lbTitulo")
        self.leNovaCategoria = QtWidgets.QLineEdit(self.frTop)
        self.leNovaCategoria.setGeometry(QtCore.QRect(10, 50, 221, 25))
        self.leNovaCategoria.setObjectName("leNovaCategoria")
        self.pbConfirmar = QtWidgets.QPushButton(self.frTop)
        self.pbConfirmar.setGeometry(QtCore.QRect(180, 100, 83, 25))
        self.pbConfirmar.setObjectName("pbConfirmar")
        self.pbCancelar = QtWidgets.QPushButton(self.frTop)
        self.pbCancelar.setGeometry(QtCore.QRect(80, 100, 83, 25))
        self.pbCancelar.setObjectName("pbCancelar")
        self.frColors = QtWidgets.QFrame(CategoriaCard)
        self.frColors.setGeometry(QtCore.QRect(2, 150, 250, 35))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frColors.sizePolicy().hasHeightForWidth())
        self.frColors.setSizePolicy(sizePolicy)
        self.frColors.setMinimumSize(QtCore.QSize(250, 35))
        self.frColors.setMaximumSize(QtCore.QSize(250, 35))
        self.frColors.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frColors.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frColors.setObjectName("frColors")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frColors)
        self.horizontalLayout.setContentsMargins(4, 4, 2, 4)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.rbCor1 = QtWidgets.QRadioButton(self.frColors)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rbCor1.sizePolicy().hasHeightForWidth())
        self.rbCor1.setSizePolicy(sizePolicy)
        self.rbCor1.setMinimumSize(QtCore.QSize(20, 20))
        self.rbCor1.setMaximumSize(QtCore.QSize(20, 20))
        self.rbCor1.setText("")
        self.rbCor1.setObjectName("rbCor1")
        self.horizontalLayout.addWidget(self.rbCor1)
        self.rbCor2 = QtWidgets.QRadioButton(self.frColors)
        self.rbCor2.setMinimumSize(QtCore.QSize(20, 20))
        self.rbCor2.setMaximumSize(QtCore.QSize(20, 20))
        self.rbCor2.setText("")
        self.rbCor2.setObjectName("rbCor2")
        self.horizontalLayout.addWidget(self.rbCor2)
        self.rbCor3 = QtWidgets.QRadioButton(self.frColors)
        self.rbCor3.setMinimumSize(QtCore.QSize(20, 20))
        self.rbCor3.setMaximumSize(QtCore.QSize(20, 20))
        self.rbCor3.setText("")
        self.rbCor3.setObjectName("rbCor3")
        self.horizontalLayout.addWidget(self.rbCor3)
        self.rbCor4 = QtWidgets.QRadioButton(self.frColors)
        self.rbCor4.setMinimumSize(QtCore.QSize(20, 20))
        self.rbCor4.setMaximumSize(QtCore.QSize(20, 20))
        self.rbCor4.setText("")
        self.rbCor4.setObjectName("rbCor4")
        self.horizontalLayout.addWidget(self.rbCor4)
        self.rbCor5 = QtWidgets.QRadioButton(self.frColors)
        self.rbCor5.setMinimumSize(QtCore.QSize(20, 20))
        self.rbCor5.setMaximumSize(QtCore.QSize(20, 20))
        self.rbCor5.setText("")
        self.rbCor5.setObjectName("rbCor5")
        self.horizontalLayout.addWidget(self.rbCor5)
        self.rbCor6 = QtWidgets.QRadioButton(self.frColors)
        self.rbCor6.setMinimumSize(QtCore.QSize(20, 20))
        self.rbCor6.setMaximumSize(QtCore.QSize(20, 20))
        self.rbCor6.setText("")
        self.rbCor6.setObjectName("rbCor6")
        self.horizontalLayout.addWidget(self.rbCor6)
        self.rbCor7 = QtWidgets.QRadioButton(self.frColors)
        self.rbCor7.setMinimumSize(QtCore.QSize(20, 20))
        self.rbCor7.setMaximumSize(QtCore.QSize(20, 20))
        self.rbCor7.setText("")
        self.rbCor7.setObjectName("rbCor7")
        self.horizontalLayout.addWidget(self.rbCor7)
        self.rbCor8 = QtWidgets.QRadioButton(self.frColors)
        self.rbCor8.setMinimumSize(QtCore.QSize(20, 20))
        self.rbCor8.setMaximumSize(QtCore.QSize(20, 20))
        self.rbCor8.setText("")
        self.rbCor8.setObjectName("rbCor8")
        self.horizontalLayout.addWidget(self.rbCor8)
        self.rbCor9 = QtWidgets.QRadioButton(self.frColors)
        self.rbCor9.setMinimumSize(QtCore.QSize(20, 20))
        self.rbCor9.setMaximumSize(QtCore.QSize(20, 20))
        self.rbCor9.setText("")
        self.rbCor9.setObjectName("rbCor9")
        self.horizontalLayout.addWidget(self.rbCor9)
        self.rbCor10 = QtWidgets.QRadioButton(self.frColors)
        self.rbCor10.setMinimumSize(QtCore.QSize(20, 20))
        self.rbCor10.setMaximumSize(QtCore.QSize(20, 20))
        self.rbCor10.setText("")
        self.rbCor10.setObjectName("rbCor10")
        self.horizontalLayout.addWidget(self.rbCor10)
        self.frColors.raise_()
        self.frTop.raise_()

        self.retranslateUi(CategoriaCard)
        QtCore.QMetaObject.connectSlotsByName(CategoriaCard)

    def retranslateUi(self, CategoriaCard):
        _translate = QtCore.QCoreApplication.translate
        CategoriaCard.setWindowTitle(_translate("CategoriaCard", "Form"))
        self.lbTitulo.setText(_translate("CategoriaCard", "Crie uma categoria"))
        self.leNovaCategoria.setPlaceholderText(_translate("CategoriaCard", "Nerds"))
        self.pbConfirmar.setText(_translate("CategoriaCard", "CRIAR"))
        self.pbCancelar.setText(_translate("CategoriaCard", "CANCELAR"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CategoriaCard = QtWidgets.QWidget()
    ui = Ui_CategoriaCard()
    ui.setupUi(CategoriaCard)
    CategoriaCard.show()
    sys.exit(app.exec_())
