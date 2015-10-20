# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QFileSystemModel, QTreeView
from MRAT_ttestPTH import ttestwindow

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.MRATcentralwidget = QtWidgets.QWidget(MainWindow)
        self.MRATcentralwidget.setObjectName("MRATcentralwidget")
        self.widget = QtWidgets.QWidget(self.MRATcentralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 0, 201, 480))





        #tree.resize(340, 480)
        #tree.show()
        MainWindow.setCentralWidget(self.MRATcentralwidget)
        self.dockWidget = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget)
        #self.widget.setObjectName("widget")
        self.treeView = QtWidgets.QTreeView(self.dockWidget)
        self.treeView.setGeometry(QtCore.QRect(10, 20, 191, 480))
        self.treeView.sizeAdjustPolicy()
        self.treeView.setObjectName("treeView")
        model = QFileSystemModel()
        model.setRootPath('')

        self.treeView.setModel(model)

        self.treeView.setAnimated(True)
        self.treeView.setIndentation(5)
        self.treeView.setSortingEnabled(True)

        self.treeView.setWindowTitle("MRAT workspace")


        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setMinimumSize(QtCore.QSize(10, 10))
        self.menubar.setDefaultUp(False)
        self.menubar.setNativeMenuBar(False)
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
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
        self.menuResults = QtWidgets.QMenu(self.menubar)
        self.menuResults.setObjectName("menuResults")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionSpatio_Temporal = QtWidgets.QAction(MainWindow)
        self.actionSpatio_Temporal.setObjectName("actionSpatio_Temporal")
        self.actionSpatio_Temporal_2 = QtWidgets.QAction(MainWindow)
        self.actionSpatio_Temporal_2.setObjectName("actionSpatio_Temporal_2")
        self.actionNew_Analysis = QtWidgets.QAction(MainWindow)
        self.actionNew_Analysis.setObjectName("actionNew_Analysis")
        self.actionOpen_Analysis = QtWidgets.QAction(MainWindow)
        self.actionOpen_Analysis.setObjectName("actionOpen_Analysis")
        self.actionPTHreshold = QtWidgets.QAction(MainWindow)
        self.actionPTHreshold.setObjectName("actionPTHreshold")
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
        self.menuFile.addAction(self.actionNew_Analysis)
        self.menuFile.addAction(self.actionOpen_Analysis)
        self.menuFile.addAction(self.actionImport_File)
        self.menuFile.addAction(self.actionExport_File)
        self.menuFile.addAction(self.actionQuit)
        self.menuTemporal.addSeparator()
        self.menuTemporal.addAction(self.actionPTHreshold)
        self.menuTemporal.addAction(self.actionTFCE)
        self.menuTemporal.addAction(self.actionWindow)
        self.menuT_TESTS.addSeparator()
        self.menuT_TESTS.addAction(self.menuTemporal.menuAction())
        self.menuT_TESTS.addAction(self.actionSpatio_Temporal_2)
        self.menuStatistics.addAction(self.actionSpatio_Temporal)
        self.menuStatistics.addAction(self.menuT_TESTS.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuData.menuAction())
        self.menubar.addAction(self.menuGraphics.menuAction())
        self.menubar.addAction(self.menuStatistics.menuAction())
        self.menubar.addAction(self.menuResults.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.actionQuit.triggered.connect(MainWindow.close)
        self.form1 = ttestwindow()



        #self.Filedial = QtWidgets.QFileDialog.getExistingDirectory(self, "Find Files",
         #       QtCore.QDir.currentPath())
        self.actionPTHreshold.triggered.connect(self.form1.show)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        ######

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Multi Region Analysis Tool"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuData.setTitle(_translate("MainWindow", "Data"))
        self.menuGraphics.setTitle(_translate("MainWindow", "Graphics"))
        self.menuStatistics.setTitle(_translate("MainWindow", "Statistics"))
        self.menuT_TESTS.setTitle(_translate("MainWindow", "T-TESTS"))
        self.menuTemporal.setTitle(_translate("MainWindow", "Temporal"))
        self.menuResults.setTitle(_translate("MainWindow", "Results"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionSpatio_Temporal.setText(_translate("MainWindow", "ANOVAs"))
        self.actionSpatio_Temporal_2.setText(_translate("MainWindow", "Spatio-Temporal"))
        self.actionNew_Analysis.setText(_translate("MainWindow", "New Analysis"))
        self.actionOpen_Analysis.setText(_translate("MainWindow", "Open Analysis"))
        self.actionPTHreshold.setText(_translate("MainWindow", "PTHreshold"))
        self.actionPTHreshold.setStatusTip(_translate("MainWindow", "Run PTHRESHOLD temporal t-test analysis"))
        self.actionTFCE.setText(_translate("MainWindow", "TFCE"))
        self.actionWindow.setText(_translate("MainWindow", "window"))
        self.actionImport_File.setText(_translate("MainWindow", "Import File"))
        self.actionExport_File.setText(_translate("MainWindow", "Export File"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))

