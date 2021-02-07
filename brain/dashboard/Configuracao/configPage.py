from PyQt5.QtWidgets import QWidget, QFileDialog
from PyQt5.QtGui import QPixmap, QImage, QBrush, QPainter, QWindow
from PyQt5.QtCore import Qt, QRect

from Telas.dashConfig import Ui_wdgConfig
from brain.DAOs.daoUsuario import DaoUsuario
from brain.dashboard.Sinais import Sinais
from modelos.efeitosModel import Efeitos


class ConfigPage(Ui_wdgConfig, QWidget):

    def __init__(self, parent=None, db=None):
        super(ConfigPage, self).__init__(parent)
        self.db = db
        self.parent = parent
        self.daoUsuario = DaoUsuario(db=db)
        self.setupUi(self)

        self.efeito = Efeitos()

        self.verificaLogoSalva()
        self.pbExcluiImg.clicked.connect(self.excluiLogo)

        self.pbInsereImg.clicked.connect(self.decideLogo)

        # Instanciando os sinais
        self.sinais = Sinais()

        # Escutando/Listening sinais
        self.tabConfiguracoes.currentChanged.connect(self.onCange)

    def onCange(self, *args):
        tabEscolhida = args[0]

        if tabEscolhida == 0:
            self.lbTitulo.setText('Configurações do usuário')
            self.lbDescricao.setText('Nesta página você pode alterar as configurações referentes ao seu cadastro.')
        elif tabEscolhida == 1:
            self.lbTitulo.setText('Configurações dos clientes')
            self.lbDescricao.setText('Configurações referentes à tela de clientes.')
        elif tabEscolhida == 2:
            self.lbTitulo.setText('Configurações da agenda')
            self.lbDescricao.setText('Configurações das datas e eventos.')
        elif tabEscolhida == 3:
            self.lbTitulo.setText('Configurações financeiras')
            self.lbDescricao.setText('Configurações referentes à area financeira do Nautilus.')

    def carregaLogo(self, logoPath: str, logo=True) -> None:

        if logoPath != '':
            imageBits = open(logoPath, 'rb').read()

            # qImagem = QImage(logoPath)
            qImagem = QImage.fromData(imageBits)
            qImagem.convertToFormat(QImage.Format_ARGB32)


            imgSize = min(qImagem.width(), qImagem.height())
            quadroImg = QRect((qImagem.width() - imgSize)/2,
                                (qImagem.height() - imgSize)/2,
                                imgSize, imgSize)

            qImagem.copy(quadroImg)

            if logo:

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
            tamanho = 77*pixRatio
            pixLogo = pixLogo.scaled(tamanho, tamanho, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.lbLogo.setPixmap(pixLogo)
            self.efeito.shadowCards([self.lbLogo], radius=5, offset=(1, 3), color=(63, 63, 63, 90))

    def excluiLogo(self):
        self.carregaLogo('Telas/Imagens/addLogo.png', logo=False)
        self.daoUsuario.atualizaLogoPath('Telas/Imagens/addLogo.png', idUsuario=self.parent.usuarioModel.userId)

    def decideLogo(self):

        logoPath = QFileDialog.getOpenFileName(directory='/home/', options=QFileDialog.DontUseNativeDialog, filter="PNG (*.png);;JPG (*.jpg)")

        if logoPath is not None:
            self.salvaLogoPath(logoPath[0])
            self.carregaLogo(logoPath[0])

    def salvaLogoPath(self, logoPath):
        usuarioAtivo = self.parent.usuarioModel
        self.daoUsuario.atualizaLogoPath(logoPath, idUsuario=usuarioAtivo.userId)
        self.parent.menssagemSistema('Logo salvo com sucesso!')

    def verificaLogoSalva(self):
        logoPath = self.daoUsuario.buscaLogoPath(self.parent.usuarioModel.userId)
        if logoPath is None or logoPath == '':
            self.carregaLogo('Telas/Imagens/addLogo.png', logo=False)
        else:
            self.carregaLogo(logoPath, logo=False)

