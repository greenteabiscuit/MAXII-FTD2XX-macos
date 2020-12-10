import numpy as np
import plotly.graph_objects as go
r, theta = np.mgrid[0.1:1:10j, 0:360:20j]
color = np.random.random(r.shape)
fig = go.Figure(go.Barpolar(
    r=r.ravel(),
    theta=theta.ravel(),
    marker_color=color.ravel()),)
fig.update_layout(polar_bargap=0)
fig.show()