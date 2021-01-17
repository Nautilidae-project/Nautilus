from PyQt5.QtWidgets import QGraphicsDropShadowEffect


class Efeitos:

    def shadowCards(self, cards: list, radius: int = 20, offset: int = 7):
        
        for card in cards:
            # criando um QGraphicsDropShadowEffect object
            shadow = QGraphicsDropShadowEffect()

            # esfumaçando sombra (blur radius)
            shadow.setBlurRadius(20)

            # deslocamento da sombra (setting offset)
            shadow.setOffset(7)

            # adicionando sombra na label
            card.setGraphicsEffect(shadow)