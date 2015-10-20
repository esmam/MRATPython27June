__author__ = 'esmab'


  self.cancel.clicked.connect(self.close)
        self.Ok.clicked.connect(self.RunAnalysis)
        self.FindpushButton.clicked.connect(self.FindFolder)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.ProjecTRoot, self.FindpushButton)
        Form.setTabOrder(self.FindpushButton, self.Condition1Name)
        Form.setTabOrder(self.Condition1Name, self.Condition1Name_2)
        Form.setTabOrder(self.Condition1Name_2, self.StartTime)
        Form.setTabOrder(self.StartTime, self.StartTime_2)
        Form.setTabOrder(self.StartTime_2, self.Prestimulus)
        Form.setTabOrder(self.Prestimulus, self.PthreshVal)
        Form.setTabOrder(self.PthreshVal, self.MinTempCluster)
        Form.setTabOrder(self.MinTempCluster, self.MAXFDR)
        Form.setTabOrder(self.MAXFDR, self.tailComboBox)
        Form.setTabOrder(self.tailComboBox, self.NumberPermutaiton)
        Form.setTabOrder(self.NumberPermutaiton, self.cancel)
        Form.setTabOrder(self.cancel, self.Ok)




    def FindFolder(self):

            directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Find Files",
            QtCore.QDir.currentPath())

            self.ProjecTRoot.setText(directory)
        ##### record all data entered in the form and pass it to the ttest function
    def RunAnalysis(self):
            condition1Name = self.Condition1Name.text()

            condition2Name = self.Condition1Name_2.text()
            startTime = self.StartTime.text()
            endTime = self.EndTime.text()
            presTim = self.Prestimulus.text()
            PThresh = self.PthreshVal.text()
            minTemporalCluster = self.MinTempCluster.text()
            maxFDR = self.MAXFDR.text()
            numPerm = self.NumberPermutaiton.text()
            anlsysTail = self.tailComboBox.currentData()

            if condition1Name == "" or condition2Name == "":
                QtWidgets.QMessageBox.information(self, "Empty Field",
                "Please enter all the required information in the form .")
            return
