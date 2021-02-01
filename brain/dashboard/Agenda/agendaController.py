# importing libraries 
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QMouseEvent
import sys

from brain.DAOs.daoEvento import DaoEvento


class CalendarioController(QCalendarWidget):

    # constructor
    def __init__(self, parent=None):
        super(CalendarioController, self).__init__(parent)
        self.setStyleSheet("""
        		 /*Tool button styles */
        QCalendarWidget QToolButton {

        	height:40px;
        	width:500px;
        	color:white;
        	font-size:20px;
        	icon-size:56px,56px;
        	background-color: #DFD880;

        }

          /*normal days */
        QCalendarWidget QAbstractItemView:enabled {


        font-size:18px;
        color: #444;
        background-color: #80CCE1;
        selection-background-color:rgb(128,64,64);
        selection-color:rgb(0,255,0);
        }

          /* header row */
        QCalendarWidget  QWidget{

        alternate-background-color: #FAFAFA;

        }
        		""")

        self.daoEvento = DaoEvento()

        print(self.daoEvento.findAll()[8][4])
        print(type(self.daoEvento.findAll()[8][4]))

        self.atualiza = True


    def paintCell(self, painter, rect, date):
        super(CalendarioController, self).paintCell(painter, rect, date)

        # if date == self.grupos.findAll()[2][4]:
        # print(f'Selected ---> {self.selectedDate()}')
        # print(f'grupos ---> {self.grupos.findAll()[2][4]}')
        # x = [self.daoEvento.findAll()]
        # print(x)
        # checking if date is selected date



        eventos = len(self.daoEvento.findAll())

        for i in range(eventos):
            if date == self.daoEvento.findAll()[i][4]:
                painter.save()
                # Cor do funda da area Selecionada
                painter.fillRect(rect, QtGui.QColor("#80CCE1"))

                painter.setPen(QtCore.Qt.NoPen)
                painter.setBrush(QtGui.QColor("#daa520"))
                r = QtCore.QRect(QtCore.QPoint(), min(rect.width(), rect.height()) * QtCore.QSize(1, 1))
                r.moveCenter(rect.center())
                painter.drawEllipse(r)
                painter.setPen(QtGui.QPen(QtGui.QColor("gray")))
                painter.drawText(rect, QtCore.Qt.AlignCenter, str(date.day()))
                painter.restore()

