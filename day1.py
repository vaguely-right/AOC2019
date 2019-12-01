import numpy as np
import pandas as pd

#Part 1
fname = 'day1input.txt'
data = pd.read_csv(fname,header=None)
data.columns = ['weight']

f = lambda x: int(x/3) - 2
data['fuel'] = data.applymap(f)
data.fuel.sum()


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
