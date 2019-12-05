import numpy as np
import os
os.chdir('AOC2019')

#%%
def get_path(wire):
    path = list()
    x,y = 0,0
    for i in range(len(wire)):
        direction = wire[i][0]
        distance = int(wire[i][1:])
        for j in range(distance):
            if direction == 'R':
                x = x + 1
            elif direction == 'L':
                x = x - 1
            elif direction == 'U':
                y = y + 1
            elif direction == 'D':
                y = y - 1
            path.append((x,y))
    return path
        
#%%
#Example
ex1 = [['R75','D30','R83','U83','L12','D49','R71','U7','L72'],['U62','R66','U55','R34','D71','R55','D58','R83']]
#This should give an answer of 159
path1 = get_path(ex1[0])
path2 = get_path(ex1[1])
cross = list(set(path1).intersection(path2))
dist = np.min(np.sum(np.abs(cross),axis=1))


ex2 = [['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51'],['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7']]
#This should give an answer of 135
path1 = get_path(ex2[0])
path2 = get_path(ex2[1])
cross = list(set(path1).intersection(path2))
dist = np.min(np.sum(np.abs(cross),axis=1))


#%%
#Part 1
fname = 'day3input.txt'
day3input = list(np.loadtxt(fname,delimiter=',',dtype=str))
path1 = get_path(day3input[0])
path2 = get_path(day3input[1])
cross = list(set(path1).intersection(path2))
dist = np.min(np.sum(np.abs(cross),axis=1))
print(dist)

#%%
#Part 2 example
path1 = get_path(ex1[0])
path2 = get_path(ex1[1])
cross = list(set(path1).intersection(path2))
dist = np.min(np.sum(np.abs(cross),axis=1))
steps1 = [path1.index(i) for i in cross]
steps2 = [path2.index(i) for i in cross]
steps = np.min(np.add(steps1,steps2)) + 2
print(steps)


path1 = get_path(ex2[0])
path2 = get_path(ex2[1])
cross = list(set(path1).intersection(path2))
dist = np.min(np.sum(np.abs(cross),axis=1))
steps1 = [path1.index(i) for i in cross]
steps2 = [path2.index(i) for i in cross]
steps = np.min(np.add(steps1,steps2)) + 2
print(steps)

#%%
#Part 2
steps1 = [path1.index(i) for i in cross]
steps2 = [path2.index(i) for i in cross]
steps = np.min(np.add(steps1,steps2)) + 2
print(steps)

#%%
#Plotting the wire paths, just because
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = (12,8) 

plt.plot([i[0] for i in path1],[i[1] for i in path1])
plt.plot([i[0] for i in path2],[i[1] for i in path2])
















