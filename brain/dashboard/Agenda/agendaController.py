from PyQt5.QtWidgets import QWidget
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5 import QtWidgets

from Telas.calendario import Ui_Form


class AgendaController(Ui_Form, QWidget):

    def __init__(self):
        super(AgendaController, self).__init__()
        self.setupUi(self)

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
        # else:
        #     super(AgendaPage, self).paintCell(painter, rect, date)

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = AgendaController()
    ui.show()
    sys.exit(app.exec_())