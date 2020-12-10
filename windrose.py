import plotly.express as px
import pandas as pd
"""
df = px.data.wind()

print(df.shape)
print(df.head(20))
print(df.tail(20))
df.to_csv("windrose_data.csv", index=False)
"""

df = pd.read_csv('windrose_data_copy.csv')

fig = px.bar_polar(
    df,
    r="strength",
    theta="direction",
    color="frequency",
    #template="plotly_dark",
    #color_discrete_sequence= px.colors.sequential.Plasma_r
)

fig.show()
