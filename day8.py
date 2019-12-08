import os
os.chdir('AOC2019')
import numpy as np

#%%
nx = 25
ny = 6

fname = 'day8input.txt'
file = open(fname,'r')
day8input = file.read()
#Drop the newline character
day8input = day8input[:-1]
nz = int(len(day8input)/nx/ny)

image = np.zeros((nx,ny,nz),dtype=int)

i = 0
for z in range(nz):
    for y in range(ny):
        for x in range(nx):
            image[x,y,z] = day8input[i]
            i += 1

#Count the nonzero digits by layer
nonzeros = np.sum(np.sum(np.isin(image,[0],invert=True),axis=0),axis=0)
maxlayer = np.argmax(nonzeros)

#Get the number of ones per layer multiplied by the number of twos per layer
np.sum(np.sum(np.isin(image,[1]),axis=0),axis=0)[maxlayer] * np.sum(np.sum(np.isin(image,[2]),axis=0),axis=0)[maxlayer]


#%%
#Part 2
finalimage = np.zeros((25,6))
for y in range(ny):
    for x in range(nx):
        for z in range(nz):
            if image[x,y,z] == 2:
                continue
            else:
                finalimage[x,y] = image[x,y,z]
                break

import matplotlib.pyplot as plt
plt.imshow(np.transpose(finalimage))

