#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vispy: gallery 2
# Copyright (c) 2015, Vispy Development Team.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.

"""
3D brain mesh viewer.
"""

from timeit import default_timer
import numpy as np

from vispy import gloo
from vispy import app
from vispy.util.transforms import perspective, translate, rotate
from vispy.io import load_data_file

brain = np.load(load_data_file('brain/brain.npz', force_download='2014-09-04'))
data = brain['vertex_buffer']
faces = brain['index_buffer']

import scipy.io
brain1 = scipy.io.loadmat('NewBESATri.mat')
#brain1 = scipy.io.loadmat('NewBESATri.mat')
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


VERT_SHADER = """
#version 120
uniform mat4 u_model;
uniform mat4 u_view;
uniform mat4 u_projection;
uniform vec4 u_color;
attribute vec3 a_position;
attribute vec3 a_normal;
attribute vec4 a_color;
varying vec3 v_position;
varying vec3 v_normal;
varying vec4 v_color;
void main()
{
    v_normal = a_normal;
    v_position = a_position;
    v_color = a_color * u_color;
    gl_Position = u_projection * u_view * u_model * vec4(a_position,1.0);
}
"""

FRAG_SHADER = """
#version 120
uniform mat4 u_model;
uniform mat4 u_view;
uniform mat4 u_normal;
uniform vec3 u_light_intensity;
uniform vec3 u_light_position;
varying vec3 v_position;
varying vec3 v_normal;
varying vec4 v_color;
void main()
{
    // Calculate normal in world coordinates
    vec3 normal = normalize(u_normal * vec4(v_normal,1.0)).xyz;
    // Calculate the location of this fragment (pixel) in world coordinates
    vec3 position = vec3(u_view*u_model * vec4(v_position, 1));
    // Calculate the vector from this pixels surface to the light source
    vec3 surfaceToLight = u_light_position - position;
    // Calculate the cosine of the angle of incidence (brightness)
    float brightness = dot(normal, surfaceToLight) /
                      (length(surfaceToLight) * length(normal));
    brightness = max(min(brightness,1.0),0.0);
    // Calculate final color of the pixel, based on:
    // 1. The angle of incidence: brightness
    // 2. The color/intensities of the light: light.intensities
    // 3. The texture and texture coord: texture(tex, fragTexCoord)
    // Specular lighting.
    vec3 surfaceToCamera = vec3(0.0, 0.0, 1.0) - position;
    vec3 K = normalize(normalize(surfaceToLight) + normalize(surfaceToCamera));
    float specular = clamp(pow(abs(dot(normal, K)), 40.), 0.0, 1.0);
    gl_FragColor = v_color * brightness * vec4(u_light_intensity, 1);
}
"""


class Canvas(app.Canvas):
    def __init__(self):
        app.Canvas.__init__(self, keys='interactive')
        self.size = 800, 600

        self.program = gloo.Program(VERT_SHADER, FRAG_SHADER)

        self.theta, self.phi = -80, 180
        self.translate = 8

        self.faces = gloo.IndexBuffer(faces)
        self.program.bind(gloo.VertexBuffer(data))

        self.program['u_color'] = 1, 1, 1, 1
        self.program['u_light_position'] = (1., 1., 1.)
        self.program['u_light_intensity'] = (1., 1., 1.)

        self.apply_zoom()

        gloo.set_state(blend=False, depth_test=True, polygon_offset_fill=True)

        self._t0 = default_timer()
        self._timer = app.Timer('auto', connect=self.on_timer, start=True)

        self.update_matrices()

    def update_matrices(self):
        self.view = translate((0, 0, -self.translate))
        self.model = np.dot(rotate(self.theta, (1, 0, 0)),
                            rotate(self.phi, (0, 1, 0)))
        self.projection = np.eye(4, dtype=np.float32)
        self.program['u_model'] = self.model
        self.program['u_view'] = self.view
        self.program['u_normal'] = np.linalg.inv(np.dot(self.view,
                                                        self.model)).T

    def on_timer(self, event):
        elapsed = default_timer() - self._t0
        self.phi = 180 + elapsed * 50.
        self.update_matrices()
        self.update()

    def on_resize(self, event):
        self.apply_zoom()

    def on_mouse_wheel(self, event):
        self.translate += -event.delta[1]/5.
        self.translate = max(2, self.translate)
        self.update_matrices()
        self.update()

    def on_draw(self, event):
        gloo.clear()
        self.program.draw('triangles', indices=self.faces)

    def apply_zoom(self):
        gloo.set_viewport(0, 0, self.physical_size[0], self.physical_size[1])
        #self.projection = perspective(90, self.size[0] /
        #                              float(self.size[1]), 1.0, 20.0)
        self.projection = perspective(90, 1, 10.0, -200.0)
        self.program['u_projection'] = self.projection

if __name__ == '__main__':
    c = Canvas()
    c.show()
    app.run()