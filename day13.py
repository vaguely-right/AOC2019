import numpy as np
import matplotlib.pyplot as plt

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
        print('Program exit: error code ',opcode)
#    print('OPCODE ',opcode,'  parameters ',pars,' modes ',mode, 'output ',outval,' base ',base)
    return nums,pos,opcode,outval,base

#%%
#Part 1
fname = 'day13input.txt'
nums = list(np.loadtxt(fname,delimiter=',',dtype=np.int64))
tiles = np.zeros((1000,1000))
nums = nums + [0]*10000
pos = 0
opcode = 1
base = 0
inval = 0
move = np.zeros((3),dtype=int)
ball = np.zeros((1),dtype=int)
paddle = np.zeros((1),dtype=int)
while opcode in [1,2,3,4,5,6,7,8,9]:
    for i in range(3):
        opcode = 1
        while opcode in [1,2,3,5,6,7,8,9]:
            nums,pos,opcode,outval,base = intcode(nums,pos,inval,base)
        move[i] = outval
    tiles[move[1],move[0]] = move[2]
    print('Tile ',move[0],move[1],' = ',move[2])

np.sum(tiles==2)
plt.imshow(tiles[0:20,0:40],vmin=0,vmax=4)

#%%
#Part 2
fname = 'day13input.txt'
nums = list(np.loadtxt(fname,delimiter=',',dtype=np.int64))
nums[0] = 2
tiles = np.zeros((20,40))
nums = nums + [0]*10000
pos = 0
opcode = 1
base = 0
inval = 1
move = np.zeros((3),dtype=int)
display = []
#First, set up the game (go until an input is needed)
while opcode in [1,2,4,5,6,7,8,9]:
    for i in range(3):
        opcode = 1
        while opcode in [1,2,3,5,6,7,8,9]:
            nums,pos,opcode,outval,base = intcode(nums,pos,inval,base)
        move[i] = outval
        tiles[move[1],move[0]] = move[2]
        #Update the paddle location
        if move[2] == 3:
            paddle = move[0]
        #Update the ball location
        if move[2] == 4:
            ball = move[0]
        if ball > paddle:
            inval = 1
        if ball < paddle:
            inval = -1
#Now play the game
if ball > paddle:
    inval = 1
if ball < paddle:
    inval = -1
while opcode in [1,2,4,5,6,7,8,9]:
    for i in range(3):
        opcode = 1
        while opcode in [1,2,3,5,6,7,8,9]:
            nums,pos,opcode,outval,base = intcode(nums,pos,inval,base)
        move[i] = outval
    if (move[0 == -1]) and (move[1] == 0):
        display.append(move[2])
    else:
        tiles[move[1],move[0]] = move[2]
        #Update the paddle location
        if move[2] == 3:
            paddle = move[0]
        #Update the ball location
        if move[2] == 4:
            ball = move[0]
        if ball > paddle:
            inval = 1
        if ball < paddle:
            inval = -1
    if np.sum(tiles==2) == 0:
        break



import matplotlib.pyplot as plt

plt.imshow(tiles,vmin=0,vmax=4)



