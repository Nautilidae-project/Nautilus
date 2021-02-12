from PyQt5.QtWidgets import QWidget, QFileDialog

from Telas.dashConfig import Ui_wdgConfig
from brain.DAOs.daoUsuario import DaoUsuario
from brain.dashboard.Configuracao.localWidgets.categoriaWidget import CategoriaCard
from brain.dashboard.Sinais import Sinais
from modelos.efeitosModel import Efeitos

from brain.funcoesAuxiliares import transformaImgCirculo

class ConfigPage(Ui_wdgConfig, QWidget):

    def __init__(self, parent=None, db=None):
        super(ConfigPage, self).__init__(parent)
        self.db = db
        self.parent = parent
        self.daoUsuario = DaoUsuario(db=db)
        self.setupUi(self)

        self.vlCategorias.addWidget(CategoriaCard(parent=self, db=db))

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

    def carregaLogo(self, logoPath: str, isLogo=True):
        logo = transformaImgCirculo(logoPath, isLogo=isLogo)

        self.lbLogo.setPixmap(logo)
        self.efeito.shadowCards([self.lbLogo], radius=5, offset=(1, 3), color=(63, 63, 63, 90))


    def excluiLogo(self):
        self.carregaLogo('Telas/Imagens/addLogo.png', isLogo=False)
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
            self.carregaLogo('Telas/Imagens/addLogo.png', isLogo=False)
        else:
            self.carregaLogo(logoPath, isLogo=False)

