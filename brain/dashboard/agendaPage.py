from PyQt5 import QtCore, QtGui
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

        # for d in (QtCore.Qt.Saturday, QtCore.Qt.Sunday,):
        #     fmt = self.weekdayTextFormat(d)
        #     fmt.setForeground(QtCore.Qt.darkGray)
        #     self.setWeekdayTextFormat(d, fmt)


        #if date.month() == 12 and date.day() == 20 or date == self.selectedDate():

    def paintCell(self, painter, rect, date):
        if date == self.selectedDate():
            painter.save()
            painter.fillRect(rect, QtGui.QColor("#D3D3D3"))
            painter.setPen(QtCore.Qt.NoPen)
            painter.setBrush(QtGui.QColor("#33B5E5"))
            r = QtCore.QRect(QtCore.QPoint(), min(rect.width(), rect.height()) * QtCore.QSize(1, 1))
            r.moveCenter(rect.center())
            painter.drawEllipse(r)
            painter.setPen(QtGui.QPen(QtGui.QColor("gray")))
            painter.drawText(rect, QtCore.Qt.AlignCenter, str(date.day()))
            painter.restore()
        else:
            super(AgendaPage, self).paintCell(painter, rect, date)

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


