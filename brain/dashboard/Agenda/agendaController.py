from datetime import datetime

from PyQt5.QtGui import QPainter, QFont
from PyQt5.QtCore import QRect, QPoint

from PyQt5.QtWidgets import QWidget, QCalendarWidget
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5 import QtWidgets

from Telas.calendario import Ui_Form


class AgendaController(Ui_Form, QCalendarWidget):

    def __init__(self):
        super(AgendaController, self).__init__()
        self.setupUi(self)

        # self.calendar = self.calendarWidget

        # self.calendar.clicked.connect(self.teste)


    def teste(self, qDate):
        print('ola')
        painter = QPainter(self)
        y = datetime(year=qDate.year(), month=qDate.dayOfWeek(), day=qDate.day())

        self.calendar.dateTextFormat()

    def paintCell(self, painter, rect, date):
        super(AgendaController, self).paintCell(painter, rect, date)

        # checking if date is selected date
        if date == self.selectedDate():
            # saving the painter
            painter.save()

            # creating a QFont object
            font = QFont()

            # setting pixel size of the font
            font.setPixelSize(15)

            # making font bold
            font.setBold(True)

            # making font italic
            font.setItalic(True)

            # setting font to the painter
            painter.setFont(font)

            # drawing text
            painter.drawText(
                rect.topLeft() + QPoint(10, 10),
                "{}".format("Evento"),
            )

            # restoring the painter
            painter.restore()


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = AgendaController()
    ui.show()
    sys.exit(app.exec_())