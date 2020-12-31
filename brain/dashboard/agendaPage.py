from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5 import QtWidgets

from Telas.dashAgenda import Ui_wdgAgenda
from datetime import datetime

from PyQt5.QtWidgets import QWidget, QCalendarWidget
from PyQt5.QtCore import QPoint

from brain.dashboard.agendaController import AgendaController


class AgendaPage(Ui_wdgAgenda, QWidget):

    def __init__(self, parent=None):
        super(AgendaPage, self).__init__(parent)

        self.setupUi(self)

        self.calendario = AgendaController()

        self.vlAgenda.addWidget(self.calendario)

        # self.calendarWidget.setGridVisible(True)

        # self.calendarWidget.clicked.connect(self.printDateInfo)

        # for d in (QtCore.Qt.Saturday, QtCore.Qt.Sunday,):
        #     fmt = self.weekdayTextFormat(d)
        #     fmt.setForeground(QtCore.Qt.darkGray)
        #     self.setWeekdayTextFormat(d, fmt)


        #if date.month() == 12 and date.day() == 20 or date == self.selectedDate():



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


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = AgendaPage()
    ui.show()
    sys.exit(app.exec_())