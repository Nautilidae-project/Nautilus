# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cliente.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_wdgCliente(QtWidgets.QWidget):

    # ----------------------------------
    def __init__(self, parent=None):
        super(Ui_wdgCliente, self).__init__()
        self.setupUi(self)

    # ----------------------------------

    def setupUi(self, wdgCliente):
        wdgCliente.setObjectName("wdgCliente")
        wdgCliente.resize(1024, 754)
        self.gridLayout = QtWidgets.QGridLayout(wdgCliente)
        self.gridLayout.setObjectName("gridLayout")
        self.tabsCliente = QtWidgets.QTabWidget(wdgCliente)
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
        self.gridLayout.addWidget(self.tabsCliente, 0, 0, 1, 1)

        self.retranslateUi(wdgCliente)
        self.tabsCliente.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(wdgCliente)

    def retranslateUi(self, wdgCliente):
        _translate = QtCore.QCoreApplication.translate
        wdgCliente.setWindowTitle(_translate("wdgCliente", "Form"))
        self.lbTitulo.setText(_translate("wdgCliente", "Cadastro de clientes"))
        self.lbCorpo.setText(_translate("wdgCliente", "Cadastre seus clientes para poder gerenciar seus créditos, débitos e grupos."))
        self.lbNome.setText(_translate("wdgCliente", "Nome:    "))
        self.leNome.setPlaceholderText(_translate("wdgCliente", "Nome"))
        self.lbSobrenome.setText(_translate("wdgCliente", "Sobrenome:    "))
        self.leSobrenome.setPlaceholderText(_translate("wdgCliente", "Sobrenome"))
        self.lbTel.setText(_translate("wdgCliente", "Telefone:    "))
        self.leTel.setPlaceholderText(_translate("wdgCliente", "Celular"))
        self.lbEmail.setText(_translate("wdgCliente", "E-mail:    "))
        self.leEmail.setPlaceholderText(_translate("wdgCliente", "E - mail"))
        self.lbCep.setText(_translate("wdgCliente", "CEP:    "))
        self.leCep.setPlaceholderText(_translate("wdgCliente", "CEP"))
        self.lbEnd.setText(_translate("wdgCliente", "Endereço:     "))
        self.leEnd.setPlaceholderText(_translate("wdgCliente", "Endereco"))
        self.lbBairro.setText(_translate("wdgCliente", "Bairro:    "))
        self.leBairro.setPlaceholderText(_translate("wdgCliente", "Bairro"))
        self.lbCompl.setText(_translate("wdgCliente", "Complemento:    "))
        self.leCompl.setPlaceholderText(_translate("wdgCliente", "Complemento"))
        self.pbCadastrar.setText(_translate("wdgCliente", "Cadastrar"))
        self.tabsCliente.setTabText(self.tabsCliente.indexOf(self.tbCadastraCliente), _translate("wdgCliente", "Cadastro"))
        self.tabsCliente.setTabText(self.tabsCliente.indexOf(self.tbInfosCliente), _translate("wdgCliente", "Informaçôes"))
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