#write all parameter to ini

import ConfigParser
import os
import sys
from PyQt5 import QtGui
from PThresholdTemporalSourceTTestMNE import PThresholdTempSourceTTestMNE
from PThresholdTemporalSourceTTest import PThresholdTempSourceTTest
import shutil




def openIni(self):
    fileName = QtGui.QFileDialog.getOpenFileName(self, 'OpenFile')
    self.myTextBox.setText(fileName)
    print(fileName)


def MRAT_WriteIniAOVA(ttestOrAnova, filePath,root, **options): #design, condition1Name,startTime,endTime, presTim,PThresh,minTemporalCluster, minSpatialCluster,numPerm, ROI,maxFDR,SpatioTemp):
    #get template path directory

    if getattr(sys, 'frozen', False):
                application_path = os.path.dirname(sys.executable)



                #fsaveragePath  = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'fsaverage'))
                templatePath = application_path+'/'
                print(templatePath)

    elif __file__:
                application_path = os.path.dirname(__file__)

                print(application_path)

                templatePath = application_path+'/'

    sys.path.insert(0, templatePath)

    #templatePath = os.path.join(os.path.dirname(__file__), '') OLD



    #templatePath = os.path.abspath(__file__)
    config = ConfigParser.ConfigParser()
    shutil.copy2(templatePath+'TemplateANOVA.ini', filePath)

    ini = config.read(filePath)

    cfgfile = open(filePath,'w')

    # add the settings to the structure of the file, and lets write it out...
    #config.add_section('Person')
    #config.set('Person','HasEyes',True)
    #config.set('Person','Age', 50)
    #config.write(cfgfile)


    #config.add_section('Section1')
    config.set('testOptions', 'TFCEPerm', 'perm')
    config.set('testOptions', 'windowOrPerm', 'perm')
    config.set('testOptions', 'anovaScript', str(options.get('design')))
    config.set('testOptions', 'anovaOrT', 'ANOVA')
    config.set('testOptions', 'anovaType', 'F')
    config.set('testOptions', 'numPerms', str(options.get('numPerm')))
    config.set('testOptions', 'minClusterLength', str(options.get('minTemporalCluster')))
    config.set('testOptions', 'minClusterLengthSpatio',str(options.get('minClusterLengthSpatio')))
    config.set('testOptions', 'compTestPThresh', str(options.get('PThresh')) )
    config.set('testOptions', 'maxFDR', str(options.get('maxFDR')))
    config.set('testOptions', 'badsubjs', str(options.get('badsubjs')))
    config.set('testOptions', 'sensorOrSource', 'source')
    config.set('timeWindow', 'TOI', str(options.get('startTime'))+' '+str(options.get('endTime')))
    config.set('timeWindow', 'preStimInterval', options.get('presTim'))
    config.set('regionNames', 'regionNames', options.get('ROI'))
    config.set('dataSet', 'path', root)

    config.set('dataSet', 'conditions', options.get('condition1Name'))
    config.set('SpatioTemp', 'SpatioTemp', options.get('SpatioTemp'))
    if options.get('SpatioTemp') == 'SpatioTemp':
        config.set('testOptions', 'minSpatialClusterLength', str(options.get('minSpatialCluster')))

    config.set('MNEORBESA', 'MNEORBESA', 'MNE')








    #config.set('Section1', 'an_int', '15')

    config.write(cfgfile)
    cfgfile.close()
    #config.set('Section1', 'a_bool', 'true')
