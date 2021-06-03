import numpy as np
import plotly.graph_objects as go

data = [
  [13, 3, 3, 5],
  [13, 2, 1, 5],
  [13, 10, 11, 12],
  [13, 8, 8, 8]
]

fig = go.Figure(data=[
    go.Surface(z=data),
])

fig.show()