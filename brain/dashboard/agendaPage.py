
from PyQt5.QtGui import QPainter, QColor, QFont

from Telas.dashAgenda import Ui_wdgAgenda
from datetime import datetime

from PyQt5.QtWidgets import QWidget, QCalendarWidget
from PyQt5.QtCore import QPoint


class AgendaPage(Ui_wdgAgenda, QWidget):

    def __init__(self, parent=None):
        super(AgendaPage, self).__init__(parent)

        self.setupUi(self)

        self.calendarWidget.setGridVisible(True)

        self.calendarWidget.clicked.connect(self.printDateInfo)

        self.calendarWidget.paintCell()

    def paintCell(self, painter, rect, date):
        super(AgendaPage, self).calendarWidget.paintCell(painter, rect, date)
        print(self)

        # checking if date is selected date
        if date.month() == 12 and date.day() == 20 or date == self.selectedDate():
            # saving the painter
            self.calendarWidget.painter.save()

            # criando o objeto Fonte
            font = QFont()

            # setando tamanho da fonte
            font.setPixelSize(10)

            # marcando a fonte com negrito
            font.setBold(True)

            # marcando a fonte com italic
            font.setItalic(True)

            # setting font to the painter
            painter.setFont(font)

            # Desenhando um texto
            painter.drawText(rect.topLeft() + QPoint(5, 100), "{}".format("Compromisso"))

            # restoring the painter
            painter.restore()

    def printDateInfo(self, qDate):
        # x = datetime.now().strftime("%B")
        # y = datetime(year=qDate.year(), month=qDate.dayOfWeek(), day=qDate.day())
        # print('{0}/{1}/{2}'.format(qDate.month(), qDate.day(), qDate.year()))
        # print(f'Numero de dias do ano: {qDate.dayOfYear()}')
        # print(f'Numero de dias do mÊs: {qDate.dayOfWeek()}')
        # print(f'Numero do dia da semana ano: {qDate.day()}')
        # print(x)
        # print(y)
        # print(y.strftime("%Y %B"))
        # print(self.calendarWidget.selectedDate())
        # self.lbData.setText(str(y))
        pass


