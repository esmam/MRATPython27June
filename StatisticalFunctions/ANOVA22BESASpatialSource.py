__author__ = 'esmab'
# function for ANOVA this functions passes parameters to the main anova function in eelbrain


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


def ANOVA22BESASpatial(root, condition1Name, condition2Name, startTime, endTime, presTim, PThresh,
                              minTemporalCluster, numPerm, anlsysTail, ROI):


    dat_files = []
    conditions = []
    subjects = []
    completed = 0
    ROI = 'leftba21+leftba20'
    root = '/Users/esmab/Documents/MATLAB_SCRIPTS/Data/Adina_AGcopy'
    for condition in ['mod_ev_lorel', 'sat_no_ev_hirel','sat_ev_lorel', 'sat_ev_hirel']:

        for name in os.listdir(root + '/' + condition):
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
    #FOR TEMPRAL ONLY
    #y = ds['dat'].sub(source=ROISources).mean('source')
    #print( table.frequencies('conditions', 'subject', ds=ds))
    y = ds['dat']



    t = table.frequencies('conditions', 'subject', ds=ds)
    anlsysTail = 'both'
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
   # Results = testnd.ttest_rel(y, 'conditions', match='subject', tail=0,ds=ds, tstart=(int(startTime)+int(presTim))/1000, tstop=(int(endTime)+int(presTim))/1000, samples=int(numPerm), pmin=float(PThresh), mintime = int(minTemporalCluster)/1000)

    A = Factor([1, 0], repeat=3 * 8, name='A')
    B = Factor(range(3), tile=2, repeat=8, name='B')
    B = ds['subject']
    A = ds['conditions'] #Factor('abc', 'A', repeat=7)

    Results = testnd.anova(y, 'A*B'*ds['subject'] , sub=None, ds=ds, samples=10, pmin=.05, fmin=None, tfce=False, tstart=.1, tstop=.5, match='subject')


    #test.anova(timecourse, ‘factorname*factorname*subject’, ds=ds,match=‘subject’, samples = 10000, pmin=0.05, tstart=0.1, tstop=0.25,mintime=0.02, group=‘groupname’)!

    QMessageBox.about(None, 'Data extraction complete, now running the statistical test','Analysis Complete Results are displayed in the main window')




    #plot.UTSClusters(Results, title="Random Effects Model")
    #Results_table = cluster_table


    return Results


if __name__ == '__main__':

    results = ANOVA22BESASpatial('root', 'condition1Name', 'condition2Name', 'startTime', 'endTime', 'presTim', 'PThresh',
                              'minTemporalCluster', 'numPerm', 'anlsysTail', 'ROI')

