
from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph as pg
import pyqtgraph.opengl as gl
import numpy as np
import plotly.graph_objects as go

## Create a GL View widget to display data
app = pg.mkQApp("Example")
w = gl.GLViewWidget()
w.show()
w.setWindowTitle('pyqtgraph example: GLSurfacePlot')
w.setCameraPosition(distance=50)
g = gl.GLGridItem()
g.scale(3, 3, 1)
g.setDepthValue(10)  # draw grid after surfaces since they may be translucent
w.addItem(g)

z1 = pg.gaussianFilter(np.random.normal(size=(50, 50)), (1, 1))
print(z1)


fig = go.Figure(data=[
    go.Surface(z=z1)
])

fig.show()


# p1 = gl.GLSurfacePlotItem(z=z, shader='shaded', color=(0.5, 0.5, 1, 1))
# p1.scale(16. / 49., 16. / 49., 1.0)
# p1.translate(-10, 2, 0)
# w.addItem(p1)

if __name__ == '__main__':
    pg.mkQApp().exec_()