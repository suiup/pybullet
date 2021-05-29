import numpy as np

import plotly.graph_objs as go


z = np.array([[x**2 + y**2 for x in np.linspace(-5,5,50)] for y in np.linspace(0,1,10)])
x, y = np.meshgrid(range(z.shape[0]), range(z.shape[1]))

fig = go.Figure(data=[
    go.Surface(x=x, y=y, z=z),
])

fig.show()
