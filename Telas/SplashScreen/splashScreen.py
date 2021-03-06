# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'splashScreen.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        MainWindow.setMinimumSize(QtCore.QSize(800, 480))
        MainWindow.setMaximumSize(QtCore.QSize(800, 480))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frBg = QtWidgets.QFrame(self.centralwidget)
        self.frBg.setStyleSheet("#frBg {\n"
"/*    background-image: url(:/imagemBg/imagemBg.png);*/\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"    border-image:  url(:/imagemBg/imagemBg.png);\n"
"}")
        self.frBg.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frBg.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frBg.setObjectName("frBg")
        self.pbarSplash = QtWidgets.QProgressBar(self.frBg)
        self.pbarSplash.setGeometry(QtCore.QRect(50, 350, 701, 23))
        self.pbarSplash.setStyleSheet("#pbarSplash {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(30, 41, 99);\n"
"    color: rgb(211, 215, 207);\n"
"    border-style: none;\n"
"    text-align: center;\n"
"}\n"
"\n"
"#pbarSplash::chunk {\n"
"    border-radius: 10px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.506, x2:1, y2:0.5, stop:0 rgba(74, 172, 82, 255), stop:1 rgba(86, 179, 204, 255));\n"
"}")
        self.pbarSplash.setProperty("value", 24)
        self.pbarSplash.setObjectName("pbarSplash")
        self.lbCreated = QtWidgets.QLabel(self.frBg)
        self.lbCreated.setGeometry(QtCore.QRect(693, 440, 81, 20))
        font = QtGui.QFont()
        font.setFamily("Fira Sans")
        font.setPointSize(9)
        font.setItalic(True)
        self.lbCreated.setFont(font)
        self.lbCreated.setStyleSheet("#lbCreated {\n"
"    color: rgb(238, 238, 236);\n"
"}")
        self.lbCreated.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbCreated.setObjectName("lbCreated")
        self.lbCreated_2 = QtWidgets.QLabel(self.frBg)
        self.lbCreated_2.setGeometry(QtCore.QRect(630, 440, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Fira Sans")
        font.setPointSize(6)
        font.setItalic(True)
        self.lbCreated_2.setFont(font)
        self.lbCreated_2.setStyleSheet("#lbCreated_2 {\n"
"    color: rgb(238, 238, 236);\n"
"}")
        self.lbCreated_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbCreated_2.setObjectName("lbCreated_2")
        self.lbInfo = QtWidgets.QLabel(self.frBg)
        self.lbInfo.setGeometry(QtCore.QRect(23, 380, 751, 20))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        self.lbInfo.setFont(font)
        self.lbInfo.setStyleSheet("#lbInfo {\n"
"    color: rgb(238, 238, 236);\n"
"}")
        self.lbInfo.setAlignment(QtCore.Qt.AlignCenter)
        self.lbInfo.setObjectName("lbInfo")
        self.horizontalLayout.addWidget(self.frBg)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lbCreated.setText(_translate("MainWindow", "Nautilus Group"))
        self.lbCreated_2.setText(_translate("MainWindow", "Created by"))
        self.lbInfo.setText(_translate("MainWindow", "LOADING..."))
import Telas.SplashScreen.splash_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
