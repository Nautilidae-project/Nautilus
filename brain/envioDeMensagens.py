import os
import sys

import requests
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import QAction, QPushButton, QCheckBox, QComboBox, QLabel, QCalendarWidget, \
    QFileDialog, QColorDialog, QTextEdit, QFontDialog, QApplication, QMessageBox, QMainWindow, QWidget

from Telas.Email import Ui_Form
from modelos.envioDeEmailModel import enviaEmail


class Mensagens(Ui_Form, QWidget):

    def __init__(self):
        super(Mensagens, self).__init__()
        self.setupUi(self)

        self.center()

        self.pbAnexar.clicked.connect(self.open)
        self.pbEnviar.clicked.connect(self.enviar)

        # self.selecionaArquivo()

    def enviar(self):
        id = self.leId.text()
        nome = self.leNome.text()
        email = self.leEmail.text()
        arquivo = self.lbRecebeNomeArquivo.text()

        titulo = self.leTitulo.text()
        mensagem = f"""Cliente -->  ID: {id} | Nome: {nome}
        
        {self.textEdit.toPlainText()}"""

        enviaEmail(titulo, mensagem, email, arquivo)

    def open(self):
        op = QFileDialog.getOpenFileName()
        print(op)
        self.lbRecebeNomeArquivo.setText(op[0])

    def  selecionaArquivo(self):
        # TODO 1: Pegando imagem url e Abrindo local para salvar a imagen
        url = "https://im.ziffdavisinternational.com/ign_br/screenshot/default/screenshot-4_n4bk.png"
        r = requests.get(url)
        image = r.content

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, options = QFileDialog.getSaveFileName(self, "Save Image", r"/home/renansoares/Imagens",
                                                        "All Files (*)", options=options)

        if fileName:
            with open(fileName, "wb") as f:
                f.write(image)
        # TODO 1: Fim

    def center(self):
        frameGm = self.frameGeometry()
        screen = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
        centerPoint = QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())


if __name__ == '__main__':

    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Mensagens()
    ui.show()
    sys.exit(app.exec_())


