# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cadastro.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow
import resource

class Ui_mwCadastro(object):

    # home = pyqtSignal()
    #
    # def __init__(self, parent=None):
    #     super(Ui_mwCadastro, self).__init__(parent)
    #     self.setupUi(self)
    #     self.pbVoltarLogin.clicked.connect(self.goHome)
    #     self.home.connect(self.parent().backHome)
    #
    # def goHome(self):
    #     self.home.emit()

    def setupUi(self, mwCadastro):
        mwCadastro.setObjectName("mwCadastro")
        mwCadastro.setWindowModality(QtCore.Qt.NonModal)
        mwCadastro.resize(998, 700)
        mwCadastro.setStyleSheet("/*\n"
"Azul1 = #58b3cc\n"
"Azul2 = #58b3cc\n"
"Azul3 = #16437c\n"
"*/\n"
"QWidget {\n"
"    background-color: #16437c;\n"
"}\n"
"\n"
"QFrame {\n"
"    border-radius: 40% solid;\n"
"    background-color: #DAA520;\n"
"}\n"
"\n"
"QLabel {\n"
"    font: bold;\n"
"    border-radius: 10px;\n"
"    border: 2px solid  #ffffff;\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: #DAA520;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    border-radius: 10px;\n"
"    border: 2px solid #ffffff;\n"
"    color: rgb(136, 138, 133);\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"")
        mwCadastro.setIconSize(QtCore.QSize(25, 25))
        mwCadastro.setAnimated(True)
        mwCadastro.setDocumentMode(False)
        mwCadastro.setTabShape(QtWidgets.QTabWidget.Rounded)
        mwCadastro.setDockNestingEnabled(False)
        mwCadastro.setUnifiedTitleAndToolBarOnMac(False)
        self.wdgCadastro = QtWidgets.QWidget(mwCadastro)
        self.wdgCadastro.setObjectName("wdgCadastro")
        self.frCentral = QtWidgets.QFrame(self.wdgCadastro)
        self.frCentral.setEnabled(True)
        self.frCentral.setGeometry(QtCore.QRect(130, 20, 741, 661))
        self.frCentral.setStyleSheet("#frCentral {\n"
"    background-color: #396d9d;\n"
"    border-radius: 50%;\n"
"    /*\n"
"    border: 5px solid rgb(211, 143, 37);\n"
"*/\n"
"    border: 5px solid #DAA520;\n"
"}\n"
"\n"
"")
        self.frCentral.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frCentral.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frCentral.setObjectName("frCentral")
        self.leNomeEmpresa = QtWidgets.QLineEdit(self.frCentral)
        self.leNomeEmpresa.setEnabled(True)
        self.leNomeEmpresa.setGeometry(QtCore.QRect(180, 40, 450, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto Slab")
        font.setPointSize(12)
        self.leNomeEmpresa.setFont(font)
        self.leNomeEmpresa.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.leNomeEmpresa.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.leNomeEmpresa.setStyleSheet("")
        self.leNomeEmpresa.setInputMethodHints(QtCore.Qt.ImhNone)
        self.leNomeEmpresa.setInputMask("")
        self.leNomeEmpresa.setText("")
        self.leNomeEmpresa.setFrame(True)
        self.leNomeEmpresa.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.leNomeEmpresa.setAlignment(QtCore.Qt.AlignCenter)
        self.leNomeEmpresa.setObjectName("leNomeEmpresa")
        self.lbEmpresa = QtWidgets.QLabel(self.frCentral)
        self.lbEmpresa.setGeometry(QtCore.QRect(110, 40, 81, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lbEmpresa.setFont(font)
        self.lbEmpresa.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lbEmpresa.setStyleSheet("")
        self.lbEmpresa.setAlignment(QtCore.Qt.AlignCenter)
        self.lbEmpresa.setObjectName("lbEmpresa")
        self.lbFantasia = QtWidgets.QLabel(self.frCentral)
        self.lbFantasia.setGeometry(QtCore.QRect(110, 100, 81, 30))
        self.lbFantasia.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lbFantasia.setStyleSheet("")
        self.lbFantasia.setAlignment(QtCore.Qt.AlignCenter)
        self.lbFantasia.setObjectName("lbFantasia")
        self.lbCNPJ = QtWidgets.QLabel(self.frCentral)
        self.lbCNPJ.setGeometry(QtCore.QRect(110, 160, 81, 30))
        self.lbCNPJ.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lbCNPJ.setStyleSheet("")
        self.lbCNPJ.setAlignment(QtCore.Qt.AlignCenter)
        self.lbCNPJ.setObjectName("lbCNPJ")
        self.lbEmail = QtWidgets.QLabel(self.frCentral)
        self.lbEmail.setGeometry(QtCore.QRect(110, 220, 81, 30))
        self.lbEmail.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lbEmail.setStyleSheet("")
        self.lbEmail.setAlignment(QtCore.Qt.AlignCenter)
        self.lbEmail.setObjectName("lbEmail")
        self.lbTelefone = QtWidgets.QLabel(self.frCentral)
        self.lbTelefone.setGeometry(QtCore.QRect(110, 280, 81, 30))
        self.lbTelefone.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lbTelefone.setStyleSheet("")
        self.lbTelefone.setAlignment(QtCore.Qt.AlignCenter)
        self.lbTelefone.setObjectName("lbTelefone")
        self.lbEndereco = QtWidgets.QLabel(self.frCentral)
        self.lbEndereco.setGeometry(QtCore.QRect(110, 340, 81, 30))
        self.lbEndereco.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lbEndereco.setStyleSheet("")
        self.lbEndereco.setAlignment(QtCore.Qt.AlignCenter)
        self.lbEndereco.setObjectName("lbEndereco")
        self.lbCEP = QtWidgets.QLabel(self.frCentral)
        self.lbCEP.setGeometry(QtCore.QRect(110, 400, 81, 30))
        self.lbCEP.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lbCEP.setStyleSheet("")
        self.lbCEP.setAlignment(QtCore.Qt.AlignCenter)
        self.lbCEP.setObjectName("lbCEP")
        self.lbSenha = QtWidgets.QLabel(self.frCentral)
        self.lbSenha.setGeometry(QtCore.QRect(110, 460, 81, 30))
        self.lbSenha.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lbSenha.setStyleSheet("")
        self.lbSenha.setAlignment(QtCore.Qt.AlignCenter)
        self.lbSenha.setObjectName("lbSenha")
        self.leNomeFantasia = QtWidgets.QLineEdit(self.frCentral)
        self.leNomeFantasia.setGeometry(QtCore.QRect(180, 100, 450, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto Slab")
        font.setPointSize(12)
        self.leNomeFantasia.setFont(font)
        self.leNomeFantasia.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.leNomeFantasia.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.leNomeFantasia.setStyleSheet("")
        self.leNomeFantasia.setInputMethodHints(QtCore.Qt.ImhNone)
        self.leNomeFantasia.setInputMask("")
        self.leNomeFantasia.setText("")
        self.leNomeFantasia.setFrame(True)
        self.leNomeFantasia.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.leNomeFantasia.setAlignment(QtCore.Qt.AlignCenter)
        self.leNomeFantasia.setObjectName("leNomeFantasia")
        self.leCNPJ = QtWidgets.QLineEdit(self.frCentral)
        self.leCNPJ.setGeometry(QtCore.QRect(180, 160, 450, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto Slab")
        font.setPointSize(12)
        self.leCNPJ.setFont(font)
        self.leCNPJ.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.leCNPJ.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.leCNPJ.setStyleSheet("")
        self.leCNPJ.setInputMethodHints(QtCore.Qt.ImhNone)
        self.leCNPJ.setInputMask("")
        self.leCNPJ.setText("")
        self.leCNPJ.setFrame(True)
        self.leCNPJ.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.leCNPJ.setAlignment(QtCore.Qt.AlignCenter)
        self.leCNPJ.setObjectName("leCNPJ")
        self.leSenha = QtWidgets.QLineEdit(self.frCentral)
        self.leSenha.setGeometry(QtCore.QRect(180, 460, 450, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto Slab")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.leSenha.setFont(font)
        self.leSenha.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.leSenha.setStyleSheet("")
        self.leSenha.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.leSenha.setInputMask("")
        self.leSenha.setText("")
        self.leSenha.setFrame(True)
        self.leSenha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.leSenha.setAlignment(QtCore.Qt.AlignCenter)
        self.leSenha.setDragEnabled(False)
        self.leSenha.setReadOnly(False)
        self.leSenha.setClearButtonEnabled(False)
        self.leSenha.setObjectName("leSenha")
        self.leEndereco = QtWidgets.QLineEdit(self.frCentral)
        self.leEndereco.setGeometry(QtCore.QRect(180, 340, 450, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto Slab")
        font.setPointSize(12)
        self.leEndereco.setFont(font)
        self.leEndereco.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.leEndereco.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.leEndereco.setStyleSheet("")
        self.leEndereco.setInputMethodHints(QtCore.Qt.ImhNone)
        self.leEndereco.setInputMask("")
        self.leEndereco.setText("")
        self.leEndereco.setFrame(True)
        self.leEndereco.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.leEndereco.setAlignment(QtCore.Qt.AlignCenter)
        self.leEndereco.setObjectName("leEndereco")
        self.leCEP = QtWidgets.QLineEdit(self.frCentral)
        self.leCEP.setGeometry(QtCore.QRect(180, 400, 450, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto Slab")
        font.setPointSize(12)
        self.leCEP.setFont(font)
        self.leCEP.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.leCEP.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.leCEP.setStyleSheet("")
        self.leCEP.setInputMethodHints(QtCore.Qt.ImhNone)
        self.leCEP.setInputMask("")
        self.leCEP.setText("")
        self.leCEP.setFrame(True)
        self.leCEP.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.leCEP.setAlignment(QtCore.Qt.AlignCenter)
        self.leCEP.setObjectName("leCEP")
        self.leEmail = QtWidgets.QLineEdit(self.frCentral)
        self.leEmail.setGeometry(QtCore.QRect(180, 220, 450, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto Slab")
        font.setPointSize(12)
        self.leEmail.setFont(font)
        self.leEmail.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.leEmail.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.leEmail.setStyleSheet("")
        self.leEmail.setInputMethodHints(QtCore.Qt.ImhNone)
        self.leEmail.setInputMask("")
        self.leEmail.setText("")
        self.leEmail.setFrame(True)
        self.leEmail.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.leEmail.setAlignment(QtCore.Qt.AlignCenter)
        self.leEmail.setObjectName("leEmail")
        self.leTelefone = QtWidgets.QLineEdit(self.frCentral)
        self.leTelefone.setGeometry(QtCore.QRect(180, 280, 450, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto Slab")
        font.setPointSize(12)
        self.leTelefone.setFont(font)
        self.leTelefone.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.leTelefone.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.leTelefone.setStyleSheet("")
        self.leTelefone.setInputMethodHints(QtCore.Qt.ImhNone)
        self.leTelefone.setInputMask("")
        self.leTelefone.setText("")
        self.leTelefone.setFrame(True)
        self.leTelefone.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.leTelefone.setAlignment(QtCore.Qt.AlignCenter)
        self.leTelefone.setObjectName("leTelefone")
        self.pbFazerCadastro = QtWidgets.QPushButton(self.frCentral)
        self.pbFazerCadastro.setGeometry(QtCore.QRect(420, 580, 171, 51))
        self.pbFazerCadastro.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.pbFazerCadastro.setFont(font)
        self.pbFazerCadastro.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pbFazerCadastro.setMouseTracking(False)
        self.pbFazerCadastro.setTabletTracking(False)
        self.pbFazerCadastro.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pbFazerCadastro.setAcceptDrops(False)
        self.pbFazerCadastro.setToolTipDuration(-1)
        self.pbFazerCadastro.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pbFazerCadastro.setAutoFillBackground(False)
        self.pbFazerCadastro.setStyleSheet("QPushButton {\n"
"    border-radius: 20px;\n"
"    border: 5px solid #DAA520;\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: #396d9d;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    border-color:#ffffff;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(170, 140, 140);\n"
"}\n"
"\n"
"")
        self.pbFazerCadastro.setIconSize(QtCore.QSize(25, 25))
        self.pbFazerCadastro.setCheckable(False)
        self.pbFazerCadastro.setChecked(False)
        self.pbFazerCadastro.setAutoRepeat(False)
        self.pbFazerCadastro.setAutoExclusive(False)
        self.pbFazerCadastro.setAutoDefault(False)
        self.pbFazerCadastro.setDefault(False)
        self.pbFazerCadastro.setFlat(False)
        self.pbFazerCadastro.setObjectName("pbFazerCadastro")
        self.pbVoltarLogin = QtWidgets.QPushButton(self.frCentral)
        self.pbVoltarLogin.setGeometry(QtCore.QRect(170, 580, 170, 51))
        self.pbVoltarLogin.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.pbVoltarLogin.setFont(font)
        self.pbVoltarLogin.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pbVoltarLogin.setMouseTracking(False)
        self.pbVoltarLogin.setTabletTracking(False)
        self.pbVoltarLogin.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pbVoltarLogin.setAcceptDrops(False)
        self.pbVoltarLogin.setToolTipDuration(-1)
        self.pbVoltarLogin.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pbVoltarLogin.setAutoFillBackground(False)
        self.pbVoltarLogin.setStyleSheet("QPushButton {\n"
"    border-radius: 20px;\n"
"    border: 5px solid #DAA520;\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: #396d9d;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    border-color:#ffffff;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(170, 140, 140);\n"
"}\n"
"\n"
"")
        self.pbVoltarLogin.setIconSize(QtCore.QSize(35, 35))
        self.pbVoltarLogin.setCheckable(False)
        self.pbVoltarLogin.setChecked(False)
        self.pbVoltarLogin.setAutoRepeat(False)
        self.pbVoltarLogin.setAutoExclusive(False)
        self.pbVoltarLogin.setAutoDefault(False)
        self.pbVoltarLogin.setDefault(False)
        self.pbVoltarLogin.setFlat(False)
        self.pbVoltarLogin.setObjectName("pbVoltarLogin")
        self.leSenha_2 = QtWidgets.QLineEdit(self.frCentral)
        self.leSenha_2.setGeometry(QtCore.QRect(180, 520, 450, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto Slab")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.leSenha_2.setFont(font)
        self.leSenha_2.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.leSenha_2.setStyleSheet("")
        self.leSenha_2.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.leSenha_2.setInputMask("")
        self.leSenha_2.setText("")
        self.leSenha_2.setFrame(True)
        self.leSenha_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.leSenha_2.setAlignment(QtCore.Qt.AlignCenter)
        self.leSenha_2.setDragEnabled(False)
        self.leSenha_2.setReadOnly(False)
        self.leSenha_2.setClearButtonEnabled(False)
        self.leSenha_2.setObjectName("leSenha_2")
        self.lbSenha_2 = QtWidgets.QLabel(self.frCentral)
        self.lbSenha_2.setGeometry(QtCore.QRect(110, 520, 81, 30))
        self.lbSenha_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lbSenha_2.setStyleSheet("")
        self.lbSenha_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lbSenha_2.setObjectName("lbSenha_2")
        self.leNomeEmpresa.raise_()
        self.leNomeFantasia.raise_()
        self.leCNPJ.raise_()
        self.leSenha.raise_()
        self.leEndereco.raise_()
        self.leCEP.raise_()
        self.leEmail.raise_()
        self.leTelefone.raise_()
        self.lbFantasia.raise_()
        self.lbCNPJ.raise_()
        self.lbTelefone.raise_()
        self.lbEndereco.raise_()
        self.lbSenha.raise_()
        self.lbEmail.raise_()
        self.lbEmpresa.raise_()
        self.lbCEP.raise_()
        self.pbFazerCadastro.raise_()
        self.pbVoltarLogin.raise_()
        self.leSenha_2.raise_()
        self.lbSenha_2.raise_()
        self.frEsquerda = QtWidgets.QFrame(self.wdgCadastro)
        self.frEsquerda.setGeometry(QtCore.QRect(110, 60, 80, 600))
        self.frEsquerda.setStyleSheet("")
        self.frEsquerda.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frEsquerda.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frEsquerda.setObjectName("frEsquerda")
        self.frDireita = QtWidgets.QFrame(self.wdgCadastro)
        self.frDireita.setGeometry(QtCore.QRect(810, 60, 80, 600))
        self.frDireita.setStyleSheet("")
        self.frDireita.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frDireita.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frDireita.setObjectName("frDireita")
        self.frEsquerda.raise_()
        self.frDireita.raise_()
        self.frCentral.raise_()
        mwCadastro.setCentralWidget(self.wdgCadastro)

        self.retranslateUi(mwCadastro)
        QtCore.QMetaObject.connectSlotsByName(mwCadastro)
        mwCadastro.setTabOrder(self.pbFazerCadastro, self.leNomeEmpresa)
        mwCadastro.setTabOrder(self.leNomeEmpresa, self.leNomeFantasia)
        mwCadastro.setTabOrder(self.leNomeFantasia, self.leCNPJ)
        mwCadastro.setTabOrder(self.leCNPJ, self.leEmail)
        mwCadastro.setTabOrder(self.leEmail, self.leTelefone)
        mwCadastro.setTabOrder(self.leTelefone, self.leEndereco)
        mwCadastro.setTabOrder(self.leEndereco, self.leCEP)
        mwCadastro.setTabOrder(self.leCEP, self.leSenha)
        mwCadastro.setTabOrder(self.leSenha, self.leSenha_2)
        mwCadastro.setTabOrder(self.leSenha_2, self.pbVoltarLogin)

    def retranslateUi(self, mwCadastro):
        _translate = QtCore.QCoreApplication.translate
        mwCadastro.setWindowTitle(_translate("mwCadastro", "MainWindow"))
        self.leNomeEmpresa.setPlaceholderText(_translate("mwCadastro", "Nome da Empresa"))
        self.lbEmpresa.setText(_translate("mwCadastro", "Empresa"))
        self.lbFantasia.setText(_translate("mwCadastro", "Fantasia"))
        self.lbCNPJ.setText(_translate("mwCadastro", "CNPJ"))
        self.lbEmail.setText(_translate("mwCadastro", "E-mail"))
        self.lbTelefone.setText(_translate("mwCadastro", "Telefone"))
        self.lbEndereco.setText(_translate("mwCadastro", "Endereço"))
        self.lbCEP.setText(_translate("mwCadastro", "CEP"))
        self.lbSenha.setText(_translate("mwCadastro", "Senha"))
        self.leNomeFantasia.setPlaceholderText(_translate("mwCadastro", "Nome da Fantasia"))
        self.leCNPJ.setPlaceholderText(_translate("mwCadastro", "CNPJ"))
        self.leSenha.setPlaceholderText(_translate("mwCadastro", "Senha"))
        self.leEndereco.setPlaceholderText(_translate("mwCadastro", "Emdereço"))
        self.leCEP.setPlaceholderText(_translate("mwCadastro", "CEP"))
        self.leEmail.setPlaceholderText(_translate("mwCadastro", "E-mail"))
        self.leTelefone.setPlaceholderText(_translate("mwCadastro", "Telefone"))
        self.pbFazerCadastro.setText(_translate("mwCadastro", "Cadastre-se"))
        self.pbVoltarLogin.setText(_translate("mwCadastro", "Voltar"))
        self.leSenha_2.setPlaceholderText(_translate("mwCadastro", "Senha"))
        self.lbSenha_2.setText(_translate("mwCadastro", "Senha"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mwCadastro = QtWidgets.QMainWindow()
    ui = Ui_mwCadastro()
    ui.setupUi(mwCadastro)
    mwCadastro.show()
    sys.exit(app.exec_())

