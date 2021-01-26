from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QGraphicsDropShadowEffect


class Efeitos:

    def shadowCards(self, cards: list, radius: int = 20, offset: tuple = (1, 7), color: tuple = (63, 63, 63, 180)):
        
        for card in cards:
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
            card.setGraphicsEffect(shadow)