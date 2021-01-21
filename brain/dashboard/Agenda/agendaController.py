# importing libraries 
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


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

    def paintCell(self, painter, rect, date):
        super(CalendarioController, self).paintCell(painter, rect, date)

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
                "{}".format("evento hoje"),
            )

            # restoring the painter
            painter.restore()
