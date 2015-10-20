import sys
from PyQt5 import QtPrintSupport
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QGridLayout, QLabel, QLineEdit
from PyQt5.QtWidgets import QTextEdit, QMenuBar,QWidget, QDialog, QApplication,QFileSystemModel,QMainWindow
#from  PyQt5.QtWidgets.QMainWindow import QMainWindow

from PyQt5.QtWidgets import QApplication, QFileSystemModel, QTreeView

import mainwindow
from mainwindow import *
from temporalpthreshsourcettest1006 import *
#import MRAT_ttestPTH

class MainWindow(QMainWindow, mainwindow.Ui_MainWindow): #mainwindow.Ui_MainWindow


    def __init__(self,  parent=None):

        _instance = None
        _initialized = False

        super(MainWindow,self).__init__(parent)
        self.setupUi(self)
        self.show()



if __name__ == '__main__':

    app = QApplication(sys.argv)

    form = MainWindow()

    #form.show()

    #app.exec_()



    sys.exit(app.exec_())

