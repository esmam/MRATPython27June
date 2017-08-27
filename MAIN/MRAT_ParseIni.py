####
#Extract data from ini and pass it to a statistical funciton
# Author Esma Mansouri

###
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'temporalpthreshsourcettest1006.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
# Implementation of t-test window form
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore,QtGui, QtWidgets
#import _thread
from PyQt5.QtWidgets import (QWidget, QProgressBar,QFileDialog,
    QPushButton, QApplication)
from PyQt5.QtCore import QBasicTimer
from PyQt5.QtCore import QObject, pyqtSignal
import random
import numpy as np
import matplotlib
matplotlib.use("Qt5Agg")

#from PyQt5 import QtCore
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
from PThresholdTemporalSourceTTestMNE import PThresholdTempSourceTTestMNE

from PThresholdSpatialSourceTTest import PThresholdSpatialSourceTTest
from PThresholdSpatialSourceTTestMNE import PThresholdSpatialSourceTTestMNE

import ConfigParser
from PyQt5 import QtGui
from PThresholdTemporalSourceTTestMNE import PThresholdTempSourceTTestMNE
from PThresholdTemporalSourceTTest import PThresholdTempSourceTTest
from ANOVAtoEelbrainMNESpatialTFCE import ANOVA22BESASpatialMNETFCE

def openIni(self):
    fileName = QtGui.QFileDialog.getOpenFileName(self, 'OpenFile')
    myTextBox.setText(fileName)
    print(fileName)


def MRAT_IniParser(filename):

    config = ConfigParser.ConfigParser()
    ini = config.read(filename)
    testType =  config.get('testOptions', 'anovaOrT')
    SpatioTemp = config.get('SpatioTemp', 'SpatioTemp')
    TFCEPerm = config.get('testOptions', 'TFCEPerm')
    windowOrPerm = config.get('testOptions', 'windowOrPerm')
    anovaOrT = config.get('testOptions', 'anovaOrT')
    badsubjects = config.get('testOptions', 'badsubjs')
    TOI = config.get('timeWindow', 'TOI')

    TOI = TOI.split(' ')
    starttime = int(TOI[0])
    endtime = int(TOI[1])
    preStimInterval = config.get('timeWindow', 'preStimInterval')

    regionNames = config.get('regionNames', 'regionNames')

    dataSet = config.get('dataSet', 'path')

    if  'spatio' not in SpatioTemp.lower():
    #extract data
        if 'ttest' in testType.lower():



            tail = config.get('testOptions', 'tail')


            numPerms = config.get('testOptions', 'numPerms')
            minClusterLength = config.get('testOptions', 'minClusterLength')



            #if  'Spatio' in SpatioTemp.lower():
            #    minClusterLengthSpatio = config.get('testOptions', 'minClusterLengthSpatio')
            maxFDR = config.get('testOptions', 'maxFDR')
            sensorOrSource = config.get('testOptions', 'sensorOrSource')

            test1 = config.get('testOptions', 'test1')

            compTestPThresh = config.get('testOptions', 'compTestPThresh')



            MNEORBESA = config.get('MNEORBESA', 'MNEORBESA')

            condition1 = config.get('CONDITIONS', 'condition1')

            condition2 = config.get('CONDITIONS', 'condition2')

            #condition1Name = 'test'

            #condition2Name = 'test1'

            FDR = config.get('FDR', 'FDR')

            if  'temp' in SpatioTemp.lower():
                #call spatio temp ttest function
                if 'BESA' in MNEORBESA:
                    Multiple,Results, sigregion,AllRegionsLargestIndex, allRegions,ROISources = PThresholdTempSourceTTest(badsubjects,dataSet, condition1, condition2,starttime,endtime, preStimInterval,compTestPThresh,minClusterLength, numPerms, tail, regionNames,maxFDR)
                elif 'MNE' in MNEORBESA:
                    Multiple,Results, sigregion,AllRegionsLargestIndex, allRegions,ROISources = PThresholdTempSourceTTestMNE(badsubjects,dataSet, condition1, condition2,starttime,endtime, preStimInterval,compTestPThresh,minClusterLength, numPerms, tail, regionNames,maxFDR)


            #######


            resultsAll = Results

            #get conditions names
            #need to check of it is multiple ROI or just one
            a = resultsAll

            if Multiple  == 1:
                a = 1
                ind = 0
                from PyQt5 import QtCore, QtGui, QtWidgets
                from mainwindow import Ui_MainWindow

                Regionnames1 = []
                durations1 = []
                ids1=[]
                ps1=[]
                sigs1=[]
                tstarts1=[]
                tstops1=[]
                l = len(resultsAll)#.__len__
                firstPlotDone = 0
                for ind in range(0, l):

                    CurrRegSources = ROISources[ind]

                    Regionnames = []
                    durations = []
                    ids=[]
                    ps=[]
                    sigs=[]
                    tstarts=[]
                    tstops=[]
                    FDRsig=[]
                    AllRegionsLargestIndexCurr = AllRegionsLargestIndex[ind]
                    current = resultsAll[ind]
                    if current is dict:
                        test = 1

                    cluster_table = current.clusters.as_table()

                    resultsForPlot = resultsAll[ind]._default_plot_obj

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



                    ##############

                    #############

                    Results = resultsAll[ind].clusters

                    #main_widget = QWidget(mainwindow.Ui_MainWindow.dockPlot())
                    main_widget = QtWidgets.QDockWidget()
                    #main_widget = QtWidgets.QWidget()


                    if firstPlotDone == 0:

                        l = QVBoxLayout(main_widget)
                        sc = MyStaticMplCanvas(main_widget, width=5, height=4, dpi=100)
                        #dc = MyDynamicMplCanvas(main_widget, width=5, height=4, dpi=100)
                        #MyStaticMplCanvas.compute_initial_figure(main_widget)
                        #MyStaticMplCanvas.compute_initial_figure1(sc,startx,endx,stepx,cond1Data,cond2Data, condition1Name,condition2Name)
                        MyStaticMplCanvas.compute_initial_figure(sc) #,startx,endx,stepx,cond1Data,cond2Data, condition1Name,condition2Name)

                        l.addWidget(sc)
                        firstPlotDone = 1

                    #from MRAT_PlotBESABrain import PlotBESABrain
                    #PlotBESABrain(ROISources)

                    #PLotWidget = QWidget()
                    #PLotWidget = l.widget()

                    #DockPlot = QDockWidget.create
                    #Ui_MainWindow.dockPlot
                    #Ui_MainWindow
                    #Ui_MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), l)

                    #main_widget.show()


                        sc.cond1 = cond1Data
                        sc.cond2 = cond2Data
                        sc.start = startx
                        sc.end = endx
                        sc.step = stepx
                        sc.condition1Name = condition1
                        sc.condition2Name = condition2
                        #sc.allRegions = allRegions
                        sc.ROISources = ROISources




                    #Extract epoch time for x axis for each condition

                    #Extract y axis values
                    #print(Results.clusters)
                    #x = Results.clusters[1, 'cluster'].x
                    #d = Results.clusters[0, 'cluster'].any()
                    #data = {'ClusterID':['1','2','3'], 'n_sources':['4','5','6'], 'hemisphere':['7','8','9'],'Start Time':['7','8','9'],'End Time':['7','8','9'],'Duration':['7','8','9'],'P-value':['7','8','9']}

                    cluster = Results.get('cluster')
                    #len = Results._len_
                    duration = Results.get('duration')
                    from MRAT_PlotBESABrain import PlotBESABrain
                    for _len_ in duration:

                        durations.append(str(int(_len_*1000)))

                    index = 1
                    id = Results.get('id')
                    for _len_ in id:
                        #ids.append(str(_len_))
                        ids.append(str(index))
                        index = index +1


                    p = Results.get('p')
                    for _len_ in p:
                        ps.append(str(_len_))

                    sig = Results.get('sig')
                    tstop = Results.get('tstop')
                    for _len_ in sig:
                        sigs.append(str(_len_))



                    tstart = Results.get('tstart')
                    for _len_ in tstart:
                        tstarts.append(str(int(_len_*1000)))



                    for _len_ in tstop:
                        tstops.append(str(int(_len_*1000)))
                        allRegions = list(allRegions)
                        name = allRegions[ind]
                        name = name.replace('[', '')
                        Regionnames.append(name)

                    v = Results.get('v')

                    if AllRegionsLargestIndexCurr > -1:

                        Regionnames1.append(Regionnames[AllRegionsLargestIndexCurr])
                        ids1.append(ids[AllRegionsLargestIndexCurr])
                        durations1.append(durations[AllRegionsLargestIndexCurr])
                        tstarts1.append(tstarts[AllRegionsLargestIndexCurr])
                        tstops1.append(tstops[AllRegionsLargestIndexCurr])
                        ps1.append(ps[AllRegionsLargestIndexCurr])
                        sigs1.append(sigs[AllRegionsLargestIndexCurr])
                        #get header
                    index = 0
                    for i in range(0,len(allRegions)):
                        #ids.append(str(_len_))
                        #FDRsig.append(str(sigregion))
                        allRegions = list(allRegions)
                        name = allRegions[i]
                        name = name.replace('[', '')
                        if name in sig:
                            FDRsig.append(str('Sig after FDR'))
                        else:
                            FDRsig.append(str('no sig after FDR'))



                    data = {'0 Region Name':Regionnames1,'1 Largest ClusterID':ids1, '2 Duration':durations1, '3 Start time':tstarts1,'4 End Time':tstops1, '5 P-value': ps1,'6 Sig':sigs1, '7 FDR sig': FDRsig} #,'Duration':['7','8','9'],'P-value':['7','8','9']}
    
    
                    table = MyTable(sc,data,ROISources, MNEORBESA,len(durations1),8)#,startx,endx,stepx,cond1Data,cond2Data)
    
    
                    import csv
    
      




                    with open(dataSet+'/'+condition1+'_'+condition2+'_Results.csv', 'wb') as f:  # This creates the file object for the context
                                          # below it and closes the file automatically
                        l = []
                        l1=[]
                        writer = csv.writer(f)
                        for k, v in data.iteritems(): # Iterate over items returning key, value tuples
                            l1.append('%s: ' % (str(k)))
                            #l1.append('%s: ' % (str(v)))
                            #f.write(', '.join(l1))
                            #writer.writerow(k)
    
    
                            for item in v:
                              l1.append('%s' % ( str(item))) # Build a nice list of strings
                            #  writer.writerow(zip(v))
                              #f.write(', '.join(l))
                            #
                              #f.write(item)
                            writer.writerow(zip(l1))
                            l1=[]
    
                   #### TODO fix the layout of the csv
    
    
                    table.show()






            else:


                cluster_table = Results.clusters.as_table()

                resultsForPlot = Results._default_plot_obj

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

                ##############

                #############

                Results = Results.clusters

                #main_widget = QWidget(mainwindow.Ui_MainWindow.dockPlot())
                main_widget = QtWidgets.QDockWidget()
                #main_widget = QtWidgets.QWidget()



                a = 1
                ind = 0
                from PyQt5 import QtCore, QtGui, QtWidgets
                from mainwindow import Ui_MainWindow

                Regionnames1 = []
                durations1 = []
                ids1=[]
                ps1=[]
                sigs1=[]
                tstarts1=[]
                tstops1=[]
                l =  1 #len(resultsAll)#.__len__
                firstPlotDone = 0
                for ind in range(0, l):

                    Regionnames = []
                    durations = []
                    ids=[]
                    ps=[]
                    sigs=[]
                    tstarts=[]
                    tstops=[]
                    FDRsig=[]
                    AllRegionsLargestIndexCurr = AllRegionsLargestIndex[ind]
                    current = resultsAll
                    if current is dict:
                        test = 1

                    cluster_table = current.clusters.as_table()

                    resultsForPlot = resultsAll._default_plot_obj

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



                    ##############

                    #############

                    Results = resultsAll.clusters

                    #main_widget = QWidget(mainwindow.Ui_MainWindow.dockPlot())
                    main_widget = QtWidgets.QDockWidget()
                    #main_widget = QtWidgets.QWidget()


                    if firstPlotDone == 0:

                        l = QVBoxLayout(main_widget)
                        sc = MyStaticMplCanvas(main_widget, width=5, height=4, dpi=100)
                        #dc = MyDynamicMplCanvas(main_widget, width=5, height=4, dpi=100)
                        #MyStaticMplCanvas.compute_initial_figure(main_widget)
                        #MyStaticMplCanvas.compute_initial_figure1(sc,startx,endx,stepx,cond1Data,cond2Data, condition1Name,condition2Name,MNEBESA)
                        MyStaticMplCanvas.compute_initial_figure(sc)
                        #MyStaticMplCanvas.compute_initial_figure1(sc,startx,endx,stepx,cond1Data,cond2Data, condition1Name,condition2Name,MNEBESA)
                        l.addWidget(sc)
                        firstPlotDone = 1


                        sc.cond1 = cond1Data
                        sc.cond2 = cond2Data
                        sc.start = startx
                        sc.end = endx
                        sc.step = stepx

                        sc.condition1Name = condition1
                        sc.condition2Name = condition2
                        #self.sc.allRegions = allRegions
                        sc.ROISources = ROISources
                        sc.directory = dataSet
                        sc.Results = Results
                        sc.Sources = False



                        sc.cond1 = cond1Data
                        sc.cond2 = cond2Data
                        sc.start = startx
                        sc.end = endx
                        sc.step = stepx

                        sc.condition1Name = condition1
                        sc.condition2Name = condition2
                        #sc.allRegions = allRegions
                        sc.ROISources = ROISources


                    cluster = Results.get('cluster')
                    #len = Results._len_
                    duration = Results.get('duration')
                    from MRAT_PlotBESABrain import PlotBESABrain
                    for _len_ in duration:

                        durations.append(str(int(_len_*1000)))

                    index = 1
                    id = Results.get('id')
                    for _len_ in id:
                        #ids.append(str(_len_))
                        ids.append(str(index))
                        index = index +1


                    p = Results.get('p')
                    for _len_ in p:
                        ps.append(str(_len_))

                    sig = Results.get('sig')
                    for _len_ in sig:
                        sigs.append(str(_len_))

                    tstart = Results.get('tstart')
                    for _len_ in tstart:
                        tstarts.append(str(int(_len_*1000)))

                    tstop = Results.get('tstop')

                    for _len_ in tstop:
                        tstops.append(str(int(_len_*1000)))
                        allRegions = allRegions
                        name = allRegions

                        Regionnames.append(name)

                    v = Results.get('v')

                    if AllRegionsLargestIndexCurr > -1:

                        Regionnames1.append(Regionnames[AllRegionsLargestIndexCurr])
                        ids1.append(ids[AllRegionsLargestIndexCurr])
                        durations1.append(durations[AllRegionsLargestIndexCurr])
                        tstarts1.append(tstarts[AllRegionsLargestIndexCurr])
                        tstops1.append(tstops[AllRegionsLargestIndexCurr])
                        ps1.append(ps[AllRegionsLargestIndexCurr])
                        sigs1.append(sigs[AllRegionsLargestIndexCurr])
                        #get header

                    for _len_ in id:
                        #ids.append(str(_len_))
                        FDRsig.append(str(1))
                        index = index +1

                data = {'0 Region Name':Regionnames1,'1 Largest ClusterID':ids1, '2 Duration':durations1, '3 Start time':tstarts1,'4 End Time':tstops1, '5 P-value': ps1,'6 Sig':sigs1, '7 FDR sig': FDRsig} #,'Duration':['7','8','9'],'P-value':['7','8','9']}


                table = MyTable(sc,data,ROISources, MNEORBESA,len(durations1),8)#,startx,endx,stepx,cond1Data,cond2Data)






                table.show()




            ######
        elif  'ANOVA' in testType:

            TFCEPerm = config.get('testOptions', 'TFCEPerm')
            windowOrPerm = config.get('testOptions', 'windowOrPerm')

            anovaOrT = config.get('testOptions', 'anovaOrT')




            numPerms = config.get('testOptions', 'numPerms')
            minClusterLength = config.get('testOptions', 'minClusterLength')

            maxFDR = config.get('testOptions', 'maxFDR')
            sensorOrSource = config.get('testOptions', 'sensorOrSource')

            anovadesign = config.get('testOptions', 'anovaScript')
            minClusterLengthSpatio = config.get('testOptions', 'minClusterLengthSpatio')
            #test1 = config.get('testOptions', 'test1')

            compTestPThresh = config.get('testOptions', 'compTestPThresh')







            SpatioTemp = config.get('SpatioTemp', 'SpatioTemp')

            MNEORBESA = config.get('MNEORBESA', 'MNEORBESA')

            conditions = config.get('dataSet', 'conditions')




            FDR = config.get('FDR', 'FDR')

            if 'BESA' in MNEORBESA:

                Multiple,Results, sigregion,AllRegionsLargestIndex, allRegions,ROISources,Allconditions2,Numsubjects,datsbycondition, AllFactors,parmMap1,threshold005,threshold03  = ANOVA22BESATemporal(badsubjects,dataSet, anovadesign,conditions, starttime,endtime, preStimInterval,compTestPThresh,minClusterLength, numPerms,  regionNames,maxFDR)

            elif 'MNE' in MNEORBESA:
                Multiple,Results, sigregion,AllRegionsLargestIndex, allRegions,ROISources,Allconditions2,Numsubjects,datsbycondition, AllFactors,parmMap1,threshold005,threshold03  = ANOVA22BESATemporalMNE(badsubjects,dataSet,anovadesign, conditions ,starttime,endtime, preStimInterval,compTestPThresh,minClusterLength, numPerms,  regionNames,maxFDR)


        #now dispaly results
    else: #Spatiotemporal

        if 'ttest' in testType.lower():

            TFCEPerm = config.get('testOptions', 'TFCEPerm')
            windowOrPerm = config.get('testOptions', 'windowOrPerm')

            anovaOrT = config.get('testOptions', 'anovaOrT')

            tail = config.get('testOptions', 'tail')


            numPerms = config.get('testOptions', 'numPerms')
            minClusterLength = config.get('testOptions', 'minClusterLength')



            minClusterLengthSpatio = config.get('testOptions', 'minClusterLengthSpatio')
            maxFDR = config.get('testOptions', 'maxFDR')
            sensorOrSource = config.get('testOptions', 'sensorOrSource')

            test1 = config.get('testOptions', 'test1')

            compTestPThresh = config.get('testOptions', 'compTestPThresh')









            MNEORBESA = config.get('MNEORBESA', 'MNEORBESA')

            condition1 = config.get('CONDITIONS', 'condition1')

            condition2 = config.get('CONDITIONS', 'condition2')

            #condition1Name = 'test'

            #condition2Name = 'test1'

            FDR = config.get('FDR', 'FDR')


            if 'BESA' in MNEORBESA:

                Multiple,Results, sigregion,AllRegionsLargestIndex, allRegions,ROISources = PThresholdSpatialSourceTTest(badsubjects,dataSet, condition1, condition2,starttime,endtime, preStimInterval,compTestPThresh,minClusterLength, numPerms, tail, regionNames,maxFDR)


            elif 'MNE' in MNEORBESA:

                    Multiple,Results, sigregion,AllRegionsLargestIndex, allRegions,ROISources = PThresholdSpatialSourceTTestMNE(badsubjects,dataSet, condition1, condition2,starttime,endtime, preStimInterval,compTestPThresh,minClusterLength, numPerms, tail, regionNames,maxFDR)

            #######

            resultsAll = Results

            #clusters = Results.clusters['cluster']
            #cluster_table = Results.clusters.as_table()
            #c = cluster_table._table
            #get conditions names
            #need to check of it is multiple ROI or just one
            a = resultsAll

            if Multiple  == 1:
                a = 1
                ind = 0
                from PyQt5 import QtCore, QtGui, QtWidgets
                from mainwindow import Ui_MainWindow
                Regionnames = []
                durations = []
                ids=[]
                ps=[]
                sigs=[]
                tstarts=[]
                tstops=[]
                l = len(resultsAll)#.__len__
                firstPlotDone = 0
                Regionnames1 = []
                durations1 = []
                ids1=[]
                ps1=[]
                sigs1=[]
                tstarts1=[]
                tstops1=[]
                effects=[]
                sourcenum = []
                locations1=[]
                sourcenum1=[]

                locations2=[]

                for ind in range(0, l):
                    current = resultsAll[ind]
                    if current is dict:
                        test = 1

                    cluster_table = current.clusters.as_table()

                    resultsForPlot = resultsAll[ind]._default_plot_obj

                    Cond1 = resultsForPlot[0]
                    Cond1Name = Cond1.name
                    Cond2 = resultsForPlot[1]
                    Cond2Name = Cond2.name

                    cond1Data = Cond1.x
                    cond2Data = Cond2.x
                    XAxisVals = Cond1.dims # X AXIS Y AXIS THEN PLOT
                    Startx = XAxisVals[1]
                    startx = (Startx.tmin)*1000
                    endx = (Startx.tmax)*1000
                    stepx = (Startx.tstep)*1000
                    name = Startx.name
                    nsamples = Startx.nsamples



                    ##############

                    #############

                    Results = resultsAll[ind].clusters

                    #main_widget = QWidget(mainwindow.Ui_MainWindow.dockPlot())
                    main_widget = QtWidgets.QDockWidget()
                    #main_widget = QtWidgets.QWidget()


                    if firstPlotDone == 0:

                        l = QVBoxLayout(main_widget)
                        sc = MyStaticMplCanvas(main_widget, width=5, height=4, dpi=100)
                        #dc = MyDynamicMplCanvas(main_widget, width=5, height=4, dpi=100)
                        #MyStaticMplCanvas.compute_initial_figure(main_widget)
                        MyStaticMplCanvas.compute_initial_figure(sc)
                        #MyStaticMplCanvas.compute_initial_figure1(sc,startx,endx,stepx,cond1Data,cond2Data, condition1Name,condition2Name,MNEBESA)
                        l.addWidget(sc)
                        firstPlotDone = 1

                    #from MRAT_PlotBESABrain import PlotBESABrain
                    #PlotBESABrain(ROISources)

                    #PLotWidget = QWidget()
                    #PLotWidget = l.widget()

                    #DockPlot = QDockWidget.create
                    #Ui_MainWindow.dockPlot
                    #Ui_MainWindow
                    #Ui_MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), l)

                    #main_widget.show()


                        sc.cond1 = cond1Data
                        sc.cond2 = cond2Data
                        sc.start = startx
                        sc.end = endx
                        sc.step = stepx

                        sc.condition1Name = condition1
                        sc.condition2Name = condition2
                        #sc.allRegions = allRegions
                        sc.ROISources = ROISources



                    #Extract epoch time for x axis for each condition

                    #Extract y axis values
                    #print(Results.clusters)
                    #x = Results.clusters[1, 'cluster'].x
                    #d = Results.clusters[0, 'cluster'].any()
                    #data = {'ClusterID':['1','2','3'], 'n_sources':['4','5','6'], 'hemisphere':['7','8','9'],'Start Time':['7','8','9'],'End Time':['7','8','9'],'Duration':['7','8','9'],'P-value':['7','8','9']}

                    cluster = Results.get('cluster')
                    #len = Results._len_
                    duration = Results.get('duration')
                    for _len_ in duration:

                        durations.append(str(int(_len_*1000)))

                    index = 1
                    id = Results.get('id')
                    for _len_ in id:
                        #ids.append(str(_len_))
                        ids.append(str(index))
                        index = index +1


                    p = Results.get('p')
                    for _len_ in p:
                        ps.append(str(_len_))

                    sig = Results.get('sig')
                    for _len_ in sig:
                        sigs.append(str(_len_))

                    tstart = Results.get('tstart')
                    for _len_ in tstart:
                        tstarts.append(str(int(_len_*1000)))

                    tstop = Results.get('tstop')

                    for _len_ in tstop:
                        tstops.append(str(int(_len_*1000)))
                        allRegions = list(allRegions)
                        name = allRegions[ind]
                        name = name.replace('[', '')
                        Regionnames.append(name)

                    v = Results.get('v')

                    sourcenum = Results.get('n_sources')
                    sourcenum1=[]
                    locations1 = Results.get('location')
                    locations2=[]
                    v = Results.get('v')
                    AllRegionsLargestIndexCurr = AllRegionsLargestIndex[l]

                    if AllRegionsLargestIndexCurr > -1:

                            #get length of the clusters by effects and then print in for loop
                        AllRegionsLargestIndexCurr=AllRegionsLargestIndexCurr[0]




                        IndexCurr = AllRegionsLargestIndexCurr
                        IndexCurr = int(IndexCurr)

                        Regionnames1.append(Regionnames[IndexCurr])
                        sourcenum1.append(str(sourcenum[IndexCurr]))

                        locations2.append(locations1[IndexCurr])
                        ids1.append(ids[IndexCurr])
                        durations1.append(durations[IndexCurr])
                        tstarts1.append(tstarts[IndexCurr])
                        tstops1.append(tstops[IndexCurr])
                        ps1.append(ps[IndexCurr])
                        sigs1.append(sigs[IndexCurr])

                    #get header

                data = {'0 Region Name':Regionnames,'1 ClusterID':ids, '2 Duration':durations, '3 Start time':tstarts,'4 End Time':tstops, '5 P-value': ps,'6 Sig':sigs} #,'Duration':['7','8','9'],'P-value':['7','8','9']}


                table = MyTable(sc,data, len(durations),7)#,startx,endx,stepx,cond1Data,cond2Data)
                #l.addWidget(sc)



                table.show()




            ######
        elif  'ANOVA' in testType:

            TFCEPerm = config.get('testOptions', 'TFCEPerm')
            windowOrPerm = config.get('testOptions', 'windowOrPerm')

            anovaOrT = config.get('testOptions', 'anovaOrT')




            numPerms = config.get('testOptions', 'numPerms')
            minClusterLength = config.get('testOptions', 'minClusterLength')
            minClusterLengthSpatio = config.get('testOptions', 'minClusterLengthSpatio')
            maxFDR = config.get('testOptions', 'maxFDR')
            sensorOrSource = config.get('testOptions', 'sensorOrSource')



            anovadesign = config.get('testOptions', 'anovaScript')
            #minClusterLengthSpatio = config.get('testOptions', 'minClusterLengthSpatio')
            #test1 = config.get('testOptions', 'test1')

            compTestPThresh = config.get('testOptions', 'compTestPThresh')

            TOI = config.get('timeWindow', 'TOI')






            SpatioTemp = config.get('SpatioTemp', 'SpatioTemp')

            MNEORBESA = config.get('MNEORBESA', 'MNEORBESA')

            conditions = config.get('dataSet', 'conditions')

            badsubjects = config.get('testOptions', 'badsubjs')

            TOI = TOI.split(' ')
            starttime = int(TOI[0])
            endtime = int(TOI[1])

            FDR = config.get('FDR', 'FDR')
            if 'TFCE' in TFCEPerm:

                if 'BESA' in MNEORBESA:

                    Multiple,Results, sigregion,AllRegionsLargestIndex, allRegions,ROISources,Allconditions2,Numsubjects,datsbycondition,AllFactors = ANOVA22BESASpatial(badsubjects,dataSet, anovadesign,conditions, starttime,endtime, preStimInterval,compTestPThresh,minClusterLength, numPerms,  regionNames,maxFDR,minClusterLengthSpatio)

                elif 'MNE' in MNEORBESA:

                    Multiple,Results, sigregion,AllRegionsLargestIndex, allRegions,ROISources,Allconditions2,Numsubjects,datsbycondition,AllFactors = ANOVA22BESASpatialMNETFCE(badsubjects,dataSet,anovadesign, conditions ,starttime,endtime, preStimInterval, numPerms,  regionNames,maxFDR)



            else:
                if 'BESA' in MNEORBESA:

                    Multiple,Results, sigregion,AllRegionsLargestIndex, allRegions,ROISources,Allconditions2,Numsubjects,datsbycondition,AllFactors,NumSubjs = ANOVA22BESASpatial(badsubjects,dataSet, anovadesign,conditions, starttime,endtime, preStimInterval,compTestPThresh,minClusterLength, numPerms,  regionNames,maxFDR,minClusterLengthSpatio)

                elif 'MNE' in MNEORBESA:

                    Multiple,Results, sigregion,AllRegionsLargestIndex, allRegions,ROISources,Allconditions2,Numsubjects,datsbycondition,AllFactors,NumSubjs = ANOVA22BESASpatialMNE(badsubjects,dataSet,anovadesign, conditions ,starttime,endtime, preStimInterval,compTestPThresh,minClusterLength, numPerms,  regionNames,maxFDR,minClusterLengthSpatio)


            datsbycondition1=datsbycondition

            resultsAll = Results

            #get conditions names
            #need to check of it is multiple ROI or just one
            a = resultsAll

            if Multiple  == 1:
                a = 1
                ind = 0
                from PyQt5 import QtCore, QtGui, QtWidgets
                from mainwindow import Ui_MainWindow
    
                Regionnames1 = []
                durations1 = []
                ids1=[]
                ps1=[]
                sigs1=[]
                tstarts1=[]
                tstops1=[]
                effects=[]
    
                sourcenum1=[]

                locations2=[]
                numOfSources = []
                locations = []
                FDRsig=[]
                l = len(resultsAll)#.__len__
                firstPlotDone = 0
                for ind in range(0, l):
    
                    CurrRegSources = ROISources[ind]
    
                    Regionnames = []
                    durations = []
                    ids=[]
                    ps=[]
                    sigs=[]
    
                    tstarts=[]
                    tstops=[]
    
                    AllRegionsLargestIndexCurr = AllRegionsLargestIndex[ind]
                    current = resultsAll[ind]
                    if current is dict:
                        test = 1
    
                    cluster_table = current.clusters.as_table()
    
    
    
                    resultsForPlot = resultsAll[ind]._default_plot_obj
    
    
                    #get number of conditions
                    ConditionsLength = len(Allconditions2)
                    offset = 0
                    conditionData = []
                    xData1 =[]
    
                    import numpy as np
                    datsbycondition = datsbycondition1[ind]
                    for legthC in range (0, ConditionsLength):
    
    
                        xData = []
                        conditionData = datsbycondition[offset:Numsubjects+offset]
                        #for subj in range(0,Numsubjects):
                            #condBySuj = conditionData[subj]
                            #condBySuj1 = np.mean(condBySuj.x, axis = 1)
                        condBySuj1 = np.mean(conditionData.x, axis = 0)
                        xData.append(condBySuj1)
                        # all conditions data means on subjects
                        #xData1.append(np.mean(xData, axis = 0))
                        xData1.append(xData)
                        offset = offset + Numsubjects
    
    
    
                    #Cond1 = resultsForPlot[0]
                    #Cond1Name = Cond1.name
                    #Cond2 = resultsForPlot[1]
                    #Cond2Name = Cond2.name
    
                    #cond1Data = Cond1.x
                    #cond2Data = Cond2.x
                    #XAxisVals = conditionData[0].dims # X AXIS Y AXIS THEN PLOT
                    XAxisVals = conditionData.dims
                    Startx = XAxisVals[1]
                    startx = (Startx.tmin)*1000
                    endx = (Startx.tmax)*1000
                    stepx = (Startx.tstep)*1000
                    name = Startx.name
                    nsamples = Startx.nsamples
    
    
    
                    ##############
    
                    #############
    
                    Results = resultsAll[ind].clusters
    
                    #main_widget = QWidget(mainwindow.Ui_MainWindow.dockPlot())
                    main_widget = QtWidgets.QDockWidget()
                    #main_widget = QtWidgets.QWidget()
    
    
                    if firstPlotDone == 0:
    
                        l = QVBoxLayout(main_widget)
                        sc = MyStaticMplCanvasANOVA(main_widget, width=5, height=4, dpi=100)
                        #dc = MyDynamicMplCanvas(main_widget, width=5, height=4, dpi=100)
                        #MyStaticMplCanvas.compute_initial_figure(main_widget)
    
    
                        #MyStaticMplCanvasANOVA.compute_initial_figure1(sc,startx,endx,stepx, xData1,Allconditions2)
                        MyStaticMplCanvasANOVA.compute_initial_figure(sc) #,startx,endx,stepx, xData1,Allconditions2, MNEBESA)
    
                        #MyStaticMplCanvas.compute_initial_figure1(sc,startx,endx,stepx,xData1, condition1Name,condition2Name)
                        l.addWidget(sc)
                        firstPlotDone = 1
    
    
    
    
                    #PLotWidget = QWidget()
                    #PLotWidget = l.widget()
    
                    #DockPlot = QDockWidget.create
                    #Ui_MainWindow.dockPlot
                    #Ui_MainWindow
                    #Ui_MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), l)
    
                    #main_widget.show()
    
    
                        #sc.cond1 = cond1Data
                        #sc.cond2 = cond2Data
                        sc.start = startx
                        sc.end = endx
                        sc.step = stepx
                        sc.xData1 = xData1
                        sc.AllConditions = Allconditions2
                        sc.Alldata = datsbycondition1
                        sc.allRegions = allRegions
                        sc.ROISources = ROISources
                        sc.numSubject = Numsubjects
                        sc.Sources = True
                        sc.Results = Results
    
                        sc.directory = dataSet
    
    
    
                    #Extract epoch time for x axis for each condition
    
                    #Extract y axis values
                    #print(Results.clusters)
                    #x = Results.clusters[1, 'cluster'].x
                    #d = Results.clusters[0, 'cluster'].any()
                    #data = {'ClusterID':['1','2','3'], 'n_sources':['4','5','6'], 'hemisphere':['7','8','9'],'Start Time':['7','8','9'],'End Time':['7','8','9'],'Duration':['7','8','9'],'P-value':['7','8','9']}
    
                    cluster = Results.get('cluster')
                    #len = Results._len_
                    duration = Results.get('duration')
    
                    for _len_ in duration:
    
                        durations.append(str(int(_len_*1000)))
    
                    index = 1
                    id = Results.get('id')
                    for _len_ in id:
                        #ids.append(str(_len_))
                        ids.append(str(index))
                        index = index +1
    
    
                    p = Results.get('p')
                    for _len_ in p:
                        ps.append(str(_len_))
    
                    sig = Results.get('sig')
                    tstop = Results.get('tstop')
                    for _len_ in sig:
                        sigs.append(str(_len_))
    
    
    
                    tstart = Results.get('tstart')
                    for _len_ in tstart:
                        tstarts.append(str(int(_len_*1000)))
    
    
    
                    for _len_ in tstop:
                        tstops.append(str(int(_len_*1000)))
                        allRegions = list(allRegions)
                        name = allRegions[ind]
                        name = name.replace('[', '')
                        Regionnames.append(name)
    
                    v = Results.get('v')
    
    
    
                        #get header
                    index = 0
                    for i in range(0,len(Regionnames1)):
                        #ids.append(str(_len_))
                        #FDRsig.append(str(sigregion))
                        #allRegions = list(allRegions)
                        name = Regionnames1[i]
                        name = name.replace('[', '')
                        if name in sig:
                            FDRsig.append(str('Sig after FDR'))
                        else:
                            FDRsig.append(str('no sig after FDR'))
    
                    id = []
                    sourcemin=[]
                    sourcemax=[]
                    tstart = []
                    tstop = []
                    duration = []
                    v= []
                    p=[]
                    sig=[]
                    effect=[]
    
    
                    v = Results.get('v')
    
                    data = cluster_table
                    eff = Results.get('effect')
                    for ll in eff:
                        effects.append(ll)
    
                    for _len_ in tstop:
                        tstops.append(str(int(_len_*1000)))
                        allRegions = allRegions
                        name = allRegions
    
                        Regionnames.append(name)
    
    
                    sourcenum = Results.get('n_sources')
    
                    sourcenum1=[]
    
                    for s1 in sourcenum:
                        sourcenum1.append(str(s1))
    
                    sourcenum = Results.get('n_sources')
    
                    locations1 = Results.get('location')
                    AllRegionsLargestIndexCurr = 0
                    if AllRegionsLargestIndexCurr > 0:
    
                        #get length of the clusters by effects and then print in for loop
                        #AllRegionsLargestIndexCurr=AllRegionsLargestIndexCurr[0]
                        ClusterByEffectLength = len(AllRegionsLargestIndexCurr)
    
                        for effIndex in range(0,ClusterByEffectLength):
    
                            IndexCurr = AllRegionsLargestIndexCurr[effIndex].get('LargestIndexByEffect', None)
                            IndexCurr=int(IndexCurr)
                            effects.append(AllRegionsLargestIndexCurr[effIndex].get('effect', None))
                            Regionnames1.append(Regionnames[IndexCurr])
                            sourcenum1.append(str(sourcenum[IndexCurr]))
                            locations2.append(locations1[IndexCurr])
                            ids1.append(ids[IndexCurr])
                            durations1.append(durations[IndexCurr])
                            tstarts1.append(tstarts[IndexCurr])
                            tstops1.append(tstops[IndexCurr])
                            ps1.append(ps[IndexCurr])
                            sigs1.append(sigs[IndexCurr])
                            #FDRsig.append(str(1))
    
                    else:
    
                        effects = effects
                        Regionnames1 = Regionnames
                        sourcenum1 = sourcenum1
    
                        locations2=locations1
                        ids1= ids
                        durations1 =durations
                        tstarts1 = tstarts
                        tstops1 = tstops
                        ps1 = ps
                        sigs1 = sigs
    

    
                data = {'0 Region Name':Regionnames1,'1 ClusterID':ids1, '12 effects':effects, '13 Number of sources':sourcenum1,'14 Locations':locations2,'2 Duration':durations1, '3 Start time':tstarts1,'4 End Time':tstops1, '5 P-value': ps1,'6 Sig':sigs1} #,'7 FDR sig': FDRsig} #,'Duration':['7','8','9'],'P-value':['7','8','9']}
    
    
                table = MyTableANOVA(sc,data,ROISources, MNEORBESA,len(durations1),10)#,startx,endx,stepx,cond1Data,cond2Data)
    
    
                import csv
    
                #### Save to file in the current directory
    
                # write it
                #with open(directory+'test_file.csv', 'w') as csvfile:
                #    writer = csv.writer(csvfile)
                #    [writer.writerow(r) for r in table]
    
                #f = open(directory+"output.html", 'w')
                #f.write("<html><table>")
                #for row in data:
                #    f.write("<tr><td>"+"</td><td>".join(row)+"</td></tr>")
                #f.write("</table></html>")
                #f.close()
    
    
                condition2Name = 'test'
                import re
                import datetime
    
                now = datetime.datetime.now()
                path1 = dataSet+'/'+AllFactors+str(now)+'_SpatialAnalysisResults.csv'
                #with open(directory+'/'+condition1Name+'_'+condition2Name+str(now)+'_Results.csv', 'wb') as f:  # This creates the file object for the context
                                      # below it and closes the file automatically
                l = []
                l1=[]
                DictData = []
                #writer = csv.writer(f)
    
                tt = data.iteritems()
                for k, v in data.iteritems(): # Iterate over items returning key, value tuples
                        newK = str(k)
                        newK = newK.replace(')','')
                        newK = newK.replace('(','')
    
                        l1.append('%s: ' % (newK))
                        DictData.append('%s: ' % (newK))
                        #l1.append('%s: ' % (str(v)))
                        #f.write(', '.join(l1))
                        #writer.writerow(k)
    
    
                        for item in v:
                            newItem = str(item)
                            newItem = newItem.replace(')','')
                            newItem = newItem.replace('(','')
    
                            l1.append('%s' % ( newItem)) # Build a nice list of strings
                        #  writer.writerow(zip(v))
                          #f.write(', '.join(l))
                        #
                          #f.write(item)
                            #writer.writerow(zip(l1))
                            l1=[]
                indexCol = 0
                DictData = sorted(DictData)
                with open(unicode(path1), 'wb') as stream:
    
                    writer = csv.writer(stream)
                    writer.writerow(DictData)
                    for row in range(table.rowCount()):
                        rowdata = []
                        for column in range(table.columnCount()):
                            item = table.item(row, column)
                            if item is not None:
    
                                rowdata.append(
                                    unicode(item.text()).encode('utf8'))
                            else:
                                rowdata.append('')
                            indexCol +=1
                        writer.writerow(rowdata)
    
    
    
               #### TODO fix the layout of the csv
             
 
                table.show()
    
    
    
    
    


            else:

                Results = Results[0]
    
                cluster_table = Results.clusters.as_table()
    
                resultsForPlot = Results._default_plot_obj
    
                ConditionsLength = len(Allconditions2)
                offset = 0
                conditionData = []
                xData1 =[]
    
                import numpy as np
                datsbycondition = datsbycondition1
                for legthC in range (0, ConditionsLength):
    
    
                        xData = []
                        conditionData = datsbycondition[offset:Numsubjects+offset]
                        #for subj in range(0,Numsubjects):
                            #condBySuj = conditionData[subj]
                            #condBySuj1 = np.mean(condBySuj.x, axis = 1)
                        conditionData=conditionData #[0]
                        condBySuj1 = np.mean(conditionData.x, axis = 0)
                        xData.append(condBySuj1)
                        # all conditions data means on subjects
                        #xData1.append(np.mean(xData, axis = 0))
                        xData1.append(xData)
                        offset = offset + Numsubjects
    
    
    
                    #Cond1 = resultsForPlot[0]
                    #Cond1Name = Cond1.name
                    #Cond2 = resultsForPlot[1]
                    #Cond2Name = Cond2.name
    
                    #cond1Data = Cond1.x
                    #cond2Data = Cond2.x
                    #XAxisVals = conditionData[0].dims # X AXIS Y AXIS THEN PLOT
                XAxisVals = conditionData.dims
                Startx = XAxisVals[2]
                startx = (Startx.tmin)*1000
                endx = (Startx.tmax)*1000
                stepx = (Startx.tstep)*1000
                name = Startx.name
                nsamples = Startx.nsamples
    
    
    
                from PyQt5 import QtCore, QtGui, QtWidgets
                from mainwindow import Ui_MainWindow
    
                ##############
                import datetime
    
                now = datetime.datetime.now()
                #############
    
                Results = Results.clusters
    
                #main_widget = QWidget(mainwindow.Ui_MainWindow.dockPlot())
                main_widget = QtWidgets.QDockWidget()
                #main_widget = QtWidgets.QWidget()
    
    
                l = QVBoxLayout(main_widget)
                sc = MyStaticMplCanvasANOVA(main_widget, width=5, height=4, dpi=100)
                #dc = MyDynamicMplCanvas(main_widget, width=5, height=4, dpi=100)
                #MyStaticMplCanvas.compute_initial_figure(main_widget)
                MyStaticMplCanvasANOVA.compute_initial_figure(sc)
                #MyStaticMplCanvasANOVA.compute_initial_figure1(sc,startx,endx,stepx, xData1,Allconditions2)
                l.addWidget(sc)
    
                a = 1
                ind = 0
                from PyQt5 import QtCore, QtGui, QtWidgets
                from mainwindow import Ui_MainWindow
    
                Regionnames1 = []
                durations1 = []
                effects = []
                ids1=[]
                ps1=[]
                sigs1=[]
                tstarts1=[]
                tstops1=[]
                effects=[]
                sourcenum = []
                locations1=[]
                l =  1 #len(resultsAll)#.__len__
                firstPlotDone = 0
                for ind in range(0, l):
    
                    Regionnames = []
                    durations = []
                    ids=[]
                    ps=[]
                    sigs=[]
                    tstarts=[]
                    tstops=[]
                    FDRsig=[]
                    AllRegionsLargestIndexCurr = AllRegionsLargestIndex#[ind]
                    current = resultsAll[0]
                    if current is dict:
                        test = 1
    
                    cluster_table = current.clusters.as_table()
                    resultsAll = resultsAll[0]
                    resultsForPlot = resultsAll._default_plot_obj
    
                    #Cond1 = resultsForPlot[0]
                    #Cond1Name = Cond1.name
                    #Cond2 = resultsForPlot[1]
                    #Cond2Name = Cond2.name
    
                    #cond1Data = Cond1.x
                    #cond2Data = Cond2.x
                    #XAxisVals = Cond1.dims # X AXIS Y AXIS THEN PLOT
                    #Startx = XAxisVals[0]
                    #startx = (Startx.tmin)*1000
                    #endx = (Startx.tmax)*1000
                    #stepx = (Startx.tstep)*1000
                    #name = Startx.name
                    #nsamples = Startx.nsamples
    
    
    
                    ##############
    
                    #############
    
                    Results = resultsAll.clusters
    
                    #main_widget = QWidget(mainwindow.Ui_MainWindow.dockPlot())
                    main_widget = QtWidgets.QDockWidget()
                    #main_widget = QtWidgets.QWidget()
    
    
                    if firstPlotDone == 0:
    
                        l = QVBoxLayout(main_widget)
                        sc = MyStaticMplCanvasANOVA(main_widget, width=5, height=4, dpi=100)
                        #dc = MyDynamicMplCanvas(main_widget, width=5, height=4, dpi=100)
                        #MyStaticMplCanvas.compute_initial_figure(main_widget)
    
                        #MyStaticMplCanvasANOVA.compute_initial_figure1(sc,startx,endx,stepx, xData1,Allconditions2, MNEBESA)
                        MyStaticMplCanvasANOVA.compute_initial_figure(sc) #,startx,endx,stepx, xData1,Allconditions2, MNEBESA)
    
                        l.addWidget(sc)
                        firstPlotDone = 1
    
    
                    #PlotBESABrain(ROISources)
    
                    #PLotWidget = QWidget()
                    #PLotWidget = l.widget()
    
                    #DockPlot = QDockWidget.create
                    #Ui_MainWindow.dockPlot
                    #Ui_MainWindow
                    #Ui_MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), l)
    
                    #main_widget.show()
    
    
                        #sc.cond1 = cond1Data
                        #sc.cond2 = cond2Data
                        #sc.start = startx
                        #sc.end = endx
                        #sc.step = stepx
    
                        sc.start = startx
                        sc.end = endx
                        sc.step = stepx
                        sc.xData1 = xData1
                        sc.AllConditions = Allconditions2
                        sc.Alldata = datsbycondition1
                        sc.allRegions = allRegions
                        sc.ROISources = ROISources
                        sc.numSubject = Numsubjects
                        sc.Sources = True
                        sc.Results = Results
    
                        sc.directory = dataSet
    
    
    
    
    
    
                    cluster = Results.get('cluster')
                    #len = Results._len_
                    duration = Results.get('duration')
    
                    for _len_ in duration:
    
                        durations.append(str(int(_len_*1000)))
    
                    index = 1
                    id = Results.get('id')
                    for _len_ in id:
                        #ids.append(str(_len_))
                        ids.append(str(index))
                        index = index +1
    
    
                    p = Results.get('p')
                    for _len_ in p:
                        ps.append(str(_len_))
    
                    sig = Results.get('sig')
                    for _len_ in sig:
                        sigs.append(str(_len_))
    
                    tstart = Results.get('tstart')
                    for _len_ in tstart:
                        tstarts.append(str(int(_len_*1000)))
    
                    tstop = Results.get('tstop')
                    eff = Results.get('effect')
    
                    for ll in eff:
                        effects.append(ll)
    
                    for _len_ in tstop:
                        tstops.append(str(int(_len_*1000)))
                        allRegions = allRegions
                        name = allRegions
    
                        Regionnames.append(name)
    
    
                    sourcenum = Results.get('n_sources')
    
                    sourcenum1=[]
    
                    for s1 in sourcenum:
                        sourcenum1.append(str(s1))
    
    
                    locations1 = Results.get('location')
                    locations2=[]
                    v = Results.get('v')
    
                    AllRegionsLargestIndexCurr = -1
    
                    if AllRegionsLargestIndexCurr > -1:
    
                        #get length of the clusters by effects and then print in for loop
                        AllRegionsLargestIndexCurr=AllRegionsLargestIndexCurr[0]
                        ClusterByEffectLength = len(AllRegionsLargestIndexCurr)
    
                        for effIndex in range(0,ClusterByEffectLength):
    
                            IndexCurr = AllRegionsLargestIndexCurr[effIndex].get('LargestIndexByEffect', None)
                            IndexCurr = int(IndexCurr)
                            effects.append(AllRegionsLargestIndexCurr[effIndex].get('effect', None))
                            Regionnames1.append(Regionnames[IndexCurr])
                            sourcenum1.append(str(sourcenum[IndexCurr]))
    
                            locations2.append(locations1[IndexCurr])
                            ids1.append(ids[IndexCurr])
                            durations1.append(durations[IndexCurr])
                            tstarts1.append(tstarts[IndexCurr])
                            tstops1.append(tstops[IndexCurr])
                            ps1.append(ps[IndexCurr])
                            sigs1.append(sigs[IndexCurr])
                            #FDRsig.append(str(1))
                    else:
    
                        effects = effects
                        Regionnames1 = Regionnames
                        sourcenum1 = sourcenum1
    
                        locations2=locations1
                        ids1= ids
                        durations1 =durations
                        tstarts1 = tstarts
                        tstops1 = tstops
                        ps1 = ps
                        sigs1 = sigs
    
    
    
                    #for _len_ in id:
                        #ids.append(str(_len_))
                    #    FDRsig.append(str(1))
                    #    index = index +1
    
                data = {'0 Region Name':Regionnames1,'1 ClusterID':ids1, '12 effects':effects, '13 Number of sources':sourcenum1,'14 Locations':locations2,'2 Duration':durations1, '3 Start time':tstarts1,'4 End Time':tstops1, '5 P-value': ps1,'6 Sig':sigs1} #,'7 FDR sig': FDRsig} #,'Duration':['7','8','9'],'P-value':['7','8','9']}
    
    
                table = MyTableANOVA(sc,data,ROISources, MNEORBESA,len(durations1),10)#,startx,endx,stepx,cond1Data,cond2Data)
    
    
    
 
                import csv
                import re
                path1 = dataSet+'/'+AllFactors+str(now)+'_SpatialAnalysisResults.csv'
                #with open(directory+'/'+condition1Name+'_'+condition2Name+str(now)+'_Results.csv', 'wb') as f:  # This creates the file object for the context
                                      # below it and closes the file automatically
                l = []
                l1=[]
                DictData = []
                #writer = csv.writer(f)
    
                tt = data.iteritems()
                for k, v in data.iteritems(): # Iterate over items returning key, value tuples
                        newK = str(k)
                        newK = newK.replace(')','')
                        newK = newK.replace('(','')
    
                        l1.append('%s: ' % (newK))
                        DictData.append('%s: ' % (newK))
                        #l1.append('%s: ' % (str(v)))
                        #f.write(', '.join(l1))
                        #writer.writerow(k)
    
    
                        for item in v:
                            newItem = str(item)
                            newItem = newItem.replace(')','')
                            newItem = newItem.replace('(','')
    
                            l1.append('%s' % ( newItem)) # Build a nice list of strings
                        #  writer.writerow(zip(v))
                          #f.write(', '.join(l))
                        #
                          #f.write(item)
                            #writer.writerow(zip(l1))
                            l1=[]
                indexCol = 0
                DictData = sorted(DictData)
                with open(unicode(path1), 'wb') as stream:
    
                    writer = csv.writer(stream)
                    writer.writerow(DictData)
                    for row in range(table.rowCount()):
                        rowdata = []
                        for column in range(table.columnCount()):
                            item = table.item(row, column)
                            if item is not None:
    
                                rowdata.append(
                                    unicode(item.text()).encode('utf8'))
                            else:
                                rowdata.append('')
                            indexCol +=1
                        writer.writerow(rowdata)
    
    
             
    
                table.show()
        


    return table