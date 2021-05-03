from pyvista import set_plot_theme
set_plot_theme('document')

import pyvista as pv
import matplotlib.pyplot as plt

file = 'engine.nhdr'
vol = pv.read(file)
vol

# Create opacity transfer function
opacity = [0, 0, 0.1, 0, 0, 0, 0, 0, 1, 1]

# Render engine block with box widget
p = pv.Plotter()
p.add_volume(vol, opacity=opacity, shade=False)
p.add_mesh_clip_box(vol, opacity=opacity)
p.show()