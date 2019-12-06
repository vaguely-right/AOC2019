import pandas as pd
import numpy as np
from tqdm import tqdm
import os
os.chdir('AOC2019')

#%%
#Part 1
fname = 'day6input.txt'
#day6input = list(np.loadtxt(fname,delimiter=')',dtype=str))
df = pd.read_csv(fname,sep=')',header=None)

df['orbits'] = np.nan

for i in tqdm(range(len(df))):
    j = df[1][i]
    orbits = 0
    while j in df[1].unique():
        orbits += 1
        j = df[0][df[1]==j].tolist()[0]
    df.orbits[i] = orbits

#%%
#Part 2
#Get YOU orbits
you = ['YOU']
o = 'YOU'
while o in df[1].unique():
    you.append(df[0][df[1]==o].tolist()[0])
    o = you[-1]
#Get SAN orbits
san = ['SAN']
o = 'SAN'
while o in df[1].unique():
    san.append(df[0][df[1]==o].tolist()[0])
    o = san[-1]

#Find the common orbits, and the closest one
common = list(set(you).intersection(san))
transfers = []
for i in common:
    transfers.append(you.index(i)-1+san.index(i)-1)
    
np.min(transfers)
common[transfers.index(np.min(transfers))]
