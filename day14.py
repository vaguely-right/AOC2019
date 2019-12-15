import numpy as np
import pandas as pd

#%%
fname = 'day14example1.txt'
with open(fname,'r') as f:
    d14 = f.readlines()
d14 = [i[:-1] for i in d14]
d14 = [i.split(sep='=>') for i in d14]

#Get the unique outputs
chemicals = [i[1].split(sep=' ')[-1] for i in d14]
#Add ORE to make the unique elements
elements = chemicals + ['ORE']
#Build a dataframe for the reactions
reactions = pd.DataFrame(columns=[elements+['QTY']],index=chemicals)
for i in d14:
    prod = i[1].strip().split()[1]
    reactions.at[prod,'QTY'] = i[1].strip().split(sep=' ')[0]
    