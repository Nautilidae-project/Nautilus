from PyQt5.QtWidgets import QWidget

from Telas.cardGrupo import Ui_wdgGrupoCard
from modelos.grupoModel import GrupoModelo


class GruposCard(Ui_wdgGrupoCard, QWidget):

    def __init__(self, parent=None, grupo: GrupoModelo = None,):
        super(GruposCard, self).__init__()
        self.setupUi(self)
        self.parent = parent

        if grupo is not None:
            self.lbTituloCard.setText(grupo.titulo)
            self.lbDescricao.setText(grupo.descricao)
