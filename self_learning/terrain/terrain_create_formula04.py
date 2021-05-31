import numpy as np

import plotly.graph_objs as go

a=np.linspace(-2,2,50)

b=np.linspace(-2,2,50)

x,y=np.meshgrid(a,b)

z=x**2-y**2

list = [i for i in z]
dataStr = ""
for i in list:
    dataStr += ",\t".join(('%.5f' % j) for j in i) + "\n"
print(dataStr)
with open("test.txt", "w") as f:
    f.write(dataStr)

# fig = go.Figure(data=[
#     go.Surface(x = x, y = y, z = z),
# ])
#
# fig.show()