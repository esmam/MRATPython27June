import sys
import mainwindow
import random
import numpy as np
import matplotlib
matplotlib.use("Qt5Agg")
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget
from numpy import arange, sin, pi
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches
#import Ui_MainWindow from mainwindow
from mainwindow import *


class MyMplCanvas(FigureCanvas):
    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""
    def __init__(self, parent=None, width=7, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        #self.axes = fig.add_subplot(111)
        #self.axes = plt.subplots(1,1, sharex=True)(111)
        # We want the axes cleared every time plot() is called
        #self.axes.hold(False)

        #self.axes.hold(False)

        #self.compute_initial_figure()

        #
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)


    def compute_initial_figure(self):
        pass

class MyStaticMplCanvas(MyMplCanvas):
    """Simple canvas with a sine plot."""

    #fig, (ax1) = plt.subplots(1,1, sharex=True)
    #axes = plt.subplots(1,1, sharex=True)
    def update(self,x,y,y1):
        t = arange(-700, 400,600)
        s  = np.array([[-1, 2, 3,9],[4, 5, 6,10]], np.int32)

        s1  = np.array([[-1, 2, 3,9],[4, 5, 6,10]], np.int32)
        s1  = np.array([y,y1], np.float32)

        self.axes.plot(x,y,'r',alpha=1.00,linewidth=2)
        self.axes.hold(True)
        self.axes.plot(x,y1,color='blue', alpha=1.00,linewidth=2)
        #self.axes.fill_between(x, y, y1, where=y>=y1, facecolor='green', interpolate=True)
        self.axes.set_ylabel('value')
        self.axes.set_xlabel('Time in (s)')

    def compute_initial_figure1(self,start,end,step,y,y1, cond1name,cond2name):
        self.plt = plt
        t = arange(-700, 400,600)
        s  = np.array([[-1, 2, 3,9],[4, 5, 6,10]], np.int32)
        x = arange(start-.001,end,step)
        s1  = np.array([[-1, 2, 3,9],[4, 5, 6,10]], np.int32)
        s1  = np.array([y,y1], np.float32)

        #l1 = self.axes.plot(x,y,'r',alpha=1.00,linewidth=2)
        #self.axes.hold(True)
        #l2 = self.axes.plot(x,y1,color='blue', alpha=1.00,linewidth=2)

        l3, = self.plt.plot(x,y,'r',alpha=1.00,linewidth=2)
        plt.hold(True)
        l4, = self.plt.plot(x,y1,color='blue', alpha=1.00,linewidth=2)

        #self.axes.legend((l1, l2), ('Line', 'Line', 'center'))
        #self.plt.legend(handles = [l3], loc = 1) #) #, ('Line', 'Line', 'center'))
        #self.plt.legend(handles = [l4], loc = 2) #)
        self.plt.legend((l3, l4), (cond1name, cond2name))
        #(handles=[line2], loc=4)
        #self.axes.fill_between(x, y, y1, where=y>=y1, facecolor='green', interpolate=True)
        #self.axes.set_ylabel('nAm')
        #self.axes.set_xlabel('Time in (ms)')
        self.plt.title("Analysis results for region:")
        self.plt.ylabel('nAm')
        self.plt.xlabel('Time in (ms)')
        #self.resize((20,10))

        self.plt.show()



        #self.axes.legend((l1, l2), ('Line', 'Line', 'center'))

        '''x = np.array([1,2])
        data = np.array([10,8])
        err = np.array([2,1])

        b1 = self.axes.bar(x-.2,2*err,0.4,color='b',bottom=data - err,alpha=0.3)
        self.axes.legend([(l1,l2)], ['nice legend graphic'],shadow=True,fancybox=True,numpoints=1)
        #self.axes.axis([0,3,0,15])'''



    def compute_initial_figure(self):
        t = arange(-700, 400,600)
        s  = np.array([[-1, 2, 3,9],[4, 5, 6,10]], np.int32)

        #self.axes.plot(t,s)


class MyDynamicMplCanvas(MyMplCanvas):
    """A canvas that updates itself every second with a new plot."""
    def __init__(self, *args, **kwargs):
        MyMplCanvas.__init__(self, *args, **kwargs)
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.update_figure)
        timer.start(1000)

    def compute_initial_figure(self):
        self.axes.plot([0, 1, 2, 3], [1, 2, 0, 4], 'r')

    def update_figure(self):
        # Build a list of 4 random integers between 0 and 10 (both inclusive)
        l = [random.randint(0, 10) for i in range(4)]

        self.axes.plot([0, 1, 2, 3], l, 'r')
        self.draw()

class ApplicationWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowTitle("application main window")

        self.file_menu = QMenu('&File', self)
        self.file_menu.addAction('&Quit', self.fileQuit,
                QtCore.Qt.CTRL + QtCore.Qt.Key_Q)
        self.menuBar().addMenu(self.file_menu)

        self.help_menu = QMenu('&Help', self)
        self.menuBar().addSeparator()
        self.menuBar().addMenu(self.help_menu)

        self.help_menu.addAction('&About', self.about)

        self.main_widget = QWidget(self)

        l = QVBoxLayout(self.main_widget)
        sc = MyStaticMplCanvas(self.main_widget, width=1, height=1, dpi=50)
        #dc = MyDynamicMplCanvas(self.main_widget, width=5, height=4, dpi=100)
        l.addWidget(sc)
        #l.addWidget(dc)

        self.main_widget.setFocus()
        self.setCentralWidget(self.main_widget)

        self.statusBar().showMessage("All hail matplotlib!", 2000)

    def fileQuit(self):
        self.close()

    def closeEvent(self, ce):
        self.fileQuit()

    def about(self):
        QMessageBox.about(self, "About",
  """embedding_in_qt5.py example
  Copyright 2015 BoxControL

  This program is a simple example of a Qt5 application embedding matplotlib
  canvases. It is base on example from matplolib documentation, and initially was
  developed from Florent Rougon and Darren Dale.

  http://matplotlib.org/examples/user_interfaces/embedding_in_qt4.html

  It may be used and modified with no restriction; raw copies as well as
  modified versions may be distributed without limitation."""
  )

if __name__ == '__main__':
    app = QApplication(sys.argv)

    aw = ApplicationWindow()
    aw.setWindowTitle("PyQt5 Matplot Example")
    #aw.show()
    #sys.exit(qApp.exec_())
    app.exec_()