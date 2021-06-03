import numpy as np
import plotly.graph_objects as go

list = []
with open("data.txt", "r") as f:
    data = f.readlines()
    for line in data:
        line = line.strip('\n')
        list.append(line)

dd = np.array(list)
print(dd)
#
# fig = go.Figure(data=[
#     go.Surface(z=dd),
# ])
#
# fig.show()