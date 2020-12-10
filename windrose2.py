import plotly.express as px
import pandas as pd
#df = px.data.wind()
df = pd.read_csv("windrose_data_copy.csv")
fig = px.bar_polar(df, r="frequency", theta="direction",
                   color="strength", #template="plotly_dark",
                   color_discrete_sequence= px.colors.sequential.Plasma_r)
fig.show()