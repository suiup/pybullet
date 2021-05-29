import numpy as np
import plotly.graph_objects as go

z1 = np.array([[0.0, 1, 0.0, 0.0, 0.0],
                   [0.0, 0.0, 0.0, 0.0, 0.0],
                   [0.0, 0.0, 0.0, 0.0, 0.0],
                   [0.0, 0.0, 0.0, 0.0, 0.0],
                   [0.0, 0.0, 0.0, 0.0, -1]])

fig = go.Figure(data=[
    go.Surface(z=z1),
])

fig.show()
