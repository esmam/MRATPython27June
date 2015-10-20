# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ttestformSourceTemporalPTHRESHOLD.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(468, 435)
        self.formLayout = QtWidgets.QFormLayout(Form)
        self.formLayout.setObjectName("formLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.endTimeLabel = QtWidgets.QLabel(Form)
        self.endTimeLabel.setObjectName("endTimeLabel")
        self.gridLayout.addWidget(self.endTimeLabel, 5, 0, 1, 1)
        self.thresholdPValueLabel = QtWidgets.QLabel(Form)
        self.thresholdPValueLabel.setObjectName("thresholdPValueLabel")
        self.gridLayout.addWidget(self.thresholdPValueLabel, 7, 0, 1, 1)
        self.minimumTemporalClusterLineEdit = QtWidgets.QLineEdit(Form)
        self.minimumTemporalClusterLineEdit.setObjectName("minimumTemporalClusterLineEdit")
        self.gridLayout.addWidget(self.minimumTemporalClusterLineEdit, 8, 1, 1, 1)
        self.startTimeLabel = QtWidgets.QLabel(Form)
        self.startTimeLabel.setObjectName("startTimeLabel")
        self.gridLayout.addWidget(self.startTimeLabel, 4, 0, 1, 1)
        self.prestimulusLineEdit = QtWidgets.QLineEdit(Form)
        self.prestimulusLineEdit.setObjectName("prestimulusLineEdit")
        self.gridLayout.addWidget(self.prestimulusLineEdit, 6, 1, 1, 1)
        self.condition2Label = QtWidgets.QLabel(Form)
        self.condition2Label.setObjectName("condition2Label")
        self.gridLayout.addWidget(self.condition2Label, 2, 0, 1, 1)
        self.minimFDRRateLabel = QtWidgets.QLabel(Form)
        self.minimFDRRateLabel.setObjectName("minimFDRRateLabel")
        self.gridLayout.addWidget(self.minimFDRRateLabel, 9, 0, 1, 1)
        self.thresholdPValueLineEdit = QtWidgets.QLineEdit(Form)
        self.thresholdPValueLineEdit.setObjectName("thresholdPValueLineEdit")
        self.gridLayout.addWidget(self.thresholdPValueLineEdit, 7, 1, 1, 1)
        self.find = QtWidgets.QPushButton(Form)
        self.find.setObjectName("find")
        self.gridLayout.addWidget(self.find, 1, 1, 1, 1)
        self.condition2LineEdit = QtWidgets.QLineEdit(Form)
        self.condition2LineEdit.setObjectName("condition2LineEdit")
        self.gridLayout.addWidget(self.condition2LineEdit, 2, 1, 1, 1)
        self.condition1Label = QtWidgets.QLabel(Form)
        self.condition1Label.setObjectName("condition1Label")
        self.gridLayout.addWidget(self.condition1Label, 0, 0, 1, 1)
        self.prestimulusLabel = QtWidgets.QLabel(Form)
        self.prestimulusLabel.setObjectName("prestimulusLabel")
        self.gridLayout.addWidget(self.prestimulusLabel, 6, 0, 1, 1)
        self.minimFDRRateLineEdit = QtWidgets.QLineEdit(Form)
        self.minimFDRRateLineEdit.setObjectName("minimFDRRateLineEdit")
        self.gridLayout.addWidget(self.minimFDRRateLineEdit, 9, 1, 1, 1)
        self.endTimeLineEdit = QtWidgets.QLineEdit(Form)
        self.endTimeLineEdit.setObjectName("endTimeLineEdit")
        self.gridLayout.addWidget(self.endTimeLineEdit, 5, 1, 1, 1)
        self.startTimeLineEdit = QtWidgets.QLineEdit(Form)
        self.startTimeLineEdit.setObjectName("startTimeLineEdit")
        self.gridLayout.addWidget(self.startTimeLineEdit, 4, 1, 1, 1)
        self.condition1LineEdit = QtWidgets.QLineEdit(Form)
        self.condition1LineEdit.setObjectName("condition1LineEdit")
        self.gridLayout.addWidget(self.condition1LineEdit, 0, 1, 1, 1)
        self.numberOfPermutationsLabel = QtWidgets.QLabel(Form)
        self.numberOfPermutationsLabel.setObjectName("numberOfPermutationsLabel")
        self.gridLayout.addWidget(self.numberOfPermutationsLabel, 11, 0, 1, 1)
        self.tailLabel = QtWidgets.QLabel(Form)
        self.tailLabel.setObjectName("tailLabel")
        self.gridLayout.addWidget(self.tailLabel, 10, 0, 1, 1)
        self.find_2 = QtWidgets.QPushButton(Form)
        self.find_2.setObjectName("find_2")
        self.gridLayout.addWidget(self.find_2, 3, 1, 1, 1)
        self.tailComboBox = QtWidgets.QComboBox(Form)
        self.tailComboBox.setObjectName("tailComboBox")
        self.tailComboBox.addItem("")
        self.tailComboBox.addItem("")
        self.tailComboBox.addItem("")
        self.tailComboBox.addItem("")
        self.gridLayout.addWidget(self.tailComboBox, 10, 1, 1, 1)
        self.numberOfPermutationsLineEdit = QtWidgets.QLineEdit(Form)
        self.numberOfPermutationsLineEdit.setObjectName("numberOfPermutationsLineEdit")
        self.gridLayout.addWidget(self.numberOfPermutationsLineEdit, 11, 1, 1, 1)
        self.minimumTemporalClusterLabel = QtWidgets.QLabel(Form)
        self.minimumTemporalClusterLabel.setObjectName("minimumTemporalClusterLabel")
        self.gridLayout.addWidget(self.minimumTemporalClusterLabel, 8, 0, 1, 1)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.SpanningRole, self.gridLayout)
        self.cancel = QtWidgets.QPushButton(Form)
        self.cancel.setObjectName("cancel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.cancel)
        self.Ok = QtWidgets.QPushButton(Form)
        self.Ok.setObjectName("Ok")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.Ok)

        self.retranslateUi(Form)

        self.cancel.clicked.connect(Form.close)

        self.Ok.clicked.connect(self.RunAnalysis)
        self.find.clicked.connect(self.FindFolder)
        #self.find.clicked.connect(self.FindFolder)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.condition1LineEdit, self.find)
        Form.setTabOrder(self.find, self.condition2LineEdit)
        Form.setTabOrder(self.condition2LineEdit, self.find_2)
        Form.setTabOrder(self.find_2, self.startTimeLineEdit)
        Form.setTabOrder(self.startTimeLineEdit, self.endTimeLineEdit)
        Form.setTabOrder(self.endTimeLineEdit, self.prestimulusLineEdit)
        Form.setTabOrder(self.prestimulusLineEdit, self.thresholdPValueLineEdit)
        Form.setTabOrder(self.thresholdPValueLineEdit, self.minimumTemporalClusterLineEdit)
        Form.setTabOrder(self.minimumTemporalClusterLineEdit, self.minimFDRRateLineEdit)
        Form.setTabOrder(self.minimFDRRateLineEdit, self.tailComboBox)
        Form.setTabOrder(self.tailComboBox, self.numberOfPermutationsLineEdit)
        Form.setTabOrder(self.numberOfPermutationsLineEdit, self.cancel)
        Form.setTabOrder(self.cancel, self.Ok)
        ## find folder

    def FindFolder(self):

        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Find Files",
                QtCore.QDir.currentPath())

        self.condition1LineEdit.setText(directory)

    def FindFolder2(self):

        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Find Files",
                QtCore.QDir.currentPath())

        self.condition2LineEdit.setText(directory)


    ##### record all data entered in the form and pass it to the ttest function
    def RunAnalysis(self):
        condition1Name = self.condition1LineEdit.text()
        condition2Name = self.condition2LineEdit.text()
        startTime = self.startTimeLineEdit.text()
        endTime = self.endTimeLineEdit.text()
        presTim = self.prestimulusLineEdit.text()
        PThresh = self.thresholdPValueLineEdit.text()
        minTemporalCluster = self.minimumTemporalClusterLineEdit.text()
        minFDR = self.minimFDRRateLineEdit.text()
        numPerm = self.numberOfPermutationsLineEdit.text()
        anlsysTail = self.tailComboBox.currentData()


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.endTimeLabel.setText(_translate("Form", "End Time"))
        self.thresholdPValueLabel.setText(_translate("Form", "Threshold p-value"))
        self.startTimeLabel.setText(_translate("Form", "Start Time"))
        self.condition2Label.setText(_translate("Form", "Condition 2 "))
        self.minimFDRRateLabel.setText(_translate("Form", "Maximum FDR rate"))
        self.find.setText(_translate("Form", "find"))
        self.condition1Label.setText(_translate("Form", "Condition 1"))
        self.prestimulusLabel.setText(_translate("Form", "Prestimulus"))
        self.numberOfPermutationsLabel.setText(_translate("Form", "Number of permutations"))
        self.tailLabel.setText(_translate("Form", "tail"))
        self.find_2.setText(_translate("Form", "find"))
        self.tailComboBox.setItemText(0, _translate("Form", "Please choose an option"))
        self.tailComboBox.setItemText(1, _translate("Form", "Both"))
        self.tailComboBox.setItemText(2, _translate("Form", "Left tail"))
        self.tailComboBox.setItemText(3, _translate("Form", "Right Tail"))
        self.minimumTemporalClusterLabel.setText(_translate("Form", "Minimum Temporal Cluster"))
        self.cancel.setText(_translate("Form", "Cancel"))
        self.Ok.setText(_translate("Form", "Run Analysis"))

