__author__ = 'esmab'

from PyQt5 import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QWidget, QProgressBar,QFileDialog,
    QPushButton, QApplication)
from PyQt5.QtWidgets import *
#(QWidget, QLabel, QLineEdit, QApplication)

from PyQt5.QtCore import QBasicTimer
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtCore import *
import sys

def main():
    app 	= QApplication(sys.argv)
    edit 	= QLineEdit()
    strList 	= str("Germany;Russia;France;Norway").split(";")
    completer 	= QCompleter(strList,edit)

    edit.setWindowTitle("PyQT QLineEdit Auto Complete")
    edit.setCompleter(completer)
    edit.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()