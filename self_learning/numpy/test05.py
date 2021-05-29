import numpy as np
import plotly.graph_objects as go


data = np.zeros((50, 50))
print(data)

data2 = np.linspace(-1, 1, 2500).reshape(50,50)

print(data2)
fig = go.Figure(data=[
    go.Surface(z=data2),
])

fig.show()