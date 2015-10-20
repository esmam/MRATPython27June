#Function for plotting brain and ROI or spatial cluster
#
import sys
import vtk


import numpy as np
from mayavi import mlab
import numpy

from mayavi.mlab import *
from numpy import genfromtxt
import scipy.io
import numpy as np
import scipy.spatial
import scipy.io

def PlotBESABrain(ROIsources):

    #get sources and coordinates from BESA brain
    my_data = genfromtxt('BESACOORD61.csv', delimiter=',')

    #get triangulation from BESA brain
    brain1 = scipy.io.loadmat('NewBESATri.mat')
    vertices1 = my_data
    brain2 = brain1['t']
    faces1 = brain2

    ROIData = my_data[ROIsources]





    faces = brain2
    faces = faces-1

    faces = faces.tolist()
    faces = list(map(tuple, faces))


    vertices = my_data
    tris = vertices[faces]
    data = vertices#[::,0]
    #data = my_data
    x = np.array(data[::,0])
    y = np.array(data[::,1])
    z = np.array(data[::,2])

    ROIx = np.array(ROIData[::,0])
    ROIy = np.array(ROIData[::,1])
    ROIz = np.array(ROIData[::,2])


    '''ROIx = np.reshape(ROIx, (-1, 3))


    ROIy = np.reshape(ROIy, (-1,3))


    ROIz = np.reshape(ROIz, (-1,3))'''

    tri = scipy.spatial.Delaunay(ROIData) # points: np.array() of 3d points
    convex = tri.convex_hull
    indices = tri.simplices
    vertices = ROIData[indices]
    convex = convex.tolist()
    convex = list(map(tuple, convex))

    # Create the data.


    # View it.


    mlab.figure(1, bgcolor=(1,1,1))
    mlab.clf()

    triangles = faces

    ROItriangles = triangles < 9
    mlab.triangular_mesh(x, y, z, triangles, scalars=z, color = (0.3,.8,.9),colormap='bone', opacity=1)
    mlab.points3d(ROIx,ROIy,ROIz, colormap='cool', mode='cube')
    #mlab,triangular_mesh(ROIx,ROIy, ROIz, convex,scalars = ROIz,color=(0,0,1))

    mlab.show()

#mlab.points3d(x, y, z, z, mode = 'cone', scale_factor=.74)
#mlab.quiver3d(x,y,z)
#mlab.show()

if __name__ == '__main__':

  ROIsources = []
  ROIsources = [1,2,3,4,5,6,7,8,9]
  results = PlotBESABrain(ROIsources)

