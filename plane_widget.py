from pyvista import set_plot_theme
set_plot_theme('document')

import pyvista as pv

file = 'engine.nhdr'
vol = pv.read(file)
vol

# Create opacity transfer function
opacity = [0.0, 0.1, 0.5, 0.9, 0]

# Render engine block with plane widget
p = pv.Plotter()

p.add_mesh_slice(vol)
p.show_grid()
p.add_axes()
p.show()

