import numpy as np
import pandas as pd

#%%
#Testing
fname = 'day10example.txt'
with open(fname,'r') as f:
    day10example = f.read().split(sep='\n')
f.close()
ny = len(day10example)
nx = len(day10example[0])
asteroids = []
for y in range(ny):
    for x in range(nx):
        if day10example[y][x] == '#':
            asteroids.append((float(x),float(y)))
angle = np.zeros((len(asteroids),len(asteroids)))
for i in range(len(asteroids)):
    for j in range(len(asteroids)):
        angle[i,j] = np.arctan2((asteroids[j][1]-asteroids[i][1]),(asteroids[j][0]-asteroids[i][0]))
len(np.unique(angle,axis=0))
u = [len(np.unique(i)) for i in angle]
np.max(u)
maxa = np.argmax(u)
maxc = asteroids[np.argmax(u)]
print(np.max(u))
#%%
fname = 'day10input.txt'
with open(fname,'r') as f:
    day10input = f.read().split(sep='\n')
f.close()
ny = len(day10input)-1
nx = len(day10input[0])
asteroids = []
for y in range(ny):
    for x in range(nx):
        if day10input[y][x] == '#':
            asteroids.append((float(x),float(y)))
angle = np.zeros((len(asteroids),len(asteroids)))
for i in range(len(asteroids)):
    for j in range(len(asteroids)):
        angle[i,j] = np.arctan2((asteroids[j][1]-asteroids[i][1]),(asteroids[j][0]-asteroids[i][0]))
len(np.unique(angle,axis=0))
u = [len(np.unique(i)) for i in angle]
np.max(u)
maxa = np.argmax(u)
maxc = asteroids[np.argmax(u)]
print(np.max(u))
#%%
#Part 2 example
laser = np.zeros(len(asteroids))
for i in range(len(laser)):
    laser[i] = np.arctan2((asteroids[i][0]-maxc[0]),(maxc[1]-asteroids[i][1]))
laser = np.where(laser<0,2.0*np.pi+laser,laser)
asteroid200 = np.unique(laser)[199]
coords200 = np.array(asteroids)[np.isin(laser,asteroid200)]
answer = np.array(asteroids)[np.isin(laser,asteroid200)][0][0] * 100 + np.array(asteroids)[np.isin(laser,asteroid200)][0][1]
print(coords200)
print(answer)

#%%
#Rewriting into Pandas for some testing of Part 2
fname = 'day10example.txt'
with open(fname,'r') as f:
    day10example = f.read().split(sep='\n')
f.close()
ny = len(day10example)
nx = len(day10example[0])
ax = []
ay = []
for y in range(ny):
    for x in range(nx):
        if day10example[y][x] == '#':
            ax.append(float(x))
            ay.append(float(y))
asteroids = pd.DataFrame({'x':ax,'y':ay})
asteroids['laser'] = np.arctan2(asteroids.x-maxc[0],maxc[1]-asteroids.y)
asteroids.laser[asteroids.laser<0] = 2.0*np.pi+asteroids.laser
asteroids['vaporized'] = [np.argwhere(np.sort(asteroids.laser.unique())==i)[0][0] for i in asteroids.laser]
asteroids[asteroids.vaporized==199]
#Got it!

#%%
#Back to using numpy, and for real this time
laser = np.zeros(len(asteroids))
for i in range(len(laser)):
    laser[i] = np.arctan2((asteroids[i][0]-maxc[0]),(maxc[1]-asteroids[i][1]))
laser = np.where(laser<0,2.0*np.pi+laser,laser)
asteroid200 = np.unique(laser)[199]
coords200 = np.array(asteroids)[np.isin(laser,asteroid200)]
print(coords200)
dist200 = [np.linalg.norm(i-maxc) for i in coords200]
acoords = coords200[np.argmin(dist200)]
answer = 100 * acoords[0] + acoords[1]
print(answer)

#%%
#Plotting, just for fun
import matplotlib.pyplot as plt
plt.scatter([i[0] for i in asteroids],[i[1] for i in asteroids])
plt.gca().invert_yaxis()

#%%
#Bring Part 2 into Pandas to do some stuff
fname = 'day10input.txt'
with open(fname,'r') as f:
    day10input = f.read().split(sep='\n')
f.close()
ny = len(day10input)-1
nx = len(day10input[0])
ax = []
ay = []
for y in range(ny):
    for x in range(nx):
        if day10input[y][x] == '#':
            ax.append(float(x))
            ay.append(float(y))

maxc = [20.0,21.0]
maxa = 292
asteroids = pd.DataFrame({'x':ax,'y':ay})
asteroids['dist'] = np.sqrt(( (asteroids.x-maxc[0])**2 + (asteroids.y-maxc[1])**2 ))
asteroids['angle'] = np.arctan2(asteroids.x-maxc[0],maxc[1]-asteroids.y)
asteroids.angle[asteroids.angle<0] = 2.0*np.pi+asteroids.angle
#asteroids['vaporized'] = [np.argwhere(np.sort(asteroids.angle.unique())==i)[0][0] for i in asteroids.angle]


vap = asteroids.copy().drop(columns=['x','y']).groupby('angle').min().reset_index()
vap['vaporized'] = [np.argwhere(np.sort(vap.angle.unique())==i)[0][0] for i in vap.angle]
asteroids = pd.merge(asteroids,vap.groupby('angle').min(),how='left',on=['angle','dist'])
asteroids.vaporized[asteroids.vaporized.isna()] = 248

asteroids.plot.scatter('x','y',c='vaporized',colormap='rainbow')
plt.scatter(maxc[0],maxc[1],marker='o',s=200)
plt.gca().invert_yaxis()








