import random
import plotly.express as px 
import plotly.figure_factory as ff 

diceSum=[]
frequency=[]

for num in range(0, 100):
    dice1=random.randint(1, 6)
    dice2=random.randint(1,6)

    diceSum.append(dice1+dice2)

    frequency.append(num)
    
fig=ff.create_distplot([diceSum], ["result"])

fig.show()