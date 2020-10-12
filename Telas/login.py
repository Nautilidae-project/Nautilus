# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow

class Ui_mwLogin(QMainWindow):

    def __init__(self, parent=None):
        super(Ui_mwLogin, self).__init__(parent)
        self.setupUi(self)


    def setupUi(self, mwLogin):
        mwLogin.setObjectName("mwLogin")
        mwLogin.setWindowModality(QtCore.Qt.NonModal)
        mwLogin.resize(1000, 711)
        mwLogin.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.163, y1:0.5625, x2:0.888, y2:0.603273, stop:0.0918367 rgba(255, 239, 214, 255), stop:0.55102 rgba(255, 255, 255, 255));")
        mwLogin.setIconSize(QtCore.QSize(25, 25))
        mwLogin.setAnimated(True)
        mwLogin.setDocumentMode(False)
        mwLogin.setTabShape(QtWidgets.QTabWidget.Rounded)
        mwLogin.setDockNestingEnabled(False)
        mwLogin.setUnifiedTitleAndToolBarOnMac(False)
        self.wdgLgin = QtWidgets.QWidget(mwLogin)
        self.wdgLgin.setObjectName("wdgLgin")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.wdgLgin)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.stkLogin = QtWidgets.QStackedWidget(self.wdgLgin)
        self.stkLogin.setObjectName("stkLogin")
        self.pgLogin = QtWidgets.QWidget()
        self.pgLogin.setObjectName("pgLogin")
        self.pbYouTube = QtWidgets.QPushButton(self.pgLogin)
        self.pbYouTube.setGeometry(QtCore.QRect(920, 640, 50, 50))
        self.pbYouTube.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.pbYouTube.setFont(font)
        self.pbYouTube.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pbYouTube.setMouseTracking(False)
        self.pbYouTube.setTabletTracking(False)
        self.pbYouTube.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pbYouTube.setAcceptDrops(False)
        self.pbYouTube.setToolTipDuration(-1)
        self.pbYouTube.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pbYouTube.setAutoFillBackground(False)
        self.pbYouTube.setStyleSheet("QPushButton {\n"
"    border-radius: 25px;\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    \n"
"    \n"
"    image: url(:/newPrefix/002-youtube.png);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(255,182,193);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(170, 140, 140);\n"
"}\n"
"\n"
"")
        self.pbYouTube.setText("")
        self.pbYouTube.setIconSize(QtCore.QSize(25, 25))
        self.pbYouTube.setCheckable(False)
        self.pbYouTube.setChecked(False)
        self.pbYouTube.setAutoRepeat(False)
        self.pbYouTube.setAutoExclusive(False)
        self.pbYouTube.setAutoDefault(False)
        self.pbYouTube.setDefault(False)
        self.pbYouTube.setFlat(False)
        self.pbYouTube.setObjectName("pbYouTube")
        self.frBordaCirculo = QtWidgets.QFrame(self.pgLogin)
        self.frBordaCirculo.setGeometry(QtCore.QRect(460, 40, 500, 500))
        self.frBordaCirculo.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.frBordaCirculo.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.frBordaCirculo.setStyleSheet("border-radius: 250px;\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0.469143, y1:0, x2:0.485, y2:1, stop:0 rgba(162, 81, 58, 255), stop:0.244898 rgba(223, 103, 60, 255), stop:0.52551 rgba(223, 140, 60, 255), stop:0.729592 rgba(223, 165, 60, 255), stop:0.887755 rgba(60, 196, 223, 255));\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0.059, y1:0.676318, x2:0.913612, y2:0.494818, stop:0.0765306 rgba(255, 248, 236, 255), stop:0.25 rgba(255, 245, 228, 255), stop:0.454082 rgba(243, 223, 197, 255), stop:0.647959 rgba(243, 216, 180, 255), stop:0.841837 rgba(243, 210, 168, 255), stop:1 rgba(243, 207, 160, 255));")
        self.frBordaCirculo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frBordaCirculo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frBordaCirculo.setObjectName("frBordaCirculo")
        self.frCirculoImputs = QtWidgets.QFrame(self.frBordaCirculo)
        self.frCirculoImputs.setGeometry(QtCore.QRect(50, 50, 400, 400))
        self.frCirculoImputs.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 200px;\n"
"border: 3px solid  rgba(255, 255, 255, 100);\n"
"")
        self.frCirculoImputs.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frCirculoImputs.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frCirculoImputs.setObjectName("frCirculoImputs")
        self.pbLogin = QtWidgets.QPushButton(self.frCirculoImputs)
        self.pbLogin.setGeometry(QtCore.QRect(40, 280, 171, 51))
        self.pbLogin.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.pbLogin.setFont(font)
        self.pbLogin.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pbLogin.setMouseTracking(False)
        self.pbLogin.setTabletTracking(False)
        self.pbLogin.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pbLogin.setAcceptDrops(False)
        self.pbLogin.setToolTipDuration(-1)
        self.pbLogin.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pbLogin.setAutoFillBackground(False)
        self.pbLogin.setStyleSheet("QPushButton {\n"
"    border-radius: 20px;\n"
"    border-color: rgb(254, 254, 254);\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(211, 143, 37);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border-color: rgb(170, 170, 170);\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(170, 140, 140);\n"
"}\n"
"\n"
"")
        self.pbLogin.setIconSize(QtCore.QSize(25, 25))
        self.pbLogin.setCheckable(False)
        self.pbLogin.setChecked(False)
        self.pbLogin.setAutoRepeat(False)
        self.pbLogin.setAutoExclusive(False)
        self.pbLogin.setAutoDefault(False)
        self.pbLogin.setDefault(False)
        self.pbLogin.setFlat(False)
        self.pbLogin.setObjectName("pbLogin")
        self.leUsuario = QtWidgets.QLineEdit(self.frCirculoImputs)
        self.leUsuario.setGeometry(QtCore.QRect(50, 210, 300, 25))
        font = QtGui.QFont()
        font.setFamily("Roboto Slab")
        font.setPointSize(12)
        self.leUsuario.setFont(font)
        self.leUsuario.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.leUsuario.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.leUsuario.setStyleSheet("border-radius: 10px;\n"
"border-bottom-color: rgb(136, 138, 133);\n"
"color: rgb(136, 138, 133);")
        self.leUsuario.setInputMethodHints(QtCore.Qt.ImhNone)
        self.leUsuario.setInputMask("")
        self.leUsuario.setText("")
        self.leUsuario.setFrame(True)
        self.leUsuario.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.leUsuario.setAlignment(QtCore.Qt.AlignCenter)
        self.leUsuario.setObjectName("leUsuario")
        self.leSenha = QtWidgets.QLineEdit(self.frCirculoImputs)
        self.leSenha.setGeometry(QtCore.QRect(50, 240, 300, 25))
        font = QtGui.QFont()
        font.setFamily("Roboto Slab")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.leSenha.setFont(font)
        self.leSenha.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.leSenha.setStyleSheet("border-radius: 10px;\n"
"color: rgb(136, 138, 133);\n"
"border-bottom-color: rgb(136, 138, 133);")
        self.leSenha.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.leSenha.setInputMask("")
        self.leSenha.setText("")
        self.leSenha.setFrame(True)
        self.leSenha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.leSenha.setAlignment(QtCore.Qt.AlignCenter)
        self.leSenha.setObjectName("leSenha")
        self.pbCadastro = QtWidgets.QPushButton(self.frCirculoImputs)
        self.pbCadastro.setGeometry(QtCore.QRect(180, 280, 170, 51))
        self.pbCadastro.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.pbCadastro.setFont(font)
        self.pbCadastro.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pbCadastro.setMouseTracking(False)
        self.pbCadastro.setTabletTracking(False)
        self.pbCadastro.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pbCadastro.setAcceptDrops(False)
        self.pbCadastro.setToolTipDuration(-1)
        self.pbCadastro.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pbCadastro.setAutoFillBackground(False)
        self.pbCadastro.setStyleSheet("QPushButton {\n"
"    border-radius: 20px;\n"
"    border-color: rgb(254, 254, 254);\n"
"    background-color: rgb(170, 170, 170);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   border-color: rgb(211, 143, 37);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"   background-color: rgb(170, 140, 140);\n"
"}")
        self.pbCadastro.setIconSize(QtCore.QSize(35, 35))
        self.pbCadastro.setCheckable(False)
        self.pbCadastro.setChecked(False)
        self.pbCadastro.setAutoRepeat(False)
        self.pbCadastro.setAutoExclusive(False)
        self.pbCadastro.setAutoDefault(False)
        self.pbCadastro.setDefault(False)
        self.pbCadastro.setFlat(False)
        self.pbCadastro.setObjectName("pbCadastro")
        self.frAvatar = QtWidgets.QFrame(self.frCirculoImputs)
        self.frAvatar.setGeometry(QtCore.QRect(100, 0, 200, 200))
        self.frAvatar.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 20px;\n"
"border-image: url(:/newPrefix/002-graduated.png);\n"
"border-radius: 100px\n"
"\n"
"\n"
"")
        self.frAvatar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frAvatar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frAvatar.setObjectName("frAvatar")
        self.leUsuario.raise_()
        self.leSenha.raise_()
        self.pbCadastro.raise_()
        self.pbLogin.raise_()
        self.frAvatar.raise_()
        self.frLogo = QtWidgets.QFrame(self.pgLogin)
        self.frLogo.setGeometry(QtCore.QRect(0, 290, 490, 90))
        self.frLogo.setStyleSheet("border-image: url(:/newPrefix/escribas_logo.png);\n"
"background-color: rgba(255, 255, 255, 0);\n"
"\n"
"\n"
"")
        self.frLogo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frLogo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frLogo.setObjectName("frLogo")
        self.lblLinha = QtWidgets.QLabel(self.pgLogin)
        self.lblLinha.setGeometry(QtCore.QRect(210, 570, 501, 17))
        self.lblLinha.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"")
        self.lblLinha.setText("")
        self.lblLinha.setPixmap(QtGui.QPixmap(":/newPrefix/linha.png"))
        self.lblLinha.setObjectName("lblLinha")
        self.lblNossaMissao = QtWidgets.QLabel(self.pgLogin)
        self.lblNossaMissao.setGeometry(QtCore.QRect(130, 590, 671, 101))
        self.lblNossaMissao.setStyleSheet("font: 25 12pt \"Roboto Slab\";\n"
"background-color: rgba(255, 255, 255, 0);")
        self.lblNossaMissao.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.lblNossaMissao.setObjectName("lblNossaMissao")
        self.pbTweeter = QtWidgets.QPushButton(self.pgLogin)
        self.pbTweeter.setGeometry(QtCore.QRect(920, 580, 50, 50))
        self.pbTweeter.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.pbTweeter.setFont(font)
        self.pbTweeter.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pbTweeter.setMouseTracking(False)
        self.pbTweeter.setTabletTracking(False)
        self.pbTweeter.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pbTweeter.setAcceptDrops(False)
        self.pbTweeter.setToolTipDuration(-1)
        self.pbTweeter.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pbTweeter.setAutoFillBackground(False)
        self.pbTweeter.setStyleSheet("QPushButton {\n"
"    border-radius: 25px;\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    \n"
"    image: url(:/newPrefix/013-twitter-1.png);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(127,255,212);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(170, 140, 140);\n"
"}\n"
"\n"
"")
        self.pbTweeter.setText("")
        self.pbTweeter.setIconSize(QtCore.QSize(25, 25))
        self.pbTweeter.setCheckable(False)
        self.pbTweeter.setChecked(False)
        self.pbTweeter.setAutoRepeat(False)
        self.pbTweeter.setAutoExclusive(False)
        self.pbTweeter.setAutoDefault(False)
        self.pbTweeter.setDefault(False)
        self.pbTweeter.setFlat(False)
        self.pbTweeter.setObjectName("pbTweeter")
        self.pbFacebook = QtWidgets.QPushButton(self.pgLogin)
        self.pbFacebook.setGeometry(QtCore.QRect(920, 520, 50, 50))
        self.pbFacebook.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.pbFacebook.setFont(font)
        self.pbFacebook.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pbFacebook.setMouseTracking(False)
        self.pbFacebook.setTabletTracking(False)
        self.pbFacebook.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pbFacebook.setAcceptDrops(False)
        self.pbFacebook.setToolTipDuration(-1)
        self.pbFacebook.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pbFacebook.setAutoFillBackground(False)
        self.pbFacebook.setStyleSheet("QPushButton {\n"
"    border-radius: 25px;\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    border-image: url(:/newPrefix/043-facebook-1.png);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(135,206,250);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(170, 140, 140);\n"
"}\n"
"\n"
"")
        self.pbFacebook.setText("")
        self.pbFacebook.setIconSize(QtCore.QSize(25, 25))
        self.pbFacebook.setCheckable(False)
        self.pbFacebook.setChecked(False)
        self.pbFacebook.setAutoRepeat(False)
        self.pbFacebook.setAutoExclusive(False)
        self.pbFacebook.setAutoDefault(False)
        self.pbFacebook.setDefault(False)
        self.pbFacebook.setFlat(False)
        self.pbFacebook.setObjectName("pbFacebook")
        self.stkLogin.addWidget(self.pgLogin)
        self.horizontalLayout.addWidget(self.stkLogin)
        mwLogin.setCentralWidget(self.wdgLgin)

        self.retranslateUi(mwLogin)
        self.stkLogin.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(mwLogin)

    def retranslateUi(self, mwLogin):
        _translate = QtCore.QCoreApplication.translate
        mwLogin.setWindowTitle(_translate("mwLogin", "MainWindow"))
        self.pbLogin.setText(_translate("mwLogin", "Login"))
        self.leUsuario.setPlaceholderText(_translate("mwLogin", "Usuário"))
        self.leSenha.setPlaceholderText(_translate("mwLogin", "Senha"))
        self.pbCadastro.setText(_translate("mwLogin", "Cadastre-se"))
        self.lblNossaMissao.setText(_translate("mwLogin", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Roboto Slab\'; font-size:12pt; font-weight:24; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; text-decoration: underline;\">Nossa Missão:</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-style:italic;\">Desenvolver a  capacidade de escrever com excelência sobre qualquer tema. Para isso, guiamos você a:</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; font-style:italic;\">*</span><span style=\" font-size:10pt; font-style:italic; text-decoration: underline;\">Aumentar seu repertório cultural</span><span style=\" font-size:10pt; font-style:italic;\">; </span><span style=\" font-size:10pt; font-weight:600; font-style:italic;\">*</span><span style=\" font-size:10pt; font-style:italic;\"> </span><span style=\" font-size:10pt; font-style:italic; text-decoration: underline;\">Organizar seus pensamentos</span><span style=\" font-size:10pt; font-style:italic;\">; </span><span style=\" font-size:10pt; font-weight:600; font-style:italic;\">*</span><span style=\" font-size:10pt; font-style:italic;\"> </span><span style=\" font-size:10pt; font-style:italic; text-decoration: underline;\">Conquistar técnicas textuais</span><span style=\" font-size:10pt; font-style:italic;\">.</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mwLogin = QtWidgets.QMainWindow()
    ui = Ui_mwLogin()
    ui.setupUi(mwLogin)
    mwLogin.show()
    sys.exit(app.exec_())

