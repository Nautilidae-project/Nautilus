from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QGraphicsDropShadowEffect


class Efeitos:

    def shadowCards(self, widgets: list, radius: int = 20, offset: tuple = (1, 7), color: tuple = (63, 63, 63, 180),
                    parentOnly=False):

        for widget in widgets:
            # criando um QGraphicsDropShadowEffect object
            shadow = QGraphicsDropShadowEffect()

            # esfumaçando sombra (blur radius)
            shadow.setBlurRadius(radius)

            shadow.setColor(QColor(*color))

            # deslocamento da sombra (setting offset)
            # shadow.setOffset(offset)
            shadow.setXOffset(offset[0])
            shadow.setYOffset(offset[1])

            # adicionando sombra na label
            widget.setGraphicsEffect(shadow)

            if parentOnly:
                for widget in widget.children():
                    widget.setGraphicsEffect(None)
