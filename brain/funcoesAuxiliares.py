import datetime

from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QImage, QBrush, QPainter, QPixmap, QWindow
from PyQt5.QtWidgets import QMessageBox

def mascaraCelular(celular):
    return f'({celular[0:2]}) {celular[2:3]}.{celular[3:7]}-{celular[7:]}'


def mascaraCNPJ(cnpj):
    return f'{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:]}'


def mascaraCep(cep):
    return f'{cep[:5]}-{cep[5:]}'

def macaraFormaPagamento(pagamento: str):
    if (pagamento.upper() == 'CC'):
        return 'Cartão de crédito'
    else:
        return 'Outras opções'

def mascaraMeses(data: datetime.date):
    return f'{data.day} de {meses[data.month]} de {data.year}'

def getValor(valor: str):
    auxValor = valor.replace(',', '.')
    floatValor = float(auxValor.split(' ')[1])
    return floatValor

def isTrueInt(lista):
    if [bool(i) for i in lista[11]][0]:
        return 1
    else:
        return 0

def isTrueBool(data):
    if [bool(i) for i in data][0]:
        return False
    else:
        return True

formasPagamento = {
    'Cartão de crédito' : 'CC',
    'Outras opções' : 'OP'
}

meses = {
    1: 'Janeiro',
    2: 'Fevereiro',
    3: 'Março',
    4: 'Abril',
    5: 'Maio',
    6: 'Junho',
    7: 'Julho',
    8: 'Agosto',
    9: 'Setembro',
    10: 'Outubro',
    11: 'Novembro',
    12: 'Dezembro'
}


def transformaImgCirculo(logoPath: str, isLogo=True, raio: int = 39):
    if logoPath != '':
        imageBits = open(logoPath, 'rb').read()

        qImagem = QImage.fromData(imageBits)
        qImagem.convertToFormat(QImage.Format_ARGB32)

        imgSize = min(qImagem.width(), qImagem.height())
        quadroImg = QRect((qImagem.width() - imgSize) / 2,
                          (qImagem.height() - imgSize) / 2,
                          imgSize, imgSize)

        qImagem.copy(quadroImg)

        if isLogo:

            borda = QImage(imgSize, imgSize, QImage.Format_ARGB32)
            borda.fill(Qt.transparent)

            pincel = QBrush(qImagem)

            pintor = QPainter(borda)
            pintor.setBrush(pincel)
            pintor.setPen(Qt.NoPen)
            pintor.setRenderHint(QPainter.Antialiasing, True)
            pintor.setRenderHint(QPainter.HighQualityAntialiasing, True)
            pintor.drawEllipse(0, 0, imgSize, imgSize)
            pintor.end()

            pixLogo = QPixmap.fromImage(borda)
        else:
            pixLogo = QPixmap(logoPath)

        pixRatio = QWindow().devicePixelRatio()
        pixLogo.setDevicePixelRatio(pixRatio)
        tamanho = raio * 2 * pixRatio
        return pixLogo.scaled(tamanho, tamanho, Qt.KeepAspectRatio, Qt.SmoothTransformation)