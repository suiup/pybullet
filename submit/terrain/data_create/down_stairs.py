import numpy as np
import plotly.graph_objects as go

shape = 50

data = np.array([[x for x in [y] * 5 * shape] for y in reversed(range(int(shape/5))) ] ).reshape(shape, shape)
list = [i for i in data]
dataStr = ""
for i in list:
    dataStr += ",\t".join(('%.5f' % j) for j in i) + "\n"
print(dataStr)
with open("test.txt", "w") as f:
    f.write(dataStr)

fig = go.Figure(data=[
    go.Surface(z=data),
])

fig.show()