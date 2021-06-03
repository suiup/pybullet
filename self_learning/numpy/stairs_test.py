import numpy as np
import plotly.graph_objects as go
        #y
data = [[0,0,0,0,0],#x
        [0.1,0.2,0.3,0.4,0.5],
        [0,1,1,1,0],
        [0,1,1,1,0],
        [0,2,2,2,0],]


fig = go.Figure(data=[
    go.Surface(z=data),
])

fig.show()