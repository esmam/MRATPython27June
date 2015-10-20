__author__ = 'esmab'
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QGridLayout, QLabel, QLineEdit
from PyQt5.QtWidgets import QTextEdit, QMenuBar,QWidget, QDialog, QApplication,QMainWindow
#from  PyQt5.QtWidgets.QMainWindow import QMainWindow


#from ttestformSourceTemporalPTHRESHOLD import Ui_Form

from temporalANOVAsource import Ui_Form


class ANOVAwindow(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(ANOVAwindow, self).__init__(parent)
        self.setupUi(self)

if __name__ == '__main__':

    app = QApplication(sys.argv)

    #form1 = ttestwindow()

    #form1.show()

    sys.exit(app.exec_())
