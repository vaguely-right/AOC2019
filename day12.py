import numpy as np

#%%
# Part 1 example
fname = 'day12example.txt'
with open(fname,'r') as f:
    d12ex = f.read().split('\n')
d12ex = [i.split('=') for i in d12ex]
d12ex = [i.split(',') for l in d12ex for i in l]
d12ex = [i for l in d12ex for i in l]
d12ex[i.isnumeric() for i in d12ex]
np.array(d12ex)[i.isnumeric() for i in d12ex]

<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>
#%%
#Ok, try the example again
pos = np.array([[-1,0,2],[2,-10,-7],[4,-8,8],[3,5,-1]])
vel = np.zeros((4,3))
for steps in range(10):
    #Calculate gravity
    for i in range(4):
        for j in range(4):
            vel[i] = vel[i] + (pos[i] < pos[j]) - (pos[i] > pos[j])
    #Apply gravity
    for i in range(4):
        pos[i] = pos[i] + vel[i]

pot = np.sum(np.abs(pos),axis=1)
kin = np.sum(np.abs(vel),axis=1)
tot = pot * kin
energy = np.sum(tot)
print(energy)

#%%
#Second example
pos = np.array([[-8,-10,0],[5,5,10],[2,-7,3],[9,-8,-3]])
vel = np.zeros((4,3))
for steps in range(100):
    #Calculate gravity
    for i in range(4):
        for j in range(4):
            vel[i] = vel[i] + (pos[i] < pos[j]) - (pos[i] > pos[j])
    #Apply gravity
    for i in range(4):
        pos[i] = pos[i] + vel[i]

pot = np.sum(np.abs(pos),axis=1)
kin = np.sum(np.abs(vel),axis=1)
tot = pot * kin
energy = np.sum(tot)
print(energy)

#%%
#Part 1 for real
pos = np.array([[0,4,0],[-10,-6,-14],[9,-16,-3],[6,-1,2]])
vel = np.zeros((4,3))
for steps in range(1000):
    #Calculate gravity
    for i in range(4):
        for j in range(4):
            vel[i] = vel[i] + (pos[i] < pos[j]) - (pos[i] > pos[j])
    #Apply gravity
    for i in range(4):
        pos[i] = pos[i] + vel[i]

pot = np.sum(np.abs(pos),axis=1)
kin = np.sum(np.abs(vel),axis=1)
tot = pot * kin
energy = np.sum(tot)
print(energy)
















