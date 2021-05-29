import numpy as np
import plotly.graph_objects as go

data = np.random.normal(size=(50,50))
print(data)

fig = go.Figure(data=[
    go.Surface(z=data)
])

fig.show()