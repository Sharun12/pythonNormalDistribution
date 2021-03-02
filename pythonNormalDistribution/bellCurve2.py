import csv
import pandas as pd 
import plotly.figure_factory as pff

df=pd.read_csv("data.csv")

fig=pff.create_distplot([df["Weight(Pounds)"].tolist()], ["Weight"], show_hist=False)

fig.show()