import numpy as np
import pandas as pd
import re

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
reactions = pd.DataFrame(columns=[elements+['QTY']],index=elements)

#reactions.at['ORE','ORE'] = 1
reactions.at['ORE','QTY'] = 1
for i in d14:
    prod = i[1].strip().split()[1]
    reactions.at[prod,'QTY'] = i[1].strip().split(sep=' ')[0]
    for j in range(1,len(i[0].strip().split()),2):
        chem = i[0].strip().replace(',',' ').split()[j]
        reactions.at[prod,chem] = i[0].strip().replace(',',' ').split()[j-1]

reactions[reactions.isna()] = 0
oreperfuel = 13312

#%%
#Example 2
fname = 'day14example2.txt'
with open(fname,'r') as f:
    d14 = f.readlines()
d14 = [i[:-1] for i in d14]
d14 = [i.split(sep='=>') for i in d14]

#Get the unique outputs
chemicals = [i[1].split(sep=' ')[-1] for i in d14]
#Add ORE to make the unique elements
elements = chemicals + ['ORE']
#Build a dataframe for the reactions
reactions = pd.DataFrame(columns=[elements+['QTY']],index=elements)

#reactions.at['ORE','ORE'] = 1
reactions.at['ORE','QTY'] = 1
for i in d14:
    prod = i[1].strip().split()[1]
    reactions.at[prod,'QTY'] = i[1].strip().split(sep=' ')[0]
    for j in range(1,len(i[0].strip().split()),2):
        chem = i[0].strip().replace(',',' ').split()[j]
        reactions.at[prod,chem] = i[0].strip().replace(',',' ').split()[j-1]

reactions[reactions.isna()] = 0
oreperfuel = 180697

#%%
#Example 3
fname = 'day14example3.txt'
with open(fname,'r') as f:
    d14 = f.readlines()
d14 = [i[:-1] for i in d14]
d14 = [i.split(sep='=>') for i in d14]

#Get the unique outputs
chemicals = [i[1].split(sep=' ')[-1] for i in d14]
#Add ORE to make the unique elements
elements = chemicals + ['ORE']
#Build a dataframe for the reactions
reactions = pd.DataFrame(columns=[elements+['QTY']],index=elements)

#reactions.at['ORE','ORE'] = 1
reactions.at['ORE','QTY'] = 1
for i in d14:
    prod = i[1].strip().split()[1]
    reactions.at[prod,'QTY'] = i[1].strip().split(sep=' ')[0]
    for j in range(1,len(i[0].strip().split()),2):
        chem = i[0].strip().replace(',',' ').split()[j]
        reactions.at[prod,chem] = i[0].strip().replace(',',' ').split()[j-1]

reactions[reactions.isna()] = 0
oreperfuel = 2210736

#%%
#Part 1 for real.
fname = 'day14input.txt'
with open(fname,'r') as f:
    d14 = f.readlines()
d14 = [i[:-1] for i in d14]
d14 = [i.split(sep='=>') for i in d14]

#Get the unique outputs
chemicals = [i[1].split(sep=' ')[-1] for i in d14]
#Add ORE to make the unique elements
elements = chemicals + ['ORE']
#Build a dataframe for the reactions
reactions = pd.DataFrame(columns=[elements+['QTY']],index=elements)

#reactions.at['ORE','ORE'] = 1
reactions.at['ORE','QTY'] = 1
for i in d14:
    prod = i[1].strip().split()[1]
    reactions.at[prod,'QTY'] = i[1].strip().split(sep=' ')[0]
    for j in range(1,len(i[0].strip().split()),2):
        chem = i[0].strip().replace(',',' ').split()[j]
        reactions.at[prod,chem] = i[0].strip().replace(',',' ').split()[j-1]

reactions[reactions.isna()] = 0
oreperfuel = 751038

#%%
#Part 1 running
needed = pd.DataFrame(columns=['QTY'],index=elements)
needed.QTY = 0
needed.at['FUEL','QTY'] = 1
have = pd.DataFrame(columns=['QTY'],index=elements)
have.QTY = 0
have.at['ORE','QTY'] = 1000000000000 

while np.any(needed > have):
    for i in chemicals:
        if needed.QTY.loc[i] > have.QTY.loc[i]:
            q = int(np.ceil((needed.QTY.loc[i]-have.QTY.loc[i])/int(reactions.QTY.loc[i].iloc[0])))
            for j in elements:
                needed.QTY.loc[j] += int(reactions.loc[i].loc[j].iloc[0]) * q
                if j == 'ORE':
                    print('Need ',needed.QTY.loc[j],' ORE so far')
            have.QTY.loc[i] += int(reactions.QTY.loc[i].iloc[0]) * q
            

print(needed.loc['ORE'])

#%%
# Part 2 running (same input as part 1)
needed = pd.DataFrame(columns=['QTY'],index=elements)
needed.QTY = 0
needed.at['FUEL','QTY'] = 1000000000000//oreperfuel
have = pd.DataFrame(columns=['QTY'],index=elements)
have.QTY = 0
have.at['ORE','QTY'] = 1000000000000 

while needed.loc['ORE'].iloc[0] < have.at['ORE','QTY']:
    for i in chemicals:
        if needed.QTY.loc[i] > have.QTY.loc[i]:
            q = int(np.ceil((needed.QTY.loc[i]-have.QTY.loc[i])/int(reactions.QTY.loc[i].iloc[0])))
            for j in elements:
                needed.QTY.loc[j] += int(reactions.loc[i].loc[j].iloc[0]) * q
                if j == 'ORE':
                    print('Need ',needed.QTY.loc[j],' ORE so far')
            have.QTY.loc[i] += int(reactions.QTY.loc[i].iloc[0]) * q
    if np.all(needed <= have):
        q = (have.at['ORE','QTY'] - needed.at['ORE','QTY'])//oreperfuel
        print('Can make at least ',needed.at['FUEL','QTY'],' FUEL')
        if q == 0:
            break
        needed.at['FUEL','QTY'] += q
        

print(needed.loc['FUEL'])






















