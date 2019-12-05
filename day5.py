import numpy as np
import os
os.chdir('AOC2019')

#%%
#Part 1
def intcode(nums,pos,inval):
    opcode = nums[pos] % 100
    mode = [int(nums[pos]/100),int(nums[pos]/1000),int(nums[pos]/10000)]
    #0=position mode, 1=immediate mode
    outval = 0
    if opcode == 1:
        #Addition mode
        pars = [nums[pos+1],nums[pos+2],nums[pos+3]]
        if mode[0] == 0:
            pars[0] = nums[pars[0]]
        if mode[1] == 0:
            pars[1] = nums[pars[1]]
        nums[pars[2]] = pars[0] + pars[1]
        pos = pos + 4
        return nums,pos,opcode,outval
    elif opcode == 2:
        #Multiplication mode
        pars = [nums[pos+1],nums[pos+2],nums[pos+3]]
        if mode[0] == 0:
            pars[0] = nums[pars[0]]
        if mode[1] == 0:
            pars[1] = nums[pars[1]]
        nums[pars[2]] = pars[0] * pars[1]        
        pos = pos + 4
        return nums,pos,opcode,outval
    elif opcode == 3:
        #Write mode
        pars = nums[pos+1]
        nums[pars] = inval
        pos = pos + 2
        return nums,pos,opcode,outval
    elif opcode == 4:
        #Return mode
        pars = nums[pos+1]
        if mode[0] == 0:
            pars = nums[pars]
        outval == pars
        pos = pos + 2
        print('Output value ',outval)
        return nums,pos,opcode,outval
    elif opcode == 99:
        pos = pos + 1
        print('Program exit code 99')
        return nums,pos,opcode,outval
    else:
        print('Program exit: error code ',opcode)
        return nums,pos,opcode,outval

#%%
fname = 'day5input.txt'
nums = np.loadtxt(fname,delimiter=',',dtype=int)
val = 1
pos = 0
opcode = 1
count = 0
while (opcode in [1,2,3,4]):
    count += 1
    nums,pos,opcode,val = intcode(nums,pos,val)
    print('OPCODE = ',opcode)









