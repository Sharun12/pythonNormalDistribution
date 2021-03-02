import csv
import pandas as pd 
import plotly.figure_factory as pff 

df=pd.read_csv("data.csv")

fig=pff.create_distplot([df["Avg Rating"].tolist()], ["Avg Rating"], show_hist=False)

fig.show()