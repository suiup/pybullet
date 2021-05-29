import numpy as np

import plotly.graph_objs as go

a = np.linspace(-1, 1, 31)

b = np.linspace(-1, 1, 31)

x, y = np.meshgrid(a, b)

z = x ** 2 + y ** 2 + x * y + x + y + 1

fig = go.Figure(data=[
    go.Surface(x=x, y=y, z=z),
])

fig.show()
