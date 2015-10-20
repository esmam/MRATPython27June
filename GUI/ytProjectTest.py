__author__ = 'esmab'

import yt
import numpy as np

ds = yt.load("IsolatedGalaxy/galaxy0030/galaxy0030")
# Choose a field
field = 'density'
# Do you want the log of the field?
use_log = True

# Find the bounds in log space of for your field
dd = ds.all_data()
mi, ma = dd.quantities.extrema(field)

if use_log:
    mi,ma = np.log10(mi), np.log10(ma)

# Instantiate the ColorTransferfunction.
tf = yt.ColorTransferFunction((mi, ma))

# Set up the camera parameters: center, looking direction, width, resolution
c = (ds.domain_right_edge + ds.domain_left_edge)/2.0
L = np.array([1.0, 1.0, 1.0])
W = ds.quan(0.3, 'unitary')
N = 256

# Create a camera object
cam = ds.camera(c, L, W, N, tf, fields = [field], log_fields = [use_log])

# Now let's add some isocontours, and take a snapshot, saving the image
# to a file.
tf.add_layers(10, 0.01, colormap = 'RdBu_r')
im = cam.snapshot('test_rendering.png')

# To add the domain box to the image:
nim = cam.draw_domain(im)
nim.write_png('test_rendering_with_domain.png')

# To add the grid outlines to the image:
nim = cam.draw_grids(im)
nim.write_png('test_rendering_with_grids.png')