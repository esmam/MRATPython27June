import sys
import os
import os
from  eelbrain import *
import scipy.io
import string
from TestTabel import *
import itertools
import eelbrain as e
import mne




def MRAT_ROIExtrationMNE(ROI):
        #Extract ROI BESA
    ROIValues = ROI

    ROIValues1 = ''

    if getattr(sys, 'frozen', False):
        application_path = os.path.dirname(sys.executable)

        print(application_path)
    elif __file__:
        application_path = os.path.dirname(__file__)

        application_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', ''))



    # open mat file to search for sources
    print(application_path)
    #RegionNamesOldBESA = scipy.io.loadmat('regionnamesOldBESA.mat')
    #RegionNameBESA = str(RegionNamesOldBESA)
    RegionNames = ['leftamygdala','leftanteriorcomissure','leftanteriornucleus','leftba1','leftba2','leftba3',
                   'leftba4','leftba5','leftba6','leftba7','leftba8','leftba9','leftba10','leftba11',
                   'leftba13','leftba17','leftba18','leftba19','leftba20','leftba21','leftba22','leftba23','leftba25',
                   'leftba26','leftba27','leftba28','leftba29','leftba30','leftba31','leftba32','leftba33','leftba34','leftba35','leftba36','leftba37',
                   'leftba38','leftba39','leftba40','leftba41','leftba42','leftba43','leftba44','leftba45','leftba46','leftba47',
                    'leftcaudatehead','leftcaudatetail','leftcorpuscallosum','leftcullmen','lefthippocampus',
                   'lefthypothalamus','leftmammillarybody','leftmedialdorsalnucleus','leftoptictract',
                   'leftpulvinar','leftputamen','rightanteriorcommissure','rightanteriornucleus','rightba1','rightba2','rightba3',
                   'rightba4','rightba5','rightba6','rightba7','rightba8','rightba9','rightba10','rightba11','rightba13','rightba17','rightba18',
                   'rightba19','rightba20','rightba21','rightba22','rightba23','rightba24','rightba25','rightba26','rightba27','rightba28','rightba29',
                   'rightba30','rightba31','rightba32','rightba33','rightba34','rightba35','rightba36','rightba37','rightba38','rightba39','rightba40',
                   'rightba41','rightba42','rightba43','rightba44','rightba45','rightba46','rightba47',
                   'rightbrodmannarea','rightcaudatebody','rightcaudatehead','rightcaudatetail','rightcorpuscallosum','rightculmen',
                   'righthippocampus','righthypothalamus','rightmammillarybody','rightopticaltract','rightpulvinar','rightputamen']

    LeftHemisphere = ['leftamygdala','leftanteriorcomissure','leftanteriornucleus','leftba1','leftba2','leftba3',
                   'leftba4','leftba5','leftba6','leftba7','leftba8','leftba9','leftba10','leftba11',
                   'leftba13','leftba17','leftba18','leftba19','leftba20','leftba21','leftba22','leftba23','leftba25',
                   'leftba26','leftba27','leftba28','leftba29','leftba30','leftba31','leftba32','leftba33','leftba34','leftba35','leftba36','leftba37',
                   'leftba38','leftba39','leftba40','leftba41','leftba42','leftba43','leftba44','leftba45','leftba46','leftba47',
                    'leftcaudatehead','leftcaudatetail','leftcorpuscallosum','leftcullmen','lefthippocampus',
                   'lefthypothalamus','leftmammillarybody','leftmedialdorsalnucleus','leftoptictract','leftpulvinar','leftputamen']

    lefthemisphereWhole = 'leftamygdala+leftanteriorcomissure+leftanteriornucleus+leftba1+leftba2+leftba3+leftba4+leftba5+leftba6+leftba7+leftba8+leftba9+leftba10+leftba11+leftba13+leftba17+leftba18+leftba19+leftba20+leftba21+leftba22+leftba23+leftba25+leftba26+leftba27+leftba28+leftba29+leftba30+leftba31+leftba32+leftba33+leftba34+leftba35+leftba36+leftba37+leftba38+leftba39+leftba40+leftba41+leftba42+leftba43+leftba44+leftba45+leftba46+leftba47+leftcaudatehead+leftcaudatetail+leftcorpuscallosum+leftcullmen+lefthippocampus+lefthypothalamus+leftmammillarybody+leftmedialdorsalnucleus+leftoptictract+leftpulvinar+leftputamen'

    
    
    RightHemiphereWhole = 'rightamygdala+rightanteriorcommissure+rightanteriornucleus+rightba1+rightba2+rightba3+rightba4+rightba5+rightba6+rightba7+rightba8+rightba9+rightba10+rightba11+rightba13+rightba17+rightba18+rightba19+rightba20+rightba21+rightba22+rightba23+rightba24+rightba25+rightba26+rightba27+rightba28+rightba29+rightba30+rightba31+rightba32+rightba33+rightba34+rightba35+rightba36+rightba37+rightba38+rightba39+rightba40+rightba41+rightba42+rightba43+rightba44+rightba45+rightba46+rightba47+rightbrodmannarea+rightcaudatebody+rightcaudatehead+rightcaudatetail+rightcorpuscallosum+rightculmen+righthippocampus+righthypothalamus+rightmammillarybody+rightopticaltract+rightpulvinar+rightputamen'



    RightHemiphere = ['rightba1','rightba2','rightba3',
                   'rightba4','rightba5','rightba6','rightba7','rightba8','rightba9','rightba10','rightba11','rightba17','rightba18',
                   'rightba19','rightba20','rightba21','rightba22','rightba23','rightba24','rightba25','rightba26','rightba27','rightba28','rightba29',
                   'rightba30','rightba31','rightba32','rightba33','rightba35','rightba36','rightba37','rightba38','rightba39','rightba40',
                   'rightba41','rightba42','rightba43','rightba44','rightba45','rightba46','rightba47',
                   'rightbrodmannarea','rightcaudatebody','rightcaudatehead','rightcaudatetail','rightcorpuscallosum','rightculmen',
                   'righthippocampus','righthypothalamus','rightmammillarybody','rightopticaltract','rightpulvinar','rightputamen']

    #multiple regions comparisions
    #labelName = ROI+'_lh'


    #ROImne=mne.read_label('/Users/esmamansouri/Documents/CODE/MRATPython27/MNELabels/leftba21-lh.label')
                   #'MRATPython27/MNELabels/leftba21-lh.label')
    #ROImneSources = ROImne.vertices


    #MneExperiment.load_label(labelName)

    #SourceObjectBESA = scipy.io.loadmat('sourcesOldBESA.mat')
    #SourceObjectBESANew = scipy.io.loadmat('matlabBESANEw.mat') #sources.mat')
    #SourceObjectBESA = SourceObjectBESANew
    RegionSourcesListAll = []
    RegionSourcesListMultiple = []
    #IF ROI IS A FILE
    ROIValues2 = []
    if ROIValues.find('/') != -1 :
        #if multiple file selected in find option
        if ',' in ROIValues:
            ROINamesFromFileNames = ROIValues.split(',')
            for RoiEl in ROINamesFromFileNames:

                FileNameParts = RoiEl.split('/')
                RoiName = FileNameParts[-1]
                p1 = application_path
                if 'MNELabels' not in p1:
                    ROImne=mne.read_label(p1+'/MNELabels/'+RoiName)
                else:

                    ROImne=mne.read_label(p1+'/'+RoiName)

                ROImneSources = ROImne.vertices
                RegionSources = ROImneSources
                RoiName = str(RoiName)
                RoiName = RoiName.replace('-lh.label', '')
                RoiName = RoiName.replace('-rh.label', '')
                ROIValues2.append(str(RoiName))
                        #a = SourceObjectBesa[0:1]['analysisRegion']



                RegionSourcesList = RegionSources.tolist()

                RegionSourcesListAll.append( RegionSourcesList)


            ROIValues = ROIValues2
            ROISources = RegionSourcesListAll #list(itertools.chain(*RegionSourcesListAll))


        else:
            with open(ROIValues) as f:

                if 'label' in ROIValues:
                    #label file from MNE
                    RoiName = ROIValues.split('/')
                    RoiName1= RoiName[-1]


                    if ROIValues.find('left'):

                        hem = 'lh'
                        RoiName1 = RoiName1.split('-lh.label')
                        RoiName1 = RoiName1[0]
                    elif ROIValues.find('right'):
                        hem = 'rh'

                        RoiName1 = RoiName1.split('-rh.label')
                        RoiName1 = RoiName1[0]

                        testpath = os.getcwd()
                    p1 = application_path

                    ROImne=mne.read_label(ROIValues)



                    ROImneSources = ROImne.vertices
                    RegionSources = ROImneSources
                    ROISources = RegionSources
                    ROIValues = RoiName1


                    #a = SourceObjectBesa[0:1]['analysisRegion']



                    RegionSourcesList = RegionSources.tolist()

                    RegionSourcesListAll.append( RegionSourcesList[0])
                else:

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
                                if roi.find('left'):
                                    hem = 'lh'
                                elif roi.find('right'):
                                    hem = 'rh'

                                testpath = os.getcwd()
                                p1 = application_path

                                if 'MNELabels' not in p1:
                                    ROImne=mne.read_label(p1+'/MNELabels/'+roi+'-'+ hem + '.label')
                                else:

                                    ROImne=mne.read_label(p1+'/'+roi+'-'+ hem + '.label')
                                #os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'MRATPython27'))
                                #ROImne=mne.read_label(p1+'/MNELabels/'+roi+'-'+ hem + '.label')

                                #ROImne=mne.read_label('/Users/esmamansouri/Documents/CODE/MRATPython27/MNELabels/'+roi+'-'+ hem + '.label')
                               #'MRATPython27/MNELabels/leftba21-lh.label')
                                ROImneSources = ROImne.vertices
                                RegionSources = ROImneSources


                                #a = SourceObjectBesa[0:1]['analysisRegion']



                                RegionSourcesList = RegionSources.tolist()

                                RegionSourcesListAll.append( RegionSourcesList[0])



                            ROISources = list(itertools.chain(*RegionSourcesListAll))
                        else:

                            ROIIndex = RegionNames.index(roi)

                                    #RegionSources = SourceObjectBESA.get('test2')[ROIIndex]
                            if 'left' in roi:
                                    hem = 'lh'
                            elif 'right' in roi:
                                    hem = 'rh'


                            testpath = os.getcwd()
                            p1 = application_path

                            if 'MNELabels' not in p1:
                                    ROImne=mne.read_label(p1+'/MNELabels/'+roi+'-'+ hem + '.label')
                            else:

                                    ROImne=mne.read_label(p1+'/'+roi+'-'+ hem + '.label')
                            #p1 = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'MRATPython27'))
                            #ROImne=mne.read_label(p1+'/MNELabels/'+roi+'-'+ hem + '.label')


                            #ROImne=mne.read_label('/Users/esmamansouri/Documents/CODE/MRATPython27/MNELabels/'+roi+'-'+ hem + '.label')

                            #'MRATPython27/MNELabels/leftba21-lh.label')
                            ROImneSources = ROImne.vertices
                            RegionSources = ROImneSources

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
        elif ROI == 'left hemisphere' or ROI == 'lefthemisphere':

            for reg in LeftHemisphere :
                ROIValues1 +=reg
                ROIValues1 +=','
            ROIValues = ROIValues1
            ROIValues = ROIValues[:-1]
        elif ROI == 'left hemisphere whole' or ROI =='lefthemispherewhole':


            ROIValues = lefthemisphereWhole
            #ROIValues = ROIValues[:-1]

        elif ROI == 'right hemisphere'or ROI == 'righthemisphere':

            for reg in RightHemiphere:
                ROIValues1 +=reg
                ROIValues1 +=','
            ROIValues = ROIValues1
            ROIValues = ROIValues[:-1]
        elif ROI == 'right hemisphere whole' or ROI == 'righthemispherewhole':
            ROIValues = RightHemiphereWhole




        rois = []

        #split regions to get sources



        index = 0
        # if Roi values are multiple regions separated by ,
        #n = ROIValues.count(',')
        #RegionSourcesListMultiple = np.empty((n+1, 0)).tolist()
        RegionSourcesListMultiple = []
        ROIValues1 = []
        ROIValues = str(ROIValues)
        if ROIValues.find(',') != -1 :
            MultipleRegion = ROIValues.split(',')
            for roi in MultipleRegion:



                ROIIndex = RegionNames.index(roi)

                #RegionSources = SourceObjectBESA.get('test2')[ROIIndex]
                #RegionSources = SourceObjectBESANew.get('a')[ROIIndex]
                #RegionSources = RegionSources[0]
                roi = str(roi)

                if 'left' in roi:
                        hem = 'lh'
                elif 'right' in roi:
                        hem = 'rh'
                #get current path
                testpath = os.getcwd()
                #p1 = os.path.dirname(os.path.realpath(__file__))

                p1 = application_path
                #p1 = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'MNELabels'))
                print(roi)
                if 'MNELabels' not in p1:

                        ROImne=mne.read_label(p1+'/MNELabels/'+roi+'-'+ hem + '.label')
                else:

                        ROImne=mne.read_label(p1+'/'+roi+'-'+ hem + '.label')
                #sys.path.insert(0, application_path+'/MNELabels')
                #ROImne=mne.read_label(application_path+'/MNELabels/'+roi+'-'+ hem + '.label')

                #p1 = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'MNELabels'))
                #ROImne=mne.read_label(p1+'/MNELabels/'+roi+'-'+ hem + '.label')
                #'MRATPython27/MNELabels/leftba21-lh.label')
                ROImneSources = ROImne.vertices
                RegionSources = ROImneSources

                #a = SourceObjectBesa[0:1]['analysisRegion']

                RegSource = RegionSources.tolist()
                #RegSource = RegSource[0]
                #RegSource[:] = [x - 1 for x in RegSource]
                RegionSourcesListMultiple.append(RegSource)
                ROIValues1.append(roi)


            ROIValues = MultipleRegion   #RegionSourcesListAll.append( RegionSourcesList[0])

            ROISources = RegionSourcesListMultiple
        else:

            # if combined region

            rois = ROIValues.split('+')

            for roi in rois:



                ROIIndex = RegionNames.index(roi)
                if 'left' in roi:
                        hem = 'lh'
                elif 'right' in roi:
                        hem = 'rh'

                testpath = os.getcwd()

                #p1 = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'MNELabels'))
                print(roi)
                p1 = application_path
                #p1 = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'MNELabels'))
                print(roi)
                if 'MNELabels' not in p1:
                    ROImne=mne.read_label(p1+'/MNELabels/'+roi+'-'+ hem + '.label')
                else:

                    ROImne=mne.read_label(p1+'/'+roi+'-'+ hem + '.label')

                #sys.path.insert(0, application_path+'/MNELabels')
                #ROImne=mne.read_label(application_path+'/MNELabels/'+roi+'-'+ hem + '.label')

                #ROImne=mne.read_label('/Users/esmamansouri/Documents/CODE/MRATPython27/MNELabels/'+roi+'-'+ hem + '.label')

                #'MRATPython27/MNELabels/leftba21-lh.label')
                ROImneSources = ROImne.vertices
                RegionSources = ROImneSources
                #RegionSources = SourceObjectBESA.get('test2')[ROIIndex]
                #RegionSources = SourceObjectBESANew.get('a')[ROIIndex]
                #RegionSources = RegionSources[0]

                #a = SourceObjectBesa[0:1]['analysisRegion']



                RegionSourcesList = RegionSources.tolist()

                RegionSourcesListAll.append( RegionSourcesList)



            ROISources = list(itertools.chain(*RegionSourcesListAll))

            #ROISources[:] = [x - 1 for x in ROISources] CHECK LATER

            ROISources1 = np.asarray(ROISources)
            ROISources = set(ROISources)
            ROISources = list( ROISources)
            if ROI == 'left hemisphere whole' or ROI =='lefthemispherewhole':
                ROIValues = 'lefthemispherewhole'
            elif ROI == 'right hemisphere whole' or ROI == 'righthemispherewhole':
                ROIValues = 'righthemispherewhole'

    return ROISources,ROIValues