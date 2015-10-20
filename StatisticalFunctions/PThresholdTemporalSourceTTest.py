__author__ = 'esmab'
# this function performs a source t-test temporal analysis with a Pthreshold .
import os
import os
from  eelbrain import *
import scipy.io
import string
from TestTabel import *
import itertools
import eelbrain as e
from PyQt5.QtWidgets import (QWidget, QProgressBar,QFileDialog,
    QPushButton, QApplication)


def PThresholdTempSourceTTest(root, condition1Name, condition2Name, startTime, endTime, presTim, PThresh,
                              minTemporalCluster, numPerm, anlsysTail, ROI):


    dat_files = []
    conditions = []
    subjects = []
    completed = 0
    for condition in [condition1Name, condition2Name]:

        for name in os.listdir(root + '/' + condition):
            if 'dat' in name:
                dat = load.besa.dat_file(root + '/' + condition + '/' + name)
                dat_files.append(dat)
                conditions.append(condition)
                subjects.append(name[:5])





    ds = Dataset()
    #ds = Dataset((('subject', Factor(subjects)), ('conditions', Factor(conditions)),('dat',combine(dat_files[5:]))))
    ds['subject'] = Factor(subjects)
    ds['conditions'] = Factor(conditions)
    #test = Factor(subjects)
    #ds['subject'] = Factor(subjects)
    ROIValues = ROI

    # open mat file to search for sources

    RegionNamesOldBESA = scipy.io.loadmat('regionnamesOldBESA.mat')
    RegionNames = ['leftba1-3','leftba4','leftba5','leftba6','leftba7','leftba8','leftba9','leftba10','leftba11','leftba17','leftba18','leftba19','leftba20'
    ,'leftba21','leftba22','leftba28','leftba36','leftba37','leftba38','leftba39','leftba40','leftba42','leftba44-45','leftba46'
    'leftba47','leftcerebellartonsil','rightba1-3','rightba4','rightba5','rightba6','rightba7','rightba8','rightba9','rightba10','rightba11'
    ,'rightba17','rightba18','rightba19','rightba20','rightba21','rightba22','rightba28','rightba36','rightba37','rightba38','rightba39'
    'rightba40','rightba42','rightba44-45','rightba46','rightba47','rightcerebellartonsil']

    SourceObjectBESA = scipy.io.loadmat('sourcesOldBESA.mat')
    RegionSourcesListAll = []
    rois = []
    #split regions to get sources
    if ROIValues.find('/') != -1 :
        with open(ROIValues) as f:
            rois = f.readlines()
            ROIValues = rois[0]



    rois =   ROIValues.split('+')

    for roi in rois:



        ROIIndex = RegionNames.index(roi)

        RegionSources = SourceObjectBESA.get('test2')[ROIIndex]
        RegionSources = RegionSources[0]

    #a = SourceObjectBesa[0:1]['analysisRegion']



        RegionSourcesList = RegionSources.tolist()

        RegionSourcesListAll.append( RegionSourcesList[0])



    ROISources = list(itertools.chain(*RegionSourcesListAll))
    ds['dat'] = combine(dat_files)  #[5:])

    #print ( ds[:5])
    #ds['dat']
    #dat_files[0]
    #test = ds['dat'].get('source')


    #get sources from roi file
    tails = 0
    y = ds['dat'].sub(source=ROISources).mean('source')
    #print( table.frequencies('conditions', 'subject', ds=ds))
    #y = ds['dat']
    t = table.frequencies('conditions', 'subject', ds=ds)
    if anlsysTail == 'both':
        tails = 0
    elif anlsysTail == 'right':
        tails = 1

    elif anlsysTail == 'left':
        tails = -1


    #QMessageBox.about(None, 'Data extraction complete, now running the statistical test','Analysis Complete Results are displayed in the main window')
    '''completed = 0
    Results = ""
    while completed< 100:

        completed += 0.0001
        progress.setValue(completed)

        progress.value = completed
        progress.isTextVisible = "True"
    '''


    tstart1=float(startTime)/1000
    tstop1=float(endTime)/1000

    ## get results for each region if multiple regions
    Results = testnd.ttest_rel(y, 'conditions', match='subject', tail=0,ds=ds, tstart=tstart1, tstop=tstop1, samples=int(numPerm), pmin=float(PThresh), mintime = int(minTemporalCluster)/1000)

    QMessageBox.about(None, 'Data extraction complete, now running the statistical test','Analysis Complete Results are displayed in the main window')




    #plot.UTSClusters(Results, title="Random Effects Model")
    #Results_table = cluster_table


    return Results

