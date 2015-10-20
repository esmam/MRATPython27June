# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindowUSEONLYSOMELINES.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from MRAT_ttestPTH import ttestwindow
from MRAT_ANOVAPTH import ANOVAwindow
from temporalpthreshsourcettest1006 import *
from temporalANOVAsource import *
from PThresholdTemporalSourceTTest import *
from TestTabel import *
from PyQt5.QtGui import QIcon, QKeySequence
#from temporalpthreshsourcettest1006 import Ui_Form
from PlotWithShading import MyStaticMplCanvas
from PyQt5 import QtGui


class Ui_MainWindow(object):



    def setupUi(self, MainWindow):

        _instance = None
        _initialized = False
        MainWindow.setObjectName("mainwindow")
        MainWindow.resize(600, 1200)

        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.MRATcentralwidget = QtWidgets.QWidget(MainWindow)
        self.MRATcentralwidget.setObjectName("MRATcentralwidget")
        MainWindow.setCentralWidget(self.MRATcentralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 570, 22))
        self.menubar.setMinimumSize(QtCore.QSize(10, 10))
        self.menubar.setDefaultUp(False)
        self.menubar.setNativeMenuBar(False)
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuData = QtWidgets.QMenu(self.menubar)
        self.menuData.setObjectName("menuData")
        self.menuGraphics = QtWidgets.QMenu(self.menubar)
        self.menuGraphics.setObjectName("menuGraphics")
        self.menuStatistics = QtWidgets.QMenu(self.menubar)
        self.menuStatistics.setObjectName("menuStatistics")
        self.menuT_TESTS = QtWidgets.QMenu(self.menuStatistics)
        self.menuT_TESTS.setObjectName("menuT_TESTS")

        self.menuTemporal = QtWidgets.QMenu(self.menuT_TESTS)
        self.menuTemporal.setObjectName("menuTemporal")

        #self.dockResults = QtWidgets.QDockWidget(MainWindow)

        self.resultsTable = QTableWidget()
        self.Plot_widget = QtWidgets.QWidget()





        self.menuANOVAs = QtWidgets.QMenu(self.menuStatistics)
        self.menuANOVAs.setObjectName("menuANOVAs")


        self.menuTemporal1 = QtWidgets.QMenu(self.menuANOVAs)
        self.menuTemporal1.setObjectName("menuTemporal")


        self.menuResults = QtWidgets.QMenu(self.menubar)
        self.menuResults.setObjectName("menuResults")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.createActions()
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        self.toolBar.addAction((self.newAct))
        self.toolBar.addAction(self.newAct)
        self.toolBar.addAction(self.openAct)
        self.toolBar.addAction(self.saveAct)



        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionSpatio_Temporal_2 = QtWidgets.QAction(MainWindow)
        self.actionSpatio_Temporal_2.setObjectName("actionSpatio_Temporal_2")
        self.actionNew_Analysis = QtWidgets.QAction(MainWindow)
        self.actionNew_Analysis.setObjectName("actionNew_Analysis")
        self.actionOpen_Analysis = QtWidgets.QAction(MainWindow)
        self.actionOpen_Analysis.setObjectName("actionOpen_Analysis")

        self.actionPTHreshold = QtWidgets.QAction(MainWindow)
        self.actionPTHreshold.setObjectName("actionPTHreshold")

        self.actionPTHresholdANOVA = QtWidgets.QAction(MainWindow)
        self.actionPTHresholdANOVA.setObjectName("actionPTHresholdANOVA")

        self.actionTFCE = QtWidgets.QAction(MainWindow)
        self.actionTFCE.setObjectName("actionTFCE")
        self.actionWindow = QtWidgets.QAction(MainWindow)
        self.actionWindow.setObjectName("actionWindow")
        self.actionImport_File = QtWidgets.QAction(MainWindow)
        self.actionImport_File.setObjectName("actionImport_File")
        self.actionExport_File = QtWidgets.QAction(MainWindow)
        self.actionExport_File.setObjectName("actionExport_File")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionFull_Brain_analysis = QtWidgets.QAction(MainWindow)
        self.actionFull_Brain_analysis.setObjectName("actionFull_Brain_analysis")
        self.actionDisplay_all = QtWidgets.QAction(MainWindow)
        self.actionDisplay_all.setObjectName("actionDisplay_all")
        self.actionExport_results = QtWidgets.QAction(MainWindow)
        self.actionExport_results.setObjectName("actionExport_results")
        self.actionDisplay_F_values = QtWidgets.QAction(MainWindow)
        self.actionDisplay_F_values.setObjectName("actionDisplay_F_values")
        self.actionDisplay_P_values = QtWidgets.QAction(MainWindow)
        self.actionDisplay_P_values.setObjectName("actionDisplay_P_values")
        self.actionEdit_plotting = QtWidgets.QAction(MainWindow)

        self.actionChooseROI = QtWidgets.QAction(MainWindow)
        self.actionChooseROI.setObjectName("actionChooseROI")
        self.actionEdit_plotting.setObjectName("actionEdit_plotting")
        self.actionEdit_Brain_model = QtWidgets.QAction(MainWindow)
        self.actionEdit_Brain_model.setObjectName("actionEdit_Brain_model")
        self.actionImport_data = QtWidgets.QAction(MainWindow)
        self.actionImport_data.setObjectName("actionImport_data")
        self.actionExport_data = QtWidgets.QAction(MainWindow)
        self.actionExport_data.setObjectName("actionExport_data")
        self.actionImport_ini_from_matlab = QtWidgets.QAction(MainWindow)
        self.actionImport_ini_from_matlab.setObjectName("actionImport_ini_from_matlab")
        self.actionMRAT_Python = QtWidgets.QAction(MainWindow)
        self.actionMRAT_Python.setObjectName("actionMRAT_Python")
        self.actionTemporal = QtWidgets.QAction(MainWindow)
        self.actionTemporal.setObjectName("actionTemporal")
        self.actionSpatio_Temporal_3 = QtWidgets.QAction(MainWindow)
        self.actionSpatio_Temporal_3.setObjectName("actionSpatio_Temporal_3")
        self.menuFile.addAction(self.actionNew_Analysis)
        self.menuFile.addAction(self.actionOpen_Analysis)
        self.menuFile.addAction(self.actionImport_File)
        self.menuFile.addAction(self.actionExport_File)
        self.menuFile.addAction(self.actionQuit)
        self.menuData.addAction(self.actionImport_data)
        self.menuData.addAction(self.actionExport_data)
        self.menuData.addAction(self.actionImport_ini_from_matlab)
        self.menuGraphics.addAction(self.actionEdit_plotting)
        self.menuGraphics.addAction(self.actionEdit_Brain_model)
        self.menuGraphics.addAction(self.actionChooseROI)
        self.menuTemporal.addSeparator()
        self.menuTemporal.addAction(self.actionPTHreshold)
        self.menuTemporal.addAction(self.actionTFCE)
        self.menuTemporal.addAction(self.actionWindow)


        self.menuTemporal1.addAction(self.actionPTHresholdANOVA)
        self.menuTemporal1.addAction(self.actionTFCE)
        self.menuTemporal1.addAction(self.actionWindow)


        self.menuT_TESTS.addSeparator()
        self.menuT_TESTS.addAction(self.menuTemporal.menuAction())
        self.menuT_TESTS.addAction(self.actionSpatio_Temporal_2)
        self.menuANOVAs.addSeparator()

        self.menuANOVAs.addAction(self.menuTemporal1.menuAction())
        self.menuANOVAs.addAction(self.actionSpatio_Temporal_2)
        self.menuANOVAs.addSeparator()






        self.menuANOVAs.addAction(self.actionTemporal)
        self.menuANOVAs.addAction(self.actionSpatio_Temporal_3)


        self.menuStatistics.addAction(self.menuANOVAs.menuAction())
        self.menuStatistics.addAction(self.menuT_TESTS.menuAction())
        self.menuStatistics.addAction(self.actionFull_Brain_analysis)
        self.menuResults.addAction(self.actionDisplay_all)
        self.menuResults.addAction(self.actionExport_results)
        self.menuResults.addAction(self.actionDisplay_F_values)
        self.menuResults.addAction(self.actionDisplay_P_values)
        self.menuAbout.addAction(self.actionMRAT_Python)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuData.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuGraphics.menuAction())
        self.menubar.addAction(self.menuStatistics.menuAction())
        self.menubar.addAction(self.menuResults.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        #add main dock window

        #self.tableMain = QTableWidget()
        #self.widget.setObjectName("widget")
        self.treeView = QtWidgets.QTreeView(MainWindow)
        self.treeView.setGeometry(QtCore.QRect(10, 20, 191, 680))
        MainWindow.DockContent = self.treeView

        self.dockWidget= QDockWidget("MRAT work space", MainWindow)
        #self.dockWidget = QDockWidget(MainWindow)
        self.dockWidget.setObjectName("dockWidget")

        self.dockWidget.setWidget(MainWindow.DockContent)
        #self.dockWidgetContents = QtWidgets.QWidget()
        #self.dockWidgetContents.setObjectName("dockWidgetContents")
        #self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget)

        self.dockWidget.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)
        #set dock widget that will hold plot widget






        ################## plot Contents
        MainWindow.Resultcontent = self.resultsTable
        self.dockResults = QDockWidget("Results Window", MainWindow)
        #self.paragraphsList = QListWidget(self.dock)
        self.addDockWidget(Qt.RightDockWidgetArea, self.dockResults)
        self.addAction(self.dockResults.toggleViewAction())
        self.dockResults.setWidget(MainWindow.Resultcontent)
        #self.dockResults.show()





        ############# REsults contents
        MainWindow.Plotcontent = self.Plot_widget
        self.dock = QtWidgets.QDockWidget('Plot Window',MainWindow)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dock)

        self.addDockWidget(Qt.RightDockWidgetArea, self.dock)
        self.addAction(self.dock.toggleViewAction())
        self.dock.setWidget(MainWindow.Plotcontent)
        ######

        #self.treeView.sizeAdjustPolicy = "AdjustToContents"

        self.treeView.setObjectName("treeView")
        self.model = QFileSystemModel()
        self.rootPath = '~/PycharmProjects/MRATPython/'
        self.model.setRootPath(self.rootPath)

        self.treeView.setModel(self.model)

        self.treeView.setAnimated(True)
        #self.treeView.sizeAdjustPolicy = 'True'
        self.treeView.setIndentation(5)
        self.treeView.setSortingEnabled(True)

        self.treeView.setWindowTitle("MRAT workspace")

        self.retranslateUi(MainWindow)
        self.actionQuit.triggered.connect(MainWindow.close)

        self.actionQuit.triggered.connect(MainWindow.close)

        from temporalpthreshsourcettest1006 import Ui_Form
        self.form1 =  ttestwindow()

        a = self.form1
        self.resultsTable = a.table
        self.formANOVA = ANOVAwindow()



        #################print result in result widget

        #self.dockResults = QDockWidget("Results Window", MainWindow)
        #self.dockResults.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)
        #MainWindow.Resultcontent = self.resultsTable
        #self.dockResults = QtWidgets.QDockWidget(MainWindow)
        #MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockResults)
        #self.addDockWidget(Qt.RightDockWidgetArea, self.dockResults)
        #self.addAction(self.dockResults.toggleViewAction())
        #self.dockResults.setWidget(MainWindow.Resultcontent)

        #self.Filedial = QtWidgets.QFileDialog.getExistingDirectory(self, "Find Files",
         #       QtCore.QDir.currentPath())
        self.actionPTHreshold.triggered.connect(self.form1.show)
        self.actionPTHresholdANOVA.triggered.connect(self.formANOVA.show)

        #self.MainWindow = MainWindow


        QtCore.QMetaObject.connectSlotsByName(MainWindow)





    def createActions(self):
        root = QFileInfo(__file__).absolutePath()

        self.newAct = QAction(QIcon(root + '/images/new.png'), "&New", self,
                shortcut="", statusTip="Create a new file",
                triggered= self.retranslateUi)

        self.openAct = QAction(QIcon(root + '/images/open.png'), "&Open...",
                self, shortcut=QKeySequence.Open,
                statusTip="Open an existing file", triggered=self.retranslateUi)

        self.saveAct = QAction(QIcon(root + '/images/save.png'), "&Save", self,
                shortcut=QKeySequence.Save,
                statusTip="Save the document to disk", triggered=self.retranslateUi)

        self.saveAsAct = QAction("Save &As...", self,
                shortcut=QKeySequence.SaveAs,
                statusTip="Save the document under a new name",
                triggered=self.retranslateUi)

        self.exitAct = QAction("E&xit", self, shortcut="Ctrl+Q",
                statusTip="Exit the application", triggered=self.retranslateUi)

        self.cutAct = QAction(QIcon(root + '/images/cut.png'), "Cu&t", self,
                shortcut=QKeySequence.Cut,
                statusTip="Cut the current selection's contents to the clipboard",
                triggered=self.retranslateUi)

        self.copyAct = QAction(QIcon(root + '/images/copy.png'), "&Copy", self,
                shortcut=QKeySequence.Copy,
                statusTip="Copy the current selection's contents to the clipboard",
                triggered=self.retranslateUi)

        self.pasteAct = QAction(QIcon(root + '/images/paste.png'), "&Paste",
                self, shortcut=QKeySequence.Paste,
                statusTip="Paste the clipboard's contents into the current selection",
                triggered=self.retranslateUi)

        self.aboutAct = QAction("&About", self,
                statusTip="Show the application's About box",
                triggered=self.retranslateUi)

        self.aboutQtAct = QAction("About &Qt", self,
                statusTip="Show the Qt library's About box",
                triggered=QApplication.instance().aboutQt)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        #self.dockResults = self.dockResults
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuData.setTitle(_translate("MainWindow", "Data"))
        self.menuGraphics.setTitle(_translate("MainWindow", "Graphics"))
        self.menuStatistics.setTitle(_translate("MainWindow", "Statistics"))
        self.menuT_TESTS.setTitle(_translate("MainWindow", "T-TESTS"))
        self.menuTemporal.setTitle(_translate("MainWindow", "Temporal"))
        self.menuTemporal1.setTitle(_translate("MainWindow", "Temporal"))
        self.menuANOVAs.setTitle(_translate("MainWindow", "ANOVAs"))
        self.menuResults.setTitle(_translate("MainWindow", "Results"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionSpatio_Temporal_2.setText(_translate("MainWindow", "Spatio-Temporal"))
        self.actionNew_Analysis.setText(_translate("MainWindow", "New Analysis"))
        self.actionOpen_Analysis.setText(_translate("MainWindow", "Open Analysis"))
        self.actionPTHresholdANOVA.setText(_translate("MainWindow", "PThreshold A"))

        self.actionPTHreshold.setText(_translate("MainWindow", "PThreshold"))

        self.actionPTHreshold.setStatusTip(_translate("MainWindow", "Run PTHRESHOLD temporal t-test analysis"))
        self.actionTFCE.setText(_translate("MainWindow", "TFCE"))
        self.actionWindow.setText(_translate("MainWindow", "window"))
        self.actionImport_File.setText(_translate("MainWindow", "Import File"))
        self.actionExport_File.setText(_translate("MainWindow", "Export File"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionFull_Brain_analysis.setText(_translate("MainWindow", "Full Brain analysis"))
        self.actionDisplay_all.setText(_translate("MainWindow", "Display all"))
        self.actionExport_results.setText(_translate("MainWindow", "Export results"))
        self.actionDisplay_F_values.setText(_translate("MainWindow", "Display F-values"))
        self.actionDisplay_P_values.setText(_translate("MainWindow", "Display P-values"))
        self.actionEdit_plotting.setText(_translate("MainWindow", "Edit plotting "))
        self.actionEdit_Brain_model.setText(_translate("MainWindow", "Edit Brain model"))
        self.actionChooseROI.setText(_translate("MainWindow", "Choose ROI on a brain model"))
        self.actionImport_data.setText(_translate("MainWindow", "import from mat"))
        self.actionExport_data.setText(_translate("MainWindow", "export data"))
        self.actionImport_ini_from_matlab.setText(_translate("MainWindow", "import ini from matlab"))
        self.actionMRAT_Python.setText(_translate("MainWindow", "MRAT-Python"))
        self.actionTemporal.setText(_translate("MainWindow", "Temporal"))
        self.actionSpatio_Temporal_3.setText(_translate("MainWindow", "Spatio_Temporal"))






