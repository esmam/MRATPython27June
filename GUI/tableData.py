#!/usr/bin/python
import sys
from PyQt5 import Qt

from PyQt5.Qt import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication,QTableWidget,QTableWidgetItem,QItemDelegate, QColorDialog

class MyTable(QTableWidget):
    def __init__(self,  *args):
        QTableWidget.__init__(self, *args)
        self.setmydata()
        self.itemSelectionChanged.connect(self.slot)
        self.setItemDelegate(delegate(self))
        
    def slot(self):
        self.viewport().update()
        
    def setmydata(self):
        for row in range(0,16):
            for col in range(0,4):
                newitem = QTableWidgetItem(str("row %1, col %2")) #,row+1,col+1))
                if row == 0 and col == 0:
                    newitem.setText("click me")
                self.setItem(row, col, newitem)

class delegate(QItemDelegate):                
    def __init__(self,parent):
        super(delegate,self).__init__(parent)
        self.selectionmodel = parent.selectionModel()
        
    def paint(self,painter,option,index):
        if index == index.model().index(12,3) or index == index.model().index(13,1): 
        #if index.row() == 12 and index.column() == 3:
            if self.selectionmodel.isSelected(index.sibling(0,0)):
                painter.fillRect(option.rect,QColor(68, 171, 230))
        painter.drawText(option.rect, Qt.AlignCenter, index.data().toString())

def main(args):
    app = QApplication(args)
    table = MyTable(16, 4)
    table.resize(500,600)
    table.show()
    sys.exit(app.exec_())
    
if __name__=="__main__":
    main(sys.argv)