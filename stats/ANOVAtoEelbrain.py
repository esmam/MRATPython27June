
# function for ANOVA this functions passes parameters to the main anova function in eelbrain


import os
import os
from  eelbrain import *
import scipy.io
import string
#from TestTabel import *
import itertools
import eelbrain as e
from PyQt5.QtWidgets import *


def ANOVA22BESASpatial(root, condition1Name, condition2Name, startTime, endTime, presTim, PThresh,
                              minTemporalCluster, numPerm, anlsysTail, ROI):


    dat_files = []
    conditions = []
    subjects = []
    Allconditions = []
    completed = 0
    ROI = 'leftba21+leftba20'
    root = '/Users/esmamansouri/Documents/Data/Adina_AG'
    for condition in ['sat_ev_lorel', 'sat_ev_hirel','sat_no_ev_lorel', 'sat_no_ev_hirel']:

        for name in os.listdir(root + '/' + condition):
            if 'dat' in name:
                dat = load.besa.dat_file(root + '/' + condition + '/' + name)
                dat_files.append(dat)
                conditions.append(condition)
                subjects.append(name[:5])
        Allconditions.append(condition)


    Allconditions1 = Factor(Allconditions, tile=len(subjects)/len(Allconditions))

    subjects.sort()
    #conditions.sort()

    ds = Dataset()
    #ds = Dataset((('subject', Factor(subjects)), ('conditions', Factor(conditions)),('dat',combine(dat_files[5:]))))
    ds['subject'] = Factor(subjects)
    ds['conditions'] = Factor(Allconditions1)
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

    #A = Factor(range(2), repeat=42, name='A')
    #B = Factor(range(2), repeat=42, name='B')

    '''Enter the data for the first level of f1, and the first level of f2.

    Enter the data for the first level of f1, and the second level of f2.

    Enter the data for the second level of f1, and the first level of f2.

    Enter the data for the second level of f1, and the second level of f2.

    ['sat_ev_lorel', 'sat_ev_hirel','sat_no_ev_lorel', 'sat_no_ev_hirel']:'''
    subject = ds['subject']
    A = ds['conditions'] #Factor('abc', 'A', repeat=7)
    A = Factor(['ev', 'no_ev'], repeat = len(subjects)/(len(Allconditions)/2))

    B = Factor(['lorel', 'hirel'], tile = len(subjects)/(len(Allconditions)/2)) #4)
    ds['EvType'] = A
    ds['LowHigh'] = B
    #subjects = ['R0374', 'R0374', 'R0374', 'R0374', 'R0411', 'R0411', 'R0411', 'R0411']

    '''dss = []
    ds = Dataset()
    for subject in subjects:

	    ds['subject'] = ds['subject'].append(Factor([subject,subject,subject,subject], name = 'subject'))
	    ds['EvType'] = ds['EvType'].append(Factor(['ev','ev','no_ev','no_ev'], name = 'EvType'))
	    ds['LowHigh'] = ds['LowHigh'].append(Factor(['lorel','hirel','lorel','hirel'], name = 'LowHigh'))
	    ds['Condition'] = ds['Condition'].append(Factor(['sat_ev_lorel', 'sat_ev_hirel','sat_no_ev_lorel', 'sat_no_ev_hirel'], name ='Condition'))

    dss.append(ds)

    ds = combine((dss))'''
    a = 1
    Results = testnd.anova(y, 'EvType*LowHigh', sub=None, ds=ds, samples=10, pmin=.3, fmin=None, minsource=3, mintime=.02, tfce=False, tstart=.1, tstop=.5, match='subject')
    a= 1
    cluster_table = Results.clusters.as_table()

    print(cluster_table)
    #QMessageBox.about(None, 'Data extraction complete, now running the statistical test','Analysis Complete Results are displayed in the main window')




    #plot.UTSClusters(Results, title="Random Effects Model")
    #Results_table = cluster_table


    return Results


#if __name__ == '__main__':

#   results = ANOVA22BESASpatial('root', 'condition1Name', 'condition2Name', 'startTime', 'endTime', 'presTim', 'PThresh',
#                             'minTemporalCluster', 'numPerm', 'anlsysTail', 'ROI')

