# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'temporalpthreshsourcettest1006.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
# Implementation of t-test window form
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
#import _thread
from PyQt5.QtWidgets import (QWidget, QProgressBar,QFileDialog,
    QPushButton, QApplication)
from PyQt5.QtCore import QBasicTimer
from PyQt5.QtCore import QObject, pyqtSignal
import random
import numpy as np
import matplotlib
matplotlib.use("Qt5Agg")
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget
from numpy import arange, sin, pi
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PlotWithShading import *
from PyQt5 import QtCore, QtGui, QtWidgets


from TestTabel import *
from mainwindow import *
#from mainwindow import Ui_MainWindow as m1
#from MRAT_MainWindow import MainWindow
#from MRAT_MainWindow import MainWindow as m1
#from MRAT_MainWindow import MainWindow



from PThresholdTemporalSourceTTest import PThresholdTempSourceTTest

class Ui_Form(object):


    def setupUi(self,Form):
        Form.setObjectName("Form")
        Form.resize(730, 491)
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 160, 331, 221))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.ROI = QtWidgets.QLineEdit(self.layoutWidget)
        self.ROI.setAutoFillBackground(True)
        ROIListCompleter =  ['leftba1-3','leftba4','leftba5','leftba6','leftba7','leftba8','leftba9','leftba10','leftba11','leftba17','leftba18','leftba19','leftba20'
        ,'leftba21','leftba22','leftba28','leftba36','leftba37','leftba38','leftba39','leftba40','leftba42','leftba44-45','leftba46'
        'leftba47','leftcerebellartonsil','rightba1-3','rightba4','rightba5','rightba6','rightba7','rightba8','rightba9','rightba10','rightba11'
        ,'rightba17','rightba18','rightba19','rightba20','rightba21','rightba22','rightba28','rightba36','rightba37','rightba38','rightba39'
        'rightba40','rightba42','rightba44-45','rightba46','rightba47','rightcerebellartonsil']

        self.completerRoi 	= QCompleter(ROIListCompleter,self.ROI)
        self.ROI.setCompleter(self.completerRoi)

        self.ROI.setObjectName("ROI")
        self.gridLayout_2.addWidget(self.ROI, 5, 1, 1, 1)
        self.ROILabel = QtWidgets.QLabel(self.layoutWidget)
        self.ROILabel.setObjectName("ROILabel")
        self.gridLayout_2.addWidget(self.ROILabel, 5, 0, 1, 1)
        self.MinimumTempLabel = QtWidgets.QLabel(self.layoutWidget)
        self.MinimumTempLabel.setObjectName("MinimumTempLabel")
        self.gridLayout_2.addWidget(self.MinimumTempLabel, 4, 0, 1, 1)
        self.tailComboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.tailComboBox.setObjectName("tailComboBox")
        self.tailComboBox.addItem("")
        self.tailComboBox.addItem("")
        self.tailComboBox.addItem("")
        self.tailComboBox.addItem("")
        self.gridLayout_2.addWidget(self.tailComboBox, 6, 1, 1, 1)
        self.MinTempCluster = QtWidgets.QLineEdit(self.layoutWidget)
        self.MinTempCluster.setObjectName("MinTempCluster")
        self.gridLayout_2.addWidget(self.MinTempCluster, 4, 1, 1, 1)
        self.Condition1 = QtWidgets.QLineEdit(self.layoutWidget)
        self.Condition1.setAutoFillBackground(True)
        self.Condition1.setObjectName("Condition1")
        self.gridLayout_2.addWidget(self.Condition1, 0, 1, 1, 1)
        self.TailLabel = QtWidgets.QLabel(self.layoutWidget)
        self.TailLabel.setObjectName("TailLabel")
        self.gridLayout_2.addWidget(self.TailLabel, 6, 0, 1, 1)
        self.Condition1Label = QtWidgets.QLabel(self.layoutWidget)
        self.Condition1Label.setObjectName("Condition1Label")
        self.gridLayout_2.addWidget(self.Condition1Label, 0, 0, 1, 1)
        #self.Prestimulus = QtWidgets.QLineEdit(self.layoutWidget)
        #self.Prestimulus.setObjectName("Prestimulus")
        #self.gridLayout_2.addWidget(self.Prestimulus, 3, 1, 1, 1)
        #self.PrestimLabel = QtWidgets.QLabel(self.layoutWidget)
        #self.PrestimLabel.setObjectName("PrestimLabel")
        self.Prestimulus = 0
        #self.gridLayout_2.addWidget(self.PrestimLabel, 3, 0, 1, 1)
        self.StartTime = QtWidgets.QLineEdit(self.layoutWidget)
        self.StartTime.setMaxLength(1000)
        self.StartTime.setObjectName("StartTime")
        self.gridLayout_2.addWidget(self.StartTime, 2, 1, 1, 1)
        self.FindROI = QtWidgets.QPushButton(self.layoutWidget)
        self.FindROI.setObjectName("FindROI")
        self.gridLayout_2.addWidget(self.FindROI, 5, 2, 1, 1)
        self.StartTimelabel = QtWidgets.QLabel(self.layoutWidget)
        self.StartTimelabel.setObjectName("StartTimelabel")
        self.gridLayout_2.addWidget(self.StartTimelabel, 2, 0, 1, 1)
        self.BadSubjects = QtWidgets.QLineEdit(self.layoutWidget)
        self.BadSubjects.setAutoFillBackground(False)
        self.BadSubjects.setObjectName("BadSubjects")
        self.gridLayout_2.addWidget(self.BadSubjects, 1, 1, 1, 1)
        self.BadSubjectsLabel = QtWidgets.QLabel(self.layoutWidget)
        self.BadSubjectsLabel.setObjectName("BadSubjectsLabel")
        self.gridLayout_2.addWidget(self.BadSubjectsLabel, 1, 0, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(Form)
        self.layoutWidget1.setGeometry(QtCore.QRect(340, 160, 292, 151))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.PthreshVal = QtWidgets.QLineEdit(self.layoutWidget1)
        self.PthreshVal.setObjectName("PthreshVal")
        self.gridLayout_3.addWidget(self.PthreshVal, 2, 1, 1, 1)
        self.EndTimeLabel = QtWidgets.QLabel(self.layoutWidget1)
        self.EndTimeLabel.setObjectName("EndTimeLabel")
        self.gridLayout_3.addWidget(self.EndTimeLabel, 1, 0, 1, 1)
        self.Condition2 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.Condition2.setObjectName("Condition2")
        self.gridLayout_3.addWidget(self.Condition2, 0, 1, 1, 1)
        self.Condition2Label = QtWidgets.QLabel(self.layoutWidget1)
        self.Condition2Label.setObjectName("Condition2Label")
        self.gridLayout_3.addWidget(self.Condition2Label, 0, 0, 1, 1)
        #self.MAXFDR = QtWidgets.QLineEdit(self.layoutWidget1)
        #self.MAXFDR.setObjectName("MAXFDR")
        #self.gridLayout_3.addWidget(self.MAXFDR, 3, 1, 1, 1)
        self.MAXFDR = 0
        self.PtreshLabel = QtWidgets.QLabel(self.layoutWidget1)
        self.PtreshLabel.setObjectName("PtreshLabel")
        self.gridLayout_3.addWidget(self.PtreshLabel, 2, 0, 1, 1)
        self.NumberPermutaiton = QtWidgets.QLineEdit(self.layoutWidget1)
        self.NumberPermutaiton.setObjectName("NumberPermutaiton")
        self.gridLayout_3.addWidget(self.NumberPermutaiton, 4, 1, 1, 1)
        #self.MAxFDRLabel = QtWidgets.QLabel(self.layoutWidget1)
        #self.MAxFDRLabel.setObjectName("MAxFDRLabel")
        #self.gridLayout_3.addWidget(self.MAxFDRLabel, 3, 0, 1, 1)
        self.NumberPermLabel = QtWidgets.QLabel(self.layoutWidget1)
        self.NumberPermLabel.setObjectName("NumberPermLabel")
        self.gridLayout_3.addWidget(self.NumberPermLabel, 4, 0, 1, 1)
        self.EndTime = QtWidgets.QLineEdit(self.layoutWidget1)
        self.EndTime.setObjectName("EndTime")
        self.EndTime.setMaxLength(1000)
        self.gridLayout_3.addWidget(self.EndTime, 1, 1, 1, 1)
        self.layoutWidget2 = QtWidgets.QWidget(Form)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 80, 271, 62))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.layoutWidget2)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.ProjecTRoot = QtWidgets.QLineEdit(self.layoutWidget2)
        self.ProjecTRoot.setObjectName("ProjecTRoot")
        self.gridLayout.addWidget(self.ProjecTRoot, 0, 0, 1, 1)
        self.FindpushButton = QtWidgets.QPushButton(self.layoutWidget2)
        self.FindpushButton.setObjectName("FindpushButton")
        self.gridLayout.addWidget(self.FindpushButton, 0, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout, 0, 1, 1, 1)
        self.ProjectRoot = QtWidgets.QLabel(self.layoutWidget2)
        self.ProjectRoot.setObjectName("ProjectRoot")
        self.gridLayout_4.addWidget(self.ProjectRoot, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 0, 481, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.cancel = QtWidgets.QPushButton(Form)
        self.cancel.setGeometry(QtCore.QRect(330, 380, 169, 32))
        self.cancel.setObjectName("cancel")
        self.Ok = QtWidgets.QPushButton(Form)
        self.Ok.setGeometry(QtCore.QRect(500, 380, 126, 32))
        self.Ok.setObjectName("Ok")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(10, 140, 261, 23))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.BadSubjectsLabel.raise_()
        self.BadSubjects.raise_()
        self.BadSubjects.raise_()
        self.ProjectRoot.raise_()
        self.label.raise_()
        self.cancel.raise_()
        self.Ok.raise_()
        self.progress = QProgressBar(self)
        self.progress.setGeometry(250, 420, 326, 102)
        self.table = QTableWidget()


        #self.progress.isVisible = "False"

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.cancel.clicked.connect(self.close)

        Rootdirectory = self.FindpushButton.clicked.connect(self.FindFolder)
        RoiFile = self.FindROI.clicked.connect(self.fileOpenROI)

        #GET Dictionary for autocompletion of condition names
        self.Ok.clicked.connect(self.RunAnalysis)



        Form.setTabOrder(self.ProjecTRoot, self.FindpushButton)
        Form.setTabOrder(self.FindpushButton,self.Condition1)
        Form.setTabOrder(self.Condition1, self.Condition2)
        Form.setTabOrder(self.Condition2, self.BadSubjects)
        Form.setTabOrder(self.BadSubjects, self.StartTime)
        Form.setTabOrder(self.StartTime, self.EndTime)
        #Form.setTabOrder(self.EndTime, self.Prestimulus)
        #Form.setTabOrder(self.Prestimulus, self.PthreshVal)
        Form.setTabOrder(self.EndTime, self.PthreshVal)
        Form.setTabOrder(self.PthreshVal, self.MinTempCluster)
        #Form.setTabOrder(self.MinTempCluster, self.MAXFDR)
        #Form.setTabOrder(self.MAXFDR, self.ROI)
        Form.setTabOrder(self.MinTempCluster, self.ROI)
        Form.setTabOrder(self.ROI, self.NumberPermutaiton)
        Form.setTabOrder(self.NumberPermutaiton, self.ROI)
        Form.setTabOrder(self.ROI, self.tailComboBox)
        Form.setTabOrder(self.tailComboBox, self.NumberPermutaiton)


    def fileOpenROI(self):
        fn, _ = QFileDialog.getOpenFileName(self, "Open File...", None,
                "label-Files (*.txt *.label);;All Files (*)")

        self.ROI.setText(fn)

    def FindFolder(self):

        self.directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Find Files",
        QtCore.QDir.currentPath())


        self.ProjecTRoot.setText(self.directory)

        strList = []
        for root, dirs, files in os.walk(self.directory):
            strList.append(dirs)


        strList1	= str("Germany;Russia;France;Norway").split(";")
        self.completer 	= QCompleter(strList[0],self.Condition1)



        self.Condition1.setCompleter(self.completer)
        self.Condition2.setCompleter(self.completer)


        return self.directory, self.completer
    ##### get all data entered in the form and pass it to the ttest function
    def RunAnalysis(self):
        condition1Name = self.Condition1.text()

        condition2Name = self.Condition2.text()
        startTime = self.StartTime.text()
        endTime = self.EndTime.text()
        #presTim = self.Prestimulus.text()
        presTim = self.Prestimulus
        PThresh = self.PthreshVal.text()
        minTemporalCluster = self.MinTempCluster.text()
        #maxFDR = self.MAXFDR.text()
        maxFDR = self.MAXFDR
        numPerm = self.NumberPermutaiton.text()
        anlsysTail = self.tailComboBox.currentData()
        ROI = self.ROI.text()
        root = self.ProjecTRoot.text()

        self.progress.isVisible = "True"
        self.progress.isTextVisible = "True"
        self.progress.format = "%p%"



        self.completed = 0
        self.Results = ""
        while self.completed < 100:

            self.completed += 0.10
            self.progress.setValue(self.completed)

            self.progress.value = self.completed
            self.progress.isTextVisible = "True"

        #pass setting from UI to statistical function
        #QObject.connectNotify(self.progressBar, pyqtSignal(""), self.progressBar.setValue)
        self.Results = PThresholdTempSourceTTest(root, condition1Name, condition2Name,startTime,endTime, presTim,PThresh,minTemporalCluster, numPerm, anlsysTail, ROI)
        resultsAll = self.Results


        #get conditions names


        cluster_table = self.Results.clusters.as_table()

        resultsForPlot = self.Results._default_plot_obj

        Cond1 = resultsForPlot[0]
        Cond1Name = Cond1.name
        Cond2 = resultsForPlot[1]
        Cond2Name = Cond2.name

        cond1Data = Cond1.x
        cond2Data = Cond2.x
        XAxisVals = Cond1.dims # X AXIS Y AXIS THEN PLOT
        Startx = XAxisVals[0]
        startx = (Startx.tmin)*1000
        endx = (Startx.tmax)*1000
        stepx = (Startx.tstep)*1000
        name = Startx.name
        nsamples = Startx.nsamples

        from PyQt5 import QtCore, QtGui, QtWidgets
        from mainwindow import Ui_MainWindow

        self.Results = self.Results.clusters

        #self.main_widget = QWidget(mainwindow.Ui_MainWindow.dockPlot())
        self.main_widget = QtWidgets.QDockWidget()
        #self.main_widget = QtWidgets.QWidget()


        l = QVBoxLayout(self.main_widget)
        self.sc = MyStaticMplCanvas(self.main_widget, width=5, height=4, dpi=100)
        #dc = MyDynamicMplCanvas(self.main_widget, width=5, height=4, dpi=100)
        #MyStaticMplCanvas.compute_initial_figure(self.main_widget)
        MyStaticMplCanvas.compute_initial_figure1(self.sc,startx,endx,stepx,cond1Data,cond2Data, condition1Name,condition2Name)
        l.addWidget(self.sc)



        #PLotWidget = QWidget()
        #PLotWidget = l.widget()

        #DockPlot = QDockWidget.create
        #Ui_MainWindow.dockPlot
        #Ui_MainWindow
        #Ui_MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), l)

        #self.main_widget.show()


        self.sc.cond1 = cond1Data
        self.sc.cond2 = cond2Data
        self.sc.start = startx
        self.sc.end = endx
        self.sc.step = stepx



        #Extract epoch time for x axis for each condition

        #Extract y axis values
        #print(self.Results.clusters)
        #x = self.Results.clusters[1, 'cluster'].x
        #d = self.Results.clusters[0, 'cluster'].any()
        #data = {'ClusterID':['1','2','3'], 'n_sources':['4','5','6'], 'hemisphere':['7','8','9'],'Start Time':['7','8','9'],'End Time':['7','8','9'],'Duration':['7','8','9'],'P-value':['7','8','9']}
        durations = []
        ids=[]
        ps=[]
        sigs=[]
        tstarts=[]
        tstops=[]
        cluster = self.Results.get('cluster')
        #len = self.Results._len_
        duration = self.Results.get('duration')
        for _len_ in duration:

            durations.append(str(int(_len_*1000)))

        index = 1
        id = self.Results.get('id')
        for _len_ in id:
            #ids.append(str(_len_))
            ids.append(str(index))
            index = index +1


        p = self.Results.get('p')
        for _len_ in p:
            ps.append(str(_len_))

        sig = self.Results.get('sig')
        for _len_ in sig:
            sigs.append(str(_len_))

        tstart = self.Results.get('tstart')
        for _len_ in tstart:
            tstarts.append(str(int(_len_*1000)))

        tstop = self.Results.get('tstop')
        for _len_ in tstop:
            tstops.append(str(int(_len_*1000)))

        v = self.Results.get('v')
        #get header

        data = {'1 ClusterID':ids, '2 Duration':durations, '3 Start time':tstarts,'4 End Time':tstops, '5 P-value': ps,'6 Sig':sigs} #,'Duration':['7','8','9'],'P-value':['7','8','9']}


        self.table = MyTable(self.sc,data, len(durations),6)#,startx,endx,stepx,cond1Data,cond2Data)
        #l.addWidget(self.sc)


        #from mainwindow import Ui_MainWindow as mainwind
        from MRAT_MainWindow import MainWindow as mainwind


        #Ui_MainWindow.__init__(self)
        #self.setupUi(self)
        m = mainwind()

        #m.dockResults.setWidget(m.Resultcontent)
        #m = mainwind()
        m.Resultcontent = self.table
        m.Resultcontent = self.table
        m.dockResults.setWidget(m.Resultcontent)

        '''l1 = QVBoxLayout(m.dock)
        self.sc1 = MyStaticMplCanvas(m.dock, width=5, height=4, dpi=100)
        #dc = MyDynamicMplCanvas(self.main_widget, width=5, height=4, dpi=100)
        #MyStaticMplCanvas.compute_initial_figure(self.main_widget)
        MyStaticMplCanvas.compute_initial_figure1(self.sc1,startx,endx,stepx,cond1Data,cond2Data, condition1Name,condition2Name)
        l1.addWidget(self.sc1)
        m.dock.show()'''


        m.Plotcontent = l
        #m.dock.set
        m.dock.setWidget(m.Plotcontent)
        #m.dock.show()
        m.addDockWidget(Qt.RightDockWidgetArea, m.dockResults)
        m.addAction(m.dockResults.toggleViewAction())


        #####

        #m.dockw = QtWidgets.QDockWidget()
        #self.main_widget = QtWidgets.QWidget()


        '''l = QVBoxLayout(m.dock)
        self.sc = MyStaticMplCanvas(m.dock, width=5, height=4, dpi=100)
        #dc = MyDynamicMplCanvas(self.main_widget, width=5, height=4, dpi=100)
        #MyStaticMplCanvas.compute_initial_figure(self.main_widget)
        MyStaticMplCanvas.compute_initial_figure1(self.sc,startx,endx,stepx,cond1Data,cond2Data, condition1Name,condition2Name)
        l.addWidget(self.sc)
        m.addDockWidget(Qt.RightDockWidgetArea, m.dock)
        m.addAction(m.dockw.toggleViewAction())'''

        ########


        ########
        #m.update()
        #m.close()
        m.show()


        '''MainWindow.dockResults = mainwind.dockResults()
        mainwind1.ResultsContent = self.table
        mainwind1.dockResults = QtWidgets.QDockWidget()
        mainwind1.dockResults.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)


        #mainwind.tableMain = self.table
        #mainwind.dockResults.setWidget(self.table)
        #mainwind.retranslateUi()

        #self.table.show()
        #self.table.setMouseTracking(True)
        #self.table.itemClicked()'''





    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Permutation Test For a Temporal t-test analysis"))
        Form.setToolTip(_translate("Form", "PThreshold T-test for Temporal Data"))
        self.ROI.setToolTip(_translate("Form", "Please enter the prestimulus interval"))
        self.ROILabel.setText(_translate("Form", "ROI"))
        self.MinimumTempLabel.setText(_translate("Form", "Minimum Temporal Cluster"))
        self.tailComboBox.setItemText(0, _translate("Form", "Please choose an option"))
        self.tailComboBox.setItemText(1, _translate("Form", "Both"))
        self.tailComboBox.setItemText(2, _translate("Form", "Left tail"))
        self.tailComboBox.setItemText(3, _translate("Form", "Right Tail"))
        self.MinTempCluster.setToolTip(_translate("Form", "Please enter the minimum temporal cluster duration in ms"))
        self.Condition1.setToolTip(_translate("Form", "Please enter the first condition's name just enter the first letters"))



        self.TailLabel.setText(_translate("Form", "Tail"))
        self.Condition1Label.setText(_translate("Form", "Condition 1 :"))
        #self.Prestimulus.setToolTip(_translate("Form", "Please enter the prestimulus interval in ms"))
        #self.PrestimLabel.setText(_translate("Form", "Prestimulus"))
        self.StartTime.setToolTip(_translate("Form", "Enter the start time in ms"))
        #self.StartTime.setInputMask(_translate("Form", "0"))
        self.FindROI.setText(_translate("Form", "find"))
        self.StartTimelabel.setText(_translate("Form", "Start Time:"))
        self.BadSubjects.setToolTip(_translate("Form", "Please enter the badsubjects names separated by , "))
        self.BadSubjectsLabel.setText(_translate("Form", "BadSubjects"))
        self.PthreshVal.setToolTip(_translate("Form", "Please Enter the PThreshold value"))
        self.EndTimeLabel.setText(_translate("Form", "End Time"))
        self.Condition2.setToolTip(_translate("Form", "Please enter the second condition's name"))
        self.Condition2Label.setText(_translate("Form", "Condition 2:"))
        #self.MAXFDR.setToolTip(_translate("Form", "Please enter the prestimulus interval"))
        self.PtreshLabel.setText(_translate("Form", "P_value threshold"))
        self.NumberPermutaiton.setToolTip(_translate("Form", "Please enter the number of permutation"))
        #self.MAxFDRLabel.setText(_translate("Form", "Max FDR Rate"))
        self.NumberPermLabel.setText(_translate("Form", "Number Of Permutations"))
        self.EndTime.setToolTip(_translate("Form", "enter the ending time "))
        self.FindpushButton.setText(_translate("Form", "find"))
        self.ProjectRoot.setText(_translate("Form", "Conditions Root :"))
        self.label.setText(_translate("Form", "Temporal t-test analysis for sources data "))
        self.cancel.setText(_translate("Form", "Cancel"))
        self.Ok.setText(_translate("Form", "Run Analysis"))

    def getResults(self):

        return self.table



