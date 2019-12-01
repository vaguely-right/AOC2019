import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
os.chdir('AOC2019')

#%%
#Part 1
fname = 'day1input.txt'
data = pd.read_csv(fname,header=None)
data.columns = ['weight']

f = lambda x: int(x/3) - 2
data['fuel'] = data.applymap(f)
data.fuel.sum()

#%%
#Part 2
fname = 'day1input.txt'
data = pd.read_csv(fname,header=None)
data.columns = ['weight']

f = lambda x: int(x/3) - 2
data['fuel0'] = data.applymap(f)

for i in range(1,10,1):
    data['fuel'+str(i)] = pd.DataFrame(data['fuel'+str(i-1)]).applymap(f)
    data['fuel'+str(i)] = data['fuel'+str(i)].clip(lower=0)

data.sum()
data.sum().sum() - data.weight.sum()

#%%
#For the brute force solution, plot the results. Just because I can.
plt.rcParams["figure.figsize"] = (11,5) 
data.drop('weight',axis=1).plot.bar(stacked=True,legend=False)

#%%
#Part 2 again, doing a proper function this time
def get_fuel(weight):
    ifuel = weight
    totfuel = 0
    while ifuel > 0:
        ifuel = int(ifuel/3)-2
        ifuel = np.maximum(ifuel,0)
        totfuel = totfuel + ifuel
    return totfuel

fname = 'day1input.txt'
data = pd.read_csv(fname,header=None)
data.columns = ['weight']

data['fuel'] = data.applymap(get_fuel)
data.fuel.sum()






