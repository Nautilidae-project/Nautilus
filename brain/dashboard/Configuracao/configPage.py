from PyQt5.QtWidgets import QWidget

from Telas.dashConfig import Ui_wdgConfig
from brain.dashboard.Sinais import Sinais


class ConfigPage(Ui_wdgConfig, QWidget):
    def __init__(self, parent=None, db=None):
        super(ConfigPage, self).__init__(parent)
        self.db = db
        self.setupUi(self)

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


