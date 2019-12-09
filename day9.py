import numpy as np
import os
os.chdir('AOC2019')

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

#%%
#Testing
nums = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
numsext = nums + ([0] * 10000)
outs = []
pos = 0
opcode = 1
inval = 0
outval = 0
base = 0
while opcode != 99:
    numsext,pos,opcode,outval,base = intcode(numsext,pos,inval,base)
    if opcode == 4:
        outs.append(outval)

nums = numsext[0:len(nums)]
print('INPUT: ',nums)
print('OUTPUT: ',outs)

#%%
#Testing again
nums = [1102,34915192,34915192,7,4,7,99,0]
numsext = nums + ([0] * 10000)
pos = 0
opcode = 1
inval = 0
outval = 0
base = 0
while opcode != 4:
    numsext,pos,opcode,outval,base = intcode(numsext,pos,inval,base)

nums = numsext[0:len(nums)]
print(outval)

#%%
nums = [104,1125899906842624,99]
numsext = nums + ([0] * 10000)
pos = 0
opcode = 1
inval = 0
outval = 0
base = 0
while opcode != 4:
    numsext,pos,opcode,outval,base = intcode(numsext,pos,inval,base)

nums = numsext[0:len(nums)]
print(outval)

#%%
#Ok, working (?). Try Part 1 now
fname = 'day9input.txt'
day9input = list(np.loadtxt(fname,delimiter=',',dtype=int))
#with open(fname,'r') as f:
#    day9input = f.read()[:-1].split(sep=',')
#f.close()
day9input = [int(i) for i in day9input]
nums = day9input + ([0] * 10000)
pos = 0
opcode = 1
inval = 1
outval = 0
base = 0
outs = []
while opcode in [1,2,3,4,5,6,7,8,9]:
    nums,pos,opcode,outval,base = intcode(nums,pos,inval,base)
    if opcode == 4:
        outs.append(outval)

day9output = nums[0:len(day9input)]
print(outval)

#%%
#Testing the day 5 input to check
fname = 'day5input.txt'
nums = list(np.loadtxt(fname,delimiter=',',dtype=int))
inval = 5
pos = 0
opcode = 1
base = 0
while not opcode in [99]:
    nums,pos,opcode,outval,base = intcode(nums,pos,inval,base)

#Yep, it works

#%%
#Trying Day 2 again to check
fname = 'day2input.txt'
nums = list(np.loadtxt(fname,delimiter=',',dtype=int))
nums[1] = 12
nums[2] = 2
pos = 0
inval = 0
opcode = 1
while not opcode in [99]:
    nums,pos,opcode,outval,base = intcode(nums,pos,inval,base)

print(nums[0])
#Yep, works.

#%%
#Running part 2
fname = 'day9input.txt'
day9input = list(np.loadtxt(fname,delimiter=',',dtype=int))
#with open(fname,'r') as f:
#    day9input = f.read()[:-1].split(sep=',')
#f.close()
day9input = [int(i) for i in day9input]
nums = day9input + ([0] * 10000)
pos = 0
opcode = 1
inval = 2
outval = 0
base = 0
outs = []
while opcode in [1,2,3,4,5,6,7,8,9]:
    nums,pos,opcode,outval,base = intcode(nums,pos,inval,base)
    if opcode == 4:
        outs.append(outval)

day9output = nums[0:len(day9input)]
print(outval)












