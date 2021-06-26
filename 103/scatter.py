import pandas as pd
import plotly.express as px

df = pd.read_csv("own.csv")

fig = px.scatter(df, x="C", y="A", size="B", color="D", title="own data")

fig.show()