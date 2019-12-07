import numpy as np
import os
os.chdir('AOC2019')
import itertools as it

#%%
#The intcode functions
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
        outval = pars[0]
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
    print('OPCODE ',opcode,'  parameters ',pars,' modes ',mode, 'output value ',outval)
    return nums,pos,opcode,outval

def amplifier(phase,inval,nums):
    pos = 0
    opcode = 1
    i = phase
    while(opcode<=8):
        nums,pos,opcode,o = intcode(nums,pos,i)
        if opcode == 3:
            i = inval
        if opcode == 4:
            outval = o
    return outval,nums

#%%
#Testing
nums = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
phase = 9
signal = 0
amplifier(phase,signal,nums)


#%%
#Testing
day7test = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
phase = [4,3,2,1,0]
signal = 0

for p in phase:
    nums = day7test
    signal = amplifier(p,signal,nums)
    print(signal)

#%%
#More testing
day7test = [3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0]
phase = [0,1,2,3,4]
signal = 0

for p in phase:
    nums = day7test
    signal = amplifier(p,signal,nums)
    print('SIGNAL IS',signal)

#%%
#One more test
day7test = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]
phase = [1,0,4,3,2]
signal = 0

for p in phase:
    nums = day7test
    signal,nums = amplifier(p,signal,nums)
    print('SIGNAL IS',signal)

#%%
#For real this time, Part 1
fname = 'day7input.txt'
day7input = np.loadtxt(fname,delimiter=',',dtype=int)
outphase = []
outsignal = []
for phase in it.permutations(range(5)):
    signal = 0
    for p in phase:
        nums = day7input
        signal = amplifier(p,signal,nums)
    outphase.append(phase)
    outsignal.append(signal)
        
print(np.max(outsignal))

#%%
#Part 2 example
day7example = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
phase = [9,8,7,6,5]
signal = 0
outval = 0
nums = []
for i in range(5):
    nums.append(day7example)
while signal == outval:
    for p,n in zip(phase,nums):
        signal,n = amplifier(p,signal,n)
        print('SIGNAL IS',signal)
    if signal == outval:
        break
    if signal > outval :
        outval = signal








