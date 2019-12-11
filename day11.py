import numpy as np

#%%
#Intcode computer
def intcode(nums,pos,inval,base):
    opcode = nums[pos] % 100
    outval = 0
    #0=position mode, 1=immediate mode
    if opcode == 1:
        #Addition mode
        pars = [nums[pos+1],nums[pos+2],nums[pos+3]]
        mode = [int(nums[pos]/100)%10,int(nums[pos]/1000)%10,int(nums[pos]/10000)%10]
        if mode[0] == 0:
            pars[0] = nums[pars[0]]
        if mode[0] == 2:
            pars[0] = nums[base + pars[0]]
        if mode[1] == 0:
            pars[1] = nums[pars[1]]
        if mode[1] == 2:
            pars[1] = nums[base + pars[1]]
        if mode[2] == 2:
            pars[2] = base + pars[2]
        nums[pars[2]] = pars[0] + pars[1]
        pos = pos + 4
    elif opcode == 2:
        #Multiplication mode
        pars = [nums[pos+1],nums[pos+2],nums[pos+3]]
        mode = [int(nums[pos]/100)%10,int(nums[pos]/1000)%10,int(nums[pos]/10000)%10]
        if mode[0] == 0:
            pars[0] = nums[pars[0]]
        if mode[0] == 2:
            pars[0] = nums[base + pars[0]]
        if mode[1] == 0:
            pars[1] = nums[pars[1]]
        if mode[1] == 2:
            pars[1] = nums[base + pars[1]]
        if mode[2] == 2:
            pars[2] = base + pars[2]
        nums[pars[2]] = pars[0] * pars[1]        
        pos = pos + 4
    elif opcode == 3:
        #Write mode
        pars = [nums[pos+1]]
        mode = [int(nums[pos]/100)%10]
#        if mode[0] == 0:
#            pars[0] = nums[pars[0]]
        if mode[0] == 2:
            pars[0] = base + pars[0]
        nums[pars[0]] = inval
        pos = pos + 2
    elif opcode == 4:
        #Return mode
        pars = [nums[pos+1]]
        mode = [int(nums[pos]/100)%10]
        if mode[0] == 0:
            pars[0] = nums[pars[0]]
        if mode[0] == 2:
            pars[0] = nums[base + pars[0]]
        outval = pars[0]
#        print('Output value ',outval)
        pos = pos + 2
    elif opcode == 5:
        #Jump-if-true
        pars = [nums[pos+1],nums[pos+2]]
        mode = [int(nums[pos]/100)%10,int(nums[pos]/1000)%10]
        if mode[0] == 0:
            pars[0] = nums[pars[0]]
        if mode[0] == 2:
            pars[0] = nums[base + pars[0]]
        if mode[1] == 0:
            pars[1] = nums[pars[1]]
        if mode[1] == 2:
            pars[1] = nums[base + pars[1]]
        if pars[0] != 0:
            pos = pars[1]
        else:
            pos = pos + 3
    elif opcode == 6:
        #Jump-if-false
        pars = [nums[pos+1],nums[pos+2]]
        mode = [int(nums[pos]/100)%10,int(nums[pos]/1000)%10] 
        if mode[0] == 0:
            pars[0] = nums[pars[0]]
        if mode[0] == 2:
            pars[0] = nums[base + pars[0]]
        if mode[1] == 0:
            pars[1] = nums[pars[1]]
        if mode[1] == 2:
            pars[1] = nums[base + pars[1]]
        if pars[0] == 0:
            pos = pars[1]
        else:
            pos = pos + 3
    elif opcode == 7:
        #Less than
        pars = [nums[pos+1],nums[pos+2],nums[pos+3]]
        mode = [int(nums[pos]/100)%10,int(nums[pos]/1000)%10,int(nums[pos]/10000)%10]
        if mode[0] == 0:
            pars[0] = nums[pars[0]]
        if mode[0] == 2:
            pars[0] = nums[base + pars[0]]
        if mode[1] == 0:
            pars[1] = nums[pars[1]]
        if mode[1] == 2:
            pars[1] = nums[base + pars[1]]
        if mode[2] == 2:
            pars[2] = base + pars[2]
        if pars[0] < pars[1]:
            nums[pars[2]] = 1
        else:
            nums[pars[2]] = 0
        pos = pos + 4
    elif opcode == 8:
        #Equals
        pars = [nums[pos+1],nums[pos+2],nums[pos+3]]
        mode = [int(nums[pos]/100)%10,int(nums[pos]/1000)%10,int(nums[pos]/10000)%10]
        if mode[0] == 0:
            pars[0] = nums[pars[0]]
        if mode[0] == 2:
            pars[0] = nums[base + pars[0]]
        if mode[1] == 0:
            pars[1] = nums[pars[1]]
        if mode[1] == 2:
            pars[1] = nums[base + pars[1]]
        if mode[2] == 2:
            pars[2] = base + pars[2]
        if pars[0] == pars[1]:
            nums[pars[2]] = 1
        else:
            nums[pars[2]] = 0
        pos = pos + 4
    elif opcode == 9:
        #Adjust the base
        pars = [nums[pos+1]]
        mode = [int(nums[pos]/100)%10]
        if mode[0] == 0:
            pars[0] = nums[pars[0]]
        if mode[0] == 2:
            pars[0] = nums[base + pars[0]]
        base = base + pars[0]
        pos = pos + 2
    elif opcode == 99:
        pars = ['none']
        mode = ['none']
        pos = pos + 1
#        print('Program exit code 99')
    else:
        pars = ['none']
        mode = ['none']
#        print('Program exit: error code ',opcode)
#    print('OPCODE ',opcode,'  parameters ',pars,' modes ',mode, 'output ',outval,' base ',base)
    return nums,pos,opcode,outval,base

def new_direction(direction,turn):
    #left-hand turn
    if turn == 0:
        R = np.array(([0,-1],[1,0]))
    #Right-hand turn
    elif turn == 1:
        R = np.array(([0,1],[-1,0]))
    else:
        print('Error: invalid turn code')
        return direction
    direction = np.matmul(R,direction)
    return direction


#%%
#Part 1 testing
paint = np.zeros((200,200),dtype=int)
painted = np.zeros((200,200),dtype=int)
direction = np.array([0,1],dtype=int)
location = np.array([100,100],dtype=int)

#Start the opcode computer running
fname = 'day11input.txt'
nums = list(np.loadtxt(fname,delimiter=',',dtype=np.int64))
nums = nums + [0]*10000
pos = 0
opcode = 1
base = 0
outval = [0,0]

while opcode != 99:
    #Input value is the current paint colour
    inval = paint[tuple(location)]
    #Run the intcode to get the new paint colour
    opcode = 1
    while not opcode in [4,99]:
        nums,pos,opcode,newcolour,base = intcode(nums,pos,inval,base)
    if opcode == 99:
        break
    #Run the intcode to get the turn direction
    opcode = 1
    while not opcode in [4,99]:
        nums,pos,opcode,turn,base = intcode(nums,pos,inval,base)
    if opcode == 99:
        break
    #Carry out the painting and the turn
    paint[tuple(location)] = newcolour
    painted[tuple(location)] = 1
    direction = new_direction(direction,turn)
    location = location + direction
    
#%%
#Part 2
paint = np.zeros((200,200),dtype=int)
painted = np.zeros((200,200),dtype=int)
direction = np.array([0,1],dtype=int)
location = np.array([100,100],dtype=int)
paint[tuple(location)] = 1

#Start the opcode computer running
fname = 'day11input.txt'
nums = list(np.loadtxt(fname,delimiter=',',dtype=np.int64))
nums = nums + [0]*10000
pos = 0
opcode = 1
base = 0
outval = [0,0]

while opcode != 99:
    #Input value is the current paint colour
    inval = paint[tuple(location)]
    #Run the intcode to get the new paint colour
    opcode = 1
    while not opcode in [4,99]:
        nums,pos,opcode,newcolour,base = intcode(nums,pos,inval,base)
    if opcode == 99:
        break
    #Run the intcode to get the turn direction
    opcode = 1
    while not opcode in [4,99]:
        nums,pos,opcode,turn,base = intcode(nums,pos,inval,base)
    if opcode == 99:
        break
    #Carry out the painting and the turn
    paint[tuple(location)] = newcolour
    painted[tuple(location)] = 1
    direction = new_direction(direction,turn)
    location = location + direction

x = np.argwhere(np.sum(painted,axis=1)>0)
y = np.argwhere(np.sum(painted,axis=0)>0)
identifier = paint[np.min(x)-2:np.max(x)+2,np.min(y)-2:np.max(y)+2]

import matplotlib.pyplot as plt

plt.imshow(identifier)







