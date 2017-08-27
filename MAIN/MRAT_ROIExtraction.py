import sys
import os
import os
from  eelbrain import *
import scipy.io
import string
from TestTabel import *
import itertools
import eelbrain as e
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

def MRAT_ROIExtration(ROI):
        #Extract ROI BESA
    ROIValues = ROI

    ROIValues1 = ''

    if getattr(sys, 'frozen', False):
        application_path = os.path.dirname(sys.executable)

        print(application_path)
    elif __file__:
        application_path = os.path.dirname(__file__)

        application_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '.', ''))





    # open mat file to search for sources

    #RegionNamesOldBESA = scipy.io.loadmat('regionnamesOldBESA.mat')
    #RegionNameBESA = str(RegionNamesOldBESA)
    RegionNames = ['leftba1-3','leftba4','leftba5','leftba6','leftba7','leftba8','leftba9','leftba10','leftba11','leftba17','leftba18','leftba19','leftba20'
    ,'leftba21','leftba22','leftba28','leftba36','leftba37','leftba38','leftba39','leftba40','leftba42','leftba44-45','leftba46'
    'leftba47','leftcerebellartonsil','rightba1-3','rightba4','rightba5','rightba6','rightba7','rightba8','rightba9','rightba10','rightba11'
    ,'rightba17','rightba18','rightba19','rightba20','rightba21','rightba22','rightba28','rightba36','rightba37','rightba38','rightba39'
    'rightba40','rightba42','rightba44-45','rightba46','rightba47','rightcerebellartonsil']

    #multiple regions comparisions
    SourceObjectBESA = scipy.io.loadmat(application_path+'/sourcesOldBESA.mat')
    SourceObjectBESANew = scipy.io.loadmat(application_path+'/matlabBESANEw.mat') #sources.mat')
    SourceObjectBESA = SourceObjectBESANew
    RegionSourcesListAll = []
    RegionSourcesListMultiple = []
    #IF ROI IS A FILE
    ROIValues2 = []
    if ROIValues.find('/') != -1 :
        with open(ROIValues) as f:
            rois = f.readlines()
            ROIValues1 = rois#[0]

            ROIValues = ROIValues1
            for r in ROIValues:
                r = r.strip()
                ROIValues2.append(r)
            ROIValues = ROIValues2
        for roi in ROIValues:
            if roi.find('+') != -1 :
                #if it is combined region
                roi = rois
                rois = ROIValues.split('+')

                for roi in rois:



                    ROIIndex = RegionNames.index(roi)

                    #RegionSources = SourceObjectBESA.get('test2')[ROIIndex]
                    RegionSources = SourceObjectBESA.get('a')[ROIIndex]
                    RegionSources = RegionSources[0]

                    #a = SourceObjectBesa[0:1]['analysisRegion']



                    RegionSourcesList = RegionSources.tolist()

                    RegionSourcesListAll.append( RegionSourcesList[0])



                ROISources = list(itertools.chain(*RegionSourcesListAll))
            else:

                ROIIndex = RegionNames.index(roi)

                        #RegionSources = SourceObjectBESA.get('test2')[ROIIndex]
                RegionSources = SourceObjectBESANew.get('a')[ROIIndex]
                RegionSources = RegionSources[0]

                        #a = SourceObjectBesa[0:1]['analysisRegion']

                RegSource = RegionSources.tolist()

                RegionSourcesListMultiple.append(RegSource[0])


                #RegionSourcesListAll.append( RegionSourcesList[0])

        ROISources = RegionSourcesListMultiple
    else:
        if ROI == 'whole brain Multiple Regions':
            for reg in RegionNames:
                ROIValues1 +=reg
                ROIValues1 +=','
            ROIValues = ROIValues1
            ROIValues = ROIValues[:-1]

        elif ROI == 'whole brain':
            for reg in RegionNames:
                ROIValues1 += reg
                #ROIValues1.append('+')
                ROIValues1 += '+'
            ROIValues = ROIValues1
            ROIValues = ROIValues[:-1]

        rois = []

        #split regions to get sources



        index = 0
        # if Roi values are multiple regions separated by ,
        #n = ROIValues.count(',')
        #RegionSourcesListMultiple = np.empty((n+1, 0)).tolist()
        RegionSourcesListMultiple = []
        if ROIValues.find(',') != -1 :
            MultipleRegion = ROIValues.split(',')
            for roi in MultipleRegion:



                ROIIndex = RegionNames.index(roi)

                #RegionSources = SourceObjectBESA.get('test2')[ROIIndex]
                RegionSources = SourceObjectBESANew.get('a')[ROIIndex]
                RegionSources = RegionSources[0]

                #a = SourceObjectBesa[0:1]['analysisRegion']

                RegSource = RegionSources.tolist()
                RegSource = RegSource[0]
                RegSource[:] = [x - 1 for x in RegSource]
                RegionSourcesListMultiple.append(RegSource)


                #RegionSourcesListAll.append( RegionSourcesList[0])

            ROISources = RegionSourcesListMultiple
        else:

            # if combined region

            rois = ROIValues.split('+')

            for roi in rois:



                ROIIndex = RegionNames.index(roi)

                #RegionSources = SourceObjectBESA.get('test2')[ROIIndex]
                RegionSources = SourceObjectBESANew.get('a')[ROIIndex]
                RegionSources = RegionSources[0]

                #a = SourceObjectBesa[0:1]['analysisRegion']



                RegionSourcesList = RegionSources.tolist()

                RegionSourcesListAll.append( RegionSourcesList[0])



            ROISources = list(itertools.chain(*RegionSourcesListAll))
            ROISources[:] = [x - 1 for x in ROISources]
    return ROISources,ROIValues