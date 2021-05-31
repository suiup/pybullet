import numpy as np

import plotly.graph_objs as go


z = np.array([[x**2 + y**2 for x in np.linspace(-2,2,10)] for y in np.linspace(0,1,10)])

list = [i for i in z]
dataStr = ""
for i in list:
    dataStr += ",\t".join(('%.5f' % j) for j in i) + "\n"
print(dataStr)
with open("test.txt", "w") as f:
    f.write(dataStr)


x, y = np.meshgrid(range(z.shape[0]), range(z.shape[1]))

fig = go.Figure(data=[
    go.Surface(x=x, y=y, z=z),
])

fig.show()
