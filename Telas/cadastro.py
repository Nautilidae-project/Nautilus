# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cadastro.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mwCadastro(object):
    def setupUi(self, mwCadastro):
        mwCadastro.setObjectName("mwCadastro")
        mwCadastro.setWindowModality(QtCore.Qt.NonModal)
        mwCadastro.resize(1000, 800)
        mwCadastro.setMinimumSize(QtCore.QSize(1000, 800))
        font = QtGui.QFont()
        font.setPointSize(9)
        mwCadastro.setFont(font)
        mwCadastro.setStyleSheet("/*\n"
"Azul1 = #58b3cc\n"
"Azul2 = #0E90AD\n"
"Azul3 = #3Ed0DA\n"
"Azul4 = #3E5F8A\n"
"*/\n"
"QWidget {\n"
"    background-color: #3E5F8A;\n"
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
        self.frInformacoes = QtWidgets.QFrame(self.wdgCadastro)
        self.frInformacoes.setEnabled(True)
        self.frInformacoes.setGeometry(QtCore.QRect(120, 80, 741, 681))
        self.frInformacoes.setStyleSheet("/*\n"
"Azul2 = #0E90AD\n"
"Azul4 = #16437c\n"
"*/\n"
"#frInformacoes {\n"
"    background-color: #0E90AD;\n"
"    border-radius: 50%;\n"
"    /*\n"
"    border: 5px solid rgb(211, 143, 37);\n"
"*/\n"
"    border: 5px solid #DAA520;\n"
"}\n"
"\n"
"")
        self.frInformacoes.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frInformacoes.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frInformacoes.setObjectName("frInformacoes")
        self.leNomeEmpresa = QtWidgets.QLineEdit(self.frInformacoes)
        self.leNomeEmpresa.setEnabled(True)
        self.leNomeEmpresa.setGeometry(QtCore.QRect(170, 310, 450, 30))
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
        self.lbEmpresa = QtWidgets.QLabel(self.frInformacoes)
        self.lbEmpresa.setGeometry(QtCore.QRect(110, 310, 81, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lbEmpresa.setFont(font)
        self.lbEmpresa.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lbEmpresa.setStyleSheet("")
        self.lbEmpresa.setAlignment(QtCore.Qt.AlignCenter)
        self.lbEmpresa.setObjectName("lbEmpresa")
        self.lbFantasia = QtWidgets.QLabel(self.frInformacoes)
        self.lbFantasia.setGeometry(QtCore.QRect(110, 360, 81, 30))
        self.lbFantasia.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lbFantasia.setStyleSheet("")
        self.lbFantasia.setAlignment(QtCore.Qt.AlignCenter)
        self.lbFantasia.setObjectName("lbFantasia")
        self.lbCNPJ = QtWidgets.QLabel(self.frInformacoes)
        self.lbCNPJ.setGeometry(QtCore.QRect(110, 410, 81, 30))
        self.lbCNPJ.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lbCNPJ.setStyleSheet("")
        self.lbCNPJ.setAlignment(QtCore.Qt.AlignCenter)
        self.lbCNPJ.setObjectName("lbCNPJ")
        self.lbEmail = QtWidgets.QLabel(self.frInformacoes)
        self.lbEmail.setGeometry(QtCore.QRect(110, 210, 81, 30))
        self.lbEmail.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lbEmail.setStyleSheet("")
        self.lbEmail.setAlignment(QtCore.Qt.AlignCenter)
        self.lbEmail.setObjectName("lbEmail")
        self.lbTelefone = QtWidgets.QLabel(self.frInformacoes)
        self.lbTelefone.setGeometry(QtCore.QRect(110, 460, 81, 30))
        self.lbTelefone.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lbTelefone.setStyleSheet("")
        self.lbTelefone.setAlignment(QtCore.Qt.AlignCenter)
        self.lbTelefone.setObjectName("lbTelefone")
        self.lbEndereco = QtWidgets.QLabel(self.frInformacoes)
        self.lbEndereco.setGeometry(QtCore.QRect(110, 560, 81, 30))
        self.lbEndereco.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lbEndereco.setStyleSheet("")
        self.lbEndereco.setAlignment(QtCore.Qt.AlignCenter)
        self.lbEndereco.setObjectName("lbEndereco")
        self.lbCEP = QtWidgets.QLabel(self.frInformacoes)
        self.lbCEP.setGeometry(QtCore.QRect(110, 510, 81, 30))
        self.lbCEP.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lbCEP.setStyleSheet("")
        self.lbCEP.setAlignment(QtCore.Qt.AlignCenter)
        self.lbCEP.setObjectName("lbCEP")
        self.lbSenha = QtWidgets.QLabel(self.frInformacoes)
        self.lbSenha.setGeometry(QtCore.QRect(110, 110, 81, 30))
        self.lbSenha.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lbSenha.setStyleSheet("")
        self.lbSenha.setAlignment(QtCore.Qt.AlignCenter)
        self.lbSenha.setObjectName("lbSenha")
        self.leNomeFantasia = QtWidgets.QLineEdit(self.frInformacoes)
        self.leNomeFantasia.setGeometry(QtCore.QRect(170, 360, 450, 30))
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
        self.leCNPJ = QtWidgets.QLineEdit(self.frInformacoes)
        self.leCNPJ.setGeometry(QtCore.QRect(170, 410, 450, 30))
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
        self.leSenha = QtWidgets.QLineEdit(self.frInformacoes)
        self.leSenha.setGeometry(QtCore.QRect(170, 110, 450, 30))
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
        self.leEndereco = QtWidgets.QLineEdit(self.frInformacoes)
        self.leEndereco.setGeometry(QtCore.QRect(170, 560, 450, 30))
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
        self.leCEP = QtWidgets.QLineEdit(self.frInformacoes)
        self.leCEP.setGeometry(QtCore.QRect(170, 510, 450, 30))
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
        self.leEmail = QtWidgets.QLineEdit(self.frInformacoes)
        self.leEmail.setGeometry(QtCore.QRect(170, 210, 450, 30))
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
        self.leTelefone = QtWidgets.QLineEdit(self.frInformacoes)
        self.leTelefone.setGeometry(QtCore.QRect(170, 460, 450, 30))
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
        self.pbFazerCadastro = QtWidgets.QPushButton(self.frInformacoes)
        self.pbFazerCadastro.setGeometry(QtCore.QRect(420, 610, 171, 51))
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
"    background-color: #0E90AD;\n"
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
        self.pbVoltarLogin = QtWidgets.QPushButton(self.frInformacoes)
        self.pbVoltarLogin.setGeometry(QtCore.QRect(150, 610, 170, 51))
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
"    background-color: #0E90AD;\n"
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
        self.leSenhaConfirma = QtWidgets.QLineEdit(self.frInformacoes)
        self.leSenhaConfirma.setGeometry(QtCore.QRect(170, 160, 450, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto Slab")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.leSenhaConfirma.setFont(font)
        self.leSenhaConfirma.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.leSenhaConfirma.setStyleSheet("")
        self.leSenhaConfirma.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.leSenhaConfirma.setInputMask("")
        self.leSenhaConfirma.setText("")
        self.leSenhaConfirma.setFrame(True)
        self.leSenhaConfirma.setEchoMode(QtWidgets.QLineEdit.Password)
        self.leSenhaConfirma.setAlignment(QtCore.Qt.AlignCenter)
        self.leSenhaConfirma.setDragEnabled(False)
        self.leSenhaConfirma.setReadOnly(False)
        self.leSenhaConfirma.setClearButtonEnabled(False)
        self.leSenhaConfirma.setObjectName("leSenhaConfirma")
        self.lbSenhaConfirma = QtWidgets.QLabel(self.frInformacoes)
        self.lbSenhaConfirma.setGeometry(QtCore.QRect(110, 160, 81, 30))
        self.lbSenhaConfirma.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lbSenhaConfirma.setStyleSheet("")
        self.lbSenhaConfirma.setAlignment(QtCore.Qt.AlignCenter)
        self.lbSenhaConfirma.setObjectName("lbSenhaConfirma")
        self.leNomeUsuario = QtWidgets.QLineEdit(self.frInformacoes)
        self.leNomeUsuario.setEnabled(True)
        self.leNomeUsuario.setGeometry(QtCore.QRect(170, 60, 450, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto Slab")
        font.setPointSize(12)
        self.leNomeUsuario.setFont(font)
        self.leNomeUsuario.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.leNomeUsuario.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.leNomeUsuario.setStyleSheet("")
        self.leNomeUsuario.setInputMethodHints(QtCore.Qt.ImhNone)
        self.leNomeUsuario.setInputMask("")
        self.leNomeUsuario.setText("")
        self.leNomeUsuario.setFrame(True)
        self.leNomeUsuario.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.leNomeUsuario.setAlignment(QtCore.Qt.AlignCenter)
        self.leNomeUsuario.setObjectName("leNomeUsuario")
        self.lbUsuario = QtWidgets.QLabel(self.frInformacoes)
        self.lbUsuario.setGeometry(QtCore.QRect(110, 60, 81, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lbUsuario.setFont(font)
        self.lbUsuario.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lbUsuario.setStyleSheet("")
        self.lbUsuario.setAlignment(QtCore.Qt.AlignCenter)
        self.lbUsuario.setObjectName("lbUsuario")
        self.lbInfoLoginTexto = QtWidgets.QLabel(self.frInformacoes)
        self.lbInfoLoginTexto.setGeometry(QtCore.QRect(100, 30, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Fira Sans")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.lbInfoLoginTexto.setFont(font)
        self.lbInfoLoginTexto.setStyleSheet("#lbInfoLoginTexto {\n"
"    \n"
"    font: 80  18pt \"Fira Sans\";\n"
"    background-color: rgba(0, 0, 0,0);\n"
"    border: 0px\n"
"}")
        self.lbInfoLoginTexto.setAlignment(QtCore.Qt.AlignCenter)
        self.lbInfoLoginTexto.setObjectName("lbInfoLoginTexto")
        self.lbInfoEmpresaTexto = QtWidgets.QLabel(self.frInformacoes)
        self.lbInfoEmpresaTexto.setGeometry(QtCore.QRect(120, 280, 321, 31))
        self.lbInfoEmpresaTexto.setStyleSheet("#lbInfoEmpresaTexto {\n"
"    \n"
"    font: 80  18pt \"Fira Sans\";\n"
"    background-color: rgba(0, 0, 0,0);\n"
"    border: 0px\n"
"}")
        self.lbInfoEmpresaTexto.setAlignment(QtCore.Qt.AlignCenter)
        self.lbInfoEmpresaTexto.setObjectName("lbInfoEmpresaTexto")
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
        self.leSenhaConfirma.raise_()
        self.lbSenhaConfirma.raise_()
        self.leNomeUsuario.raise_()
        self.lbUsuario.raise_()
        self.lbInfoLoginTexto.raise_()
        self.lbInfoEmpresaTexto.raise_()
        self.frEsquerda = QtWidgets.QFrame(self.wdgCadastro)
        self.frEsquerda.setGeometry(QtCore.QRect(100, 110, 80, 620))
        self.frEsquerda.setStyleSheet("")
        self.frEsquerda.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frEsquerda.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frEsquerda.setObjectName("frEsquerda")
        self.frDireita = QtWidgets.QFrame(self.wdgCadastro)
        self.frDireita.setGeometry(QtCore.QRect(800, 110, 80, 620))
        self.frDireita.setStyleSheet("")
        self.frDireita.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frDireita.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frDireita.setObjectName("frDireita")
        self.lbCadastroTexto = QtWidgets.QLabel(self.wdgCadastro)
        self.lbCadastroTexto.setGeometry(QtCore.QRect(290, 3, 400, 121))
        font = QtGui.QFont()
        font.setFamily("Fira Sans")
        font.setPointSize(38)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.lbCadastroTexto.setFont(font)
        self.lbCadastroTexto.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lbCadastroTexto.setStyleSheet("#lbCadastroTexto{\n"
"    font: 80  38pt \"Fira Sans\";\n"
"    border-radius: 50px;\n"
"    border: 5px solid  #DAA520;\n"
"    background-color: #0E90AD;\n"
"    padding: 20;\n"
"}")
        self.lbCadastroTexto.setTextFormat(QtCore.Qt.AutoText)
        self.lbCadastroTexto.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.lbCadastroTexto.setWordWrap(False)
        self.lbCadastroTexto.setIndent(-1)
        self.lbCadastroTexto.setOpenExternalLinks(False)
        self.lbCadastroTexto.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.lbCadastroTexto.setObjectName("lbCadastroTexto")
        self.lbCadastroTexto.raise_()
        self.frEsquerda.raise_()
        self.frDireita.raise_()
        self.frInformacoes.raise_()
        mwCadastro.setCentralWidget(self.wdgCadastro)

        self.retranslateUi(mwCadastro)
        QtCore.QMetaObject.connectSlotsByName(mwCadastro)
        mwCadastro.setTabOrder(self.pbFazerCadastro, self.leNomeUsuario)
        mwCadastro.setTabOrder(self.leNomeUsuario, self.leSenha)
        mwCadastro.setTabOrder(self.leSenha, self.leSenhaConfirma)
        mwCadastro.setTabOrder(self.leSenhaConfirma, self.leEmail)
        mwCadastro.setTabOrder(self.leEmail, self.leNomeEmpresa)
        mwCadastro.setTabOrder(self.leNomeEmpresa, self.leNomeFantasia)
        mwCadastro.setTabOrder(self.leNomeFantasia, self.leCNPJ)
        mwCadastro.setTabOrder(self.leCNPJ, self.leTelefone)
        mwCadastro.setTabOrder(self.leTelefone, self.leCEP)
        mwCadastro.setTabOrder(self.leCEP, self.leEndereco)
        mwCadastro.setTabOrder(self.leEndereco, self.pbVoltarLogin)

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
        self.leNomeFantasia.setPlaceholderText(_translate("mwCadastro", "Nome Fantasia"))
        self.leCNPJ.setPlaceholderText(_translate("mwCadastro", "CNPJ"))
        self.leSenha.setPlaceholderText(_translate("mwCadastro", "Senha"))
        self.leEndereco.setPlaceholderText(_translate("mwCadastro", "Endereço"))
        self.leCEP.setPlaceholderText(_translate("mwCadastro", "CEP"))
        self.leEmail.setPlaceholderText(_translate("mwCadastro", "E-mail"))
        self.leTelefone.setPlaceholderText(_translate("mwCadastro", "Telefone"))
        self.pbFazerCadastro.setText(_translate("mwCadastro", "Cadastre-se"))
        self.pbVoltarLogin.setText(_translate("mwCadastro", "Voltar"))
        self.leSenhaConfirma.setPlaceholderText(_translate("mwCadastro", "Senha"))
        self.lbSenhaConfirma.setText(_translate("mwCadastro", "Senha"))
        self.leNomeUsuario.setPlaceholderText(_translate("mwCadastro", "Nome de Usuário"))
        self.lbUsuario.setText(_translate("mwCadastro", "Usuário"))
        self.lbInfoLoginTexto.setText(_translate("mwCadastro", "Informações de Login"))
        self.lbInfoEmpresaTexto.setText(_translate("mwCadastro", "Informações da Empresa"))
        self.lbCadastroTexto.setText(_translate("mwCadastro", "CADASTRO"))

import Telas.login_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mwCadastro = QtWidgets.QMainWindow()
    ui = Ui_mwCadastro()
    ui.setupUi(mwCadastro)
    mwCadastro.show()
    sys.exit(app.exec_())

