import numpy as np
import re
import math

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


#%%
#Back to Part 1, reading a regular expression this time
fname = 'day12example.txt'
with open(fname,'r') as f:
    d12ex = f.read().split('\n')[:-1]

pos = np.array([[int(k) for k in j] for j in [re.findall('[-]?[0-9]+',i) for i in d12ex]])
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
#Part 1 for real, with regular expressions
fname = 'day12input.txt'
with open(fname,'r') as f:
    d12 = f.read().split('\n')[:-1]
pos = np.array([[int(k) for k in j] for j in [re.findall('[-]?[0-9]+',i) for i in d12]])
path = np.zeros((4,3,1))
path[:,:,0] = pos
vel = np.zeros((4,3))
for steps in range(1000):
    #Calculate gravity
    for i in range(4):
        for j in range(4):
            vel[i] = vel[i] + (pos[i] < pos[j]) - (pos[i] > pos[j])
    #Apply gravity
    for i in range(4):
        pos[i] = pos[i] + vel[i]
    path =  np.append(path,np.atleast_3d(pos),axis=2)

pot = np.sum(np.abs(pos),axis=1)
kin = np.sum(np.abs(vel),axis=1)
tot = pot * kin
energy = np.sum(tot)
print(energy)

#Got it!

#%%
#Plotting
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure(figsize=(12,10))
ax = fig.add_subplot(111,projection='3d')
for i in range(4):
    plt.plot(path[i,0,:],path[i,1,:],path[i,2,:])
plt.show()

#%%
#Part 2
#Split the problem into each axis
fname = 'day12example2.txt'
with open(fname,'r') as f:
    d12 = f.read().split('\n')[:-1]
inpos = np.array([[int(k) for k in j] for j in [re.findall('[-]?[0-9]+',i) for i in d12]])
invel = np.zeros((4,3),dtype=int)

steps = np.zeros((3),dtype=np.int64)

for dim in range(3):
    print('dimension ',dim)
    pos = inpos[:,dim]
    vel = np.zeros((4))
    while True:
        #Calculate gravity
        for i in range(4):
            for j in range(4):
                vel[i] = vel[i] + (pos[i] < pos[j]) - (pos[i] > pos[j])
        #Apply gravity
        for i in range(4):
            pos[i] = pos[i] + vel[i]
        steps[dim] += 1
        if (np.all(pos == inpos[:,dim])) and (np.all(vel == np.zeros(4))):
            break
        if steps[dim]%10000 == 0:
            print('step ',steps[dim])

#Find the least common multiple of the three cycle periods
nsteps = np.lcm(np.lcm(steps[0],steps[1]),steps[2])
print(nsteps*2)

#%%
#Part 2 for real
fname = 'day12input.txt'
with open(fname,'r') as f:
    d12 = f.read().split('\n')[:-1]
inpos = np.array([[int(k) for k in j] for j in [re.findall('[-]?[0-9]+',i) for i in d12]])
invel = np.zeros((4,3),dtype=int)

steps = np.zeros((3),dtype=np.int64)

for dim in range(3):
    print('dimension ',dim)
    pos = inpos[:,dim]
    vel = np.zeros((4))
    while True:
        #Calculate gravity
        for i in range(4):
            for j in range(4):
                vel[i] = vel[i] + (pos[i] < pos[j]) - (pos[i] > pos[j])
        #Apply gravity
        for i in range(4):
            pos[i] = pos[i] + vel[i]
        steps[dim] += 1
        if (np.all(pos == inpos[:,dim])) and (np.all(vel == np.zeros(4))):
            break
        if steps[dim]%10000 == 0:
            print('step ',steps[dim])

#Find the least common multiple of the three cycle periods
nsteps = np.lcm(np.lcm(steps[0],steps[1]),steps[2])
print(nsteps*2)

