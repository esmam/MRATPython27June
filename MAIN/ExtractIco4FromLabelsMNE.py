
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






def ExtractMNEico4():


    if getattr(sys, 'frozen', False):
        application_path = os.path.dirname(sys.executable)

        print(application_path)
    elif __file__:
        application_path = os.path.dirname(__file__)

        application_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', ''))


    for name in os.listdir(application_path + '/' + '/GUI/FullLabels'):
        #read mne
        count = 0
        linecounter = 1
        if 'label' in name :

            with open(application_path + '/' + '/GUI/FullLabels/'+name) as inf, open(application_path + '/' + '/GUI/FullLabelsNew/'+name, 'w') as newfile:
                for line in inf:
                    if count < 2:
                        newfile.write(line)

                    parts = line.split() # split line into parts
                    if len(parts) == 5:   # get the vertices lines
                        if int(parts[0]) <= 2562:
                            newfile.write(line)
                            linecounter = linecounter + 1
                    count = count +1

            lbl = mne.read_label(application_path+'/GUI/FullLabels/'+name)


            ROImneSources = lbl.vertices

        #get only vertices of interest