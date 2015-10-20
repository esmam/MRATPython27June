# -*- coding: utf-8 -*-
# Copyright (c) 2015, Vispy Development Team.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.

"""
Simple demonstration of Mesh visual.
"""

import numpy as np
import vispy
from vispy import app, gloo, visuals
from vispy.geometry import create_sphere
from vispy.visuals.transforms import (STTransform, MatrixTransform,
                                      ChainTransform)
from vispy.io import load_data_file
import scipy.io

brain1 = scipy.io.loadmat('NewBESATri.mat')
class Canvas(app.Canvas):
    def __init__(self):
        app.Canvas.__init__(self, keys='interactive', size=(800, 600))
        brain = np.load(load_data_file('brain/brain.npz', force_download='2014-09-04'))

        #brain1 = scipy.io.loadmat('NewBESATri.mat')
        brain2 = brain1['t']


        from numpy import genfromtxt
        my_data = genfromtxt('BESACOORD61.csv', delimiter=',')

        dataTest = brain['vertex_buffer']
        color = dataTest['a_color']
        color = color[750:1500]
        facesTest = brain['index_buffer']

        n = 750
        ps = 100
        data = np.zeros(n, [('a_position', np.float32, 3),
                            ('a_normal', np.float32, 3),
                            ('a_color', np.float32, 3)])
                            #('a_size', np.float32, 1)])

        import scipy.spatial
        tri = scipy.spatial.Delaunay(my_data) # points: np.array() of 3d points
        convex = tri.convex_hull
        indices = tri.simplices
        vertices = my_data[indices]
        data['a_position'] = my_data
        data['a_color'] = np.random.uniform(0, 1, (n, 3))
        faces = brain2
        faces = faces-1
        vertices = my_data
        norm = np.zeros( vertices.shape, dtype=vertices.dtype )
        #Create an indexed view into the vertex array using the array of three indices for triangles
        tris = vertices[faces]

        #Calculate the normal for all the triangles, by taking the cross product of the vectors v1-v0, and v2-v0 in each triangle
        n = np.cross( tris[::,1 ] - tris[::,0]  , tris[::,2 ] - tris[::,0] )
        # n is now an array of normals per triangle. The length of each normal is dependent the vertices,
        # we need to normalize these, so that our next step weights each normal equally.
        lens = np.sqrt( n[:,0]**2 + n[:,1]**2 + n[:,2]**2 )
        n[:,0] /= lens
        n[:,1] /= lens
        n[:,2] /= lens



        norm[ faces[:,0] ] += n
        norm[ faces[:,1] ] += n
        norm[ faces[:,2] ] += n

        ''' Normalize a numpy array of 3 component vectors shape=(n,3) '''
        lens = np.sqrt( norm[:,0]**2 + norm[:,1]**2 + norm[:,2]**2 )
        norm[:,0] /= lens
        norm[:,1] /= lens
        norm[:,2] /= lens

        data['a_normal'] = norm #np.random.uniform(0, 1.0, (n, 3)) #10, 3, 3
        #data['a_size'] = np.random.uniform(5*ps, 10*ps, n)
        u_linewidth = 1.0
        u_antialias = 1.0



        brain2 = np.uint32(brain2)
        convex = np.uint32(convex)
        data = data
        faces = brain2-1

        #data = dataTest
        #faces = facesTest

        self.meshes = []
        self.rotation = MatrixTransform()

        # Generate some data to work with
        global mdata
        mdata = create_sphere(20, 40, 1.0)
        #mdata['_faces'] =faces
        #mdata['_vertices']=data
        # Mesh with pre-indexed vertices, uniform color
        meshData=vispy.geometry.MeshData(vertices=data['a_position'], faces=None, edges=None, vertex_colors=None, face_colors=None)
        meshData._vertices = data['a_position']
        meshData._faces = faces
        #meshData._face_colors = data['a_color']
        #meshData._vertex_colors = data['a_color']

        self.meshes.append(visuals.MeshVisual(meshdata=meshData, color='b'))
        #for mesh in self.meshes:
        #    mesh.draw()

        # Mesh with pre-indexed vertices, per-face color
        # Because vertices are pre-indexed, we get a different color
        # every time a vertex is visited, resulting in sharp color
        # differences between edges.
        tris = vertices[faces]
        verts = data['a_position'] #mdata.get_vertices(indexed='faces')

        nf = 1496#verts.size//9
        fcolor = np.ones((nf, 3, 4), dtype=np.float32)
        fcolor[..., 0] = np.linspace(1, 0, nf)[:, np.newaxis]
        fcolor[..., 1] = np.random.normal(size=nf)[:, np.newaxis]
        fcolor[..., 2] = np.linspace(0, 1, nf)[:, np.newaxis]
        #fcolor = data['a_color']
        mesh = visuals.MeshVisual(vertices=tris, face_colors=fcolor)
        self.meshes.append(mesh)


        # Mesh with unindexed vertices, per-vertex color
        # Because vertices are unindexed, we get the same color
        # every time a vertex is visited, resulting in no color differences
        # between edges.
        #verts = mdata.get_vertices()
        faces = faces #mdata.get_faces()
        nv = verts.size//3
        vcolor = np.ones((nv, 4), dtype=np.float32)
        vcolor[:, 0] = np.linspace(.6, .6, nv)
        vcolor[:, 1] = np.random.normal(size=nv)
        vcolor[:, 2] = np.linspace(0.6, .6, nv)
        self.meshes.append(visuals.MeshVisual(verts, faces, vcolor))
        self.meshes.append(visuals.MeshVisual(verts, faces, vcolor,
                                              shading='flat'))
        #
        self.meshes.append(visuals.MeshVisual(verts, faces, vcolor,
                                              shading='smooth'))

        # Lay out meshes in a grid
        grid = (1, 1)
        s = 300. / max(grid)
        #s = 500
        for i, mesh in enumerate(self.meshes):
            x = 800. * (i % grid[0]) / grid[0]  / grid[0] - 2
            y = 800. * (i // grid[1]) / grid[1]  / grid[1] + 2
            transform = ChainTransform([STTransform(translate=(x, y),
                                                    scale=(s, s, s)),
                                        self.rotation])
            mesh.transform = transform
            mesh.transforms.scene_transform = STTransform(scale=(.01, .01, .00001))

        self.show()

        self.timer = app.Timer(connect=self.rotate)
        self.timer.start(0.00016)

    def rotate(self, event):
        # rotate with an irrational amount over each axis so there is no
        # periodicity
        self.rotation.rotate(0.2 ** 0.5, (1, 0, 0))
        self.rotation.rotate(0.3 ** 0.5, (0, 1, 0))
        self.rotation.rotate(0.5 ** 0.5, (0, 0, 1))
        self.update()

    def on_resize(self, event):
        # Set canvas viewport and reconfigure visual transforms to match.
        vp = (0,0,self.physical_size[0], self.physical_size[1])

        self.context.set_viewport(*vp)

        for mesh in self.meshes:
            mesh.transforms.configure(canvas=self, viewport=vp)

    def on_draw(self, ev):
        test = self.physical_size
        gloo.set_viewport(800, 0, *self.physical_size)
        gloo.clear(color='white', depth=True)

        for mesh in self.meshes:
            mesh.draw()


if __name__ == '__main__':
    win = Canvas()
    import sys
    if sys.flags.interactive != 1:
        app.run()