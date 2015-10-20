__author__ = 'esmab'
import sys
from PyQt5.QtCore import *
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PThresholdTemporalSourceTTest import *
from PlotWithShading import MyStaticMplCanvas
import numpy as np
from numpy import arange


data = {'col1':['1','2','3'], 'col2':['4','5','6'], 'col3':['7','8','9']}
class MyTable(QTableWidget):
    def __init__(self, sc, data, *args):
        QTableWidget.__init__(self,*args)
        self.data = data
        self.setmydata()

        #start = self.data['3 Start time']

        self.MyStaticMplCanvas1 = sc
        #self.itemSelectionChanged.connect(self.slot)
        #self.setItemDelegate(delegate(self))



        #self.resizeColumnsToContents()
        #self.resizeRowsToContents()
        self.itemSelectionChanged.connect(self.print_row)


        #self.itemSelectionChanged.connect(self.slot)
        #self.setItemDelegate(delegate(self))

    def print_row(self):
        items = self.selectedItems()


        x = arange(self.MyStaticMplCanvas1.start-.001,self.MyStaticMplCanvas1.end,self.MyStaticMplCanvas1.step)

        if items:
            #self.MyStaticMplCanvas1.update(x, self.MyStaticMplCanvas1.cond1, self.MyStaticMplCanvas1.cond2)
            #self.MyStaticMplCanvas1
            start = self.data['3 Start time']
            start1 = int(start[int(str(items[0].text()))-1])#/1000 #self.data[items(0)]
            end = self.data['4 End Time']
            end1 = int(end[int(str(items[0].text()))-1])#/1000
            rangeVal = arange(start1, end1,0.001)

            self.MyStaticMplCanvas1.plt.fill_between(x, self.MyStaticMplCanvas1.cond1, self.MyStaticMplCanvas1.cond2, edgecolor='white', facecolor='white', interpolate=True)

            #self.MyStaticMplCanvas1.axes.fill_between(x, self.MyStaticMplCanvas1.cond1, self.MyStaticMplCanvas1.cond2, where=  x>=start1 ,facecolor='green', interpolate=True)
            self.MyStaticMplCanvas1.plt.fill_between(x, self.MyStaticMplCanvas1.cond1, self.MyStaticMplCanvas1.cond2 , edgecolor='white',where= np.logical_and(start1<=x , x<=end1),facecolor='grey', interpolate=True)
            #self.MyStaticMplCanvas1.axes.fill_between(x, self.MyStaticMplCanvas1.cond1, self.MyStaticMplCanvas1.cond2 ,where= end1>=x,facecolor='grey', interpolate=True)
            self.MyStaticMplCanvas1.plt.draw()


            print(str(items[0].text()))

    def slot(self):
        self.viewport().update()

    def setmydata(self):

        horHeaders = []
        for n, key in enumerate(sorted(self.data.keys())):
            horHeaders.append(key)
            for m, item in enumerate(self.data[key]):
                newitem = QTableWidgetItem(item)
                self.setItem(m, n, newitem)
        self.setHorizontalHeaderLabels(horHeaders)
    def mouseReleaseEvent(self, event):
        if event == QtCore.Qt.LeftButton: #Release event only if done with left button, you can remove if necessary

            #Your code should go here
            indexSelection = []
            print('test')
            test = self.selectedIndexes()
            for item in self.selectedIndexes():
                indexSelection.append( str(item.row())+ "-" + str(item.column()) )
            return indexSelection

    '''def eventFilter(self, widget, event):
        if widget is self.viewport():
            index = self._last_index
            if event.type() == QtCore.QEvent.MouseButtonPress:
                index = self.indexAt(event.pos())
                print('test')
            elif event.type() == QtCore.QEvent.Leave:
                index = QtCore.QModelIndex()
            if index != self._last_index:
                row = self._last_index.row()
                column = self._last_index.column()
                item = self.item(row, column)
                if item is not None:
                    self.itemExited.emit(item)
                self.cellExited.emit(row, column)
                self._last_index = QtCore.QPersistentModelIndex(index)
    '''

    def slot(self):
        self.viewport().update()


class delegate(QItemDelegate):
    def __init__(self,parent):
        super(delegate,self).__init__(parent)
        self.selectionmodel = parent.selectionModel()

    #def paint(self,painter,option,index):


     #   if self.selectionmodel.isSelected(index.sibling(0,0)):
     #       print('test')
    def eventFilter(self, widget, index, event):

        if self.selectionmodel.isSelected(index.sibling(0,0)):
           print('test')

#def main(args):
#    app = QApplication(args)
#    table = MyTable(data, 5, 3)
#    table.show()
#    sys.exit(app.exec_())

#if __name__=="__main__":
#    main(sys.argv)