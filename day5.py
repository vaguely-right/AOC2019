import numpy as np
import os
os.chdir('AOC2019')

#%%
#Part 1
def intcode(nums,pos,inval):
    opcode = nums[pos] % 100
    outval = 0
    #0=position mode, 1=immediate mode
    if opcode == 1:
        #Addition mode
        pars = [nums[pos+1],nums[pos+2],nums[pos+3]]
        mode = [int(nums[pos]/100)%10,int(nums[pos]/1000)%10,int(nums[pos]/10000)%10]
        if mode[0] == 0:
            pars[0] = nums[pars[0]]
        if mode[1] == 0:
            pars[1] = nums[pars[1]]
        nums[pars[2]] = pars[0] + pars[1]
        pos = pos + 4
    elif opcode == 2:
        #Multiplication mode
        pars = [nums[pos+1],nums[pos+2],nums[pos+3]]
        mode = [int(nums[pos]/100)%10,int(nums[pos]/1000)%10,int(nums[pos]/10000)%10]
        if mode[0] == 0:
            pars[0] = nums[pars[0]]
        if mode[1] == 0:
            pars[1] = nums[pars[1]]
        nums[pars[2]] = pars[0] * pars[1]        
        pos = pos + 4
    elif opcode == 3:
        #Write mode
        pars = [nums[pos+1]]
        mode = [int(nums[pos]/100)%10]
        nums[pars[0]] = inval
        pos = pos + 2
    elif opcode == 4:
        #Return mode
        pars = [nums[pos+1]]
        mode = [int(nums[pos]/100)]
        if mode[0] == 0:
            pars[0] = nums[pars[0]]
        outval == pars[0]
        print('Output value ',outval)
        pos = pos + 2
    elif opcode == 5:
        #Jump-if-true
        pars = [nums[pos+1],nums[pos+2]]
        mode = [int(nums[pos]/100)%10,int(nums[pos]/1000)%10]
        if mode[0] == 0:
            pars[0] = nums[pars[0]]
        if mode[1] == 0:
            pars[1] = nums[pars[1]]
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
        if mode[1] == 0:
            pars[1] = nums[pars[1]]
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
        if mode[1] == 0:
            pars[1] = nums[pars[1]]
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
        if mode[1] == 0:
            pars[1] = nums[pars[1]]
        if pars[0] == pars[1]:
            nums[pars[2]] = 1
        else:
            nums[pars[2]] = 0
        pos = pos + 4
    elif opcode == 99:
        pars = ['none']
        mode = ['none']
        pos = pos + 1
        print('Program exit code 99')
    else:
        pars = ['none']
        mode = ['none']
        print('Program exit: error code ',opcode)
    print('OPCODE ',opcode,'  parameters ',pars,' modes ',mode)
    return nums,pos,opcode

#%%
#Test: check the day 2 examples
day2example = [1,9,10,3,2,3,11,0,99,30,40,50]
nums = list.copy(day2example)
opcode = 1
pos = 0
inval = 1

while opcode in [1,2,3,4]:
    nums,pos,opcode = intcode(nums,pos,inval)

#%%
day2example = [1,1,1,4,99,5,6,0,99]
nums = list.copy(day2example)
opcode = 1
pos = 0
inval = 1

while opcode in [1,2,3,4]:
    nums,pos,opcode = intcode(nums,pos,inval)

#%%
fname = 'day2input.txt'
nums = np.loadtxt(fname,delimiter=',',dtype=int)
opcode = 1
pos = 0
inval = 1

nums[1] = 12
nums[2] = 2

while opcode in [1,2,3,4]:
    nums,pos,opcode = intcode(nums,pos,inval)

print(nums[0])
#%%
#Sovling part 1
fname = 'day5input.txt'
nums = np.loadtxt(fname,delimiter=',',dtype=int)
inval = 1
pos = 0
opcode = 1
count = 0
while (opcode in [1,2,3,4]):
    count += 1
    nums,pos,opcode = intcode(nums,pos,inval)

#%%
#Part 2 examples
nums = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
inval = 9
pos = 0
opcode = 1
while(opcode<=8):
    nums,pos,opcode = intcode(nums,pos,inval)

#%%
#Part 2 for real
fname = 'day5input.txt'
nums = np.loadtxt(fname,delimiter=',',dtype=int)
inval = 5
pos = 0
opcode = 1
while(opcode<=8):
    nums,pos,opcode = intcode(nums,pos,inval)














