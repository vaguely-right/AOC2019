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
#        print('Output value ',outval)
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
#        print('Program exit code 99')
    else:
        pars = ['none']
        mode = ['none']
#        print('Program exit: error code ',opcode)
#    print('OPCODE ',opcode,'  parameters ',pars,' modes ',mode, 'output value ',outval)
    return nums,pos,opcode,outval

def amplifier(phase,inval,nums,pos):
    opcode = 1
    i = phase
    outval = 0
    while(opcode<=8):
        nums,pos,opcode,o = intcode(nums,pos,i)
        if opcode == 3:
            i = inval
        if opcode == 4:
            outval = o
            return outval,nums,pos
    return outval,nums,pos

#%%
#Testing
nums = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
phase = 9
signal = 0
amplifier(phase,signal,nums,0)


#%%
#Testing
day7test = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
phase = [4,3,2,1,0]
signal = 0

for p in phase:
    nums = day7test
    signal,n,pos = amplifier(p,signal,nums,0)
    print(signal)

#%%
#More testing
day7test = [3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0]
phase = [0,1,2,3,4]
signal = 0

for p in phase:
    nums = day7test
    signal,n,pos = amplifier(p,signal,nums,0)
    print('SIGNAL IS',signal)

#%%
#One more test
day7test = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]
phase = [1,0,4,3,2]
signal = 0

for p in phase:
    nums = day7test
    signal,nums,pos = amplifier(p,signal,nums,0)
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
        signal,n,pos = amplifier(0,p,signal,nums,0)
    outphase.append(phase)
    outsignal.append(signal)
        
print('MAX OUTPUT ',np.max(outsignal))
print('MAX OUTPUT PHASE ',outphase[np.argmax(outsignal)])

#%%
#Testing: feed it the max phase
fname = 'day7input.txt'
day7input = np.loadtxt(fname,delimiter=',',dtype=int)
phase = [1,0,3,4,2]
signal = 0
for p in phase:
    nums = list.copy(list(day7input))
    signal,nums,pos = amplifier(p,signal,nums,0)

print(signal)

#%%
#Part 2 example
day7example = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
phase = [9,8,7,6,5]
signal = 0
outval = 0
check = True
nums = []
pos = [int(i) for i in np.zeros(5)]
outval = [int(i) for i in np.zeros(5)]
for i in range(5):
    nums.append(day7example)
while check == True:
    for i in range(5):
        outval[i],nums[i],pos[i] = amplifier(phase[i],outval[i],nums[i],pos[i])
        print('AMP OUTPUT IS ',outval[i])
    signal = np.max(outval)
    phase = outval
    print('SIGNAL IS ',signal)
    if outval[4] == 0:
        check = False
print(signal)
#NOT WORKING YET

#%%
#More testing
day7example = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]
phase = [9,7,8,5,6]
signal = 0
outval = 0
check = True
nums = []
pos = [int(i) for i in np.zeros(5)]
for i in range(5):
    nums.append(list.copy(day7example))
while check == True:
    for i in range(5):
        signal,nums[i],pos[i] = amplifier(phase[i],signal,nums[i],pos[i])
        print('SIGNAL IS ',signal)
    if signal > outval :
        outval = signal
    print('OUTPUT IS ',outval)
    if signal == 0:
        check = False
print(outval)

#%%
#Totally rewriting Part 2
day7example = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]
phase = [[9,0],[7],[8],[5],[6]]
incount = [0,0,0,0,0]
pos = [int(i) for i in np.zeros(5)]
nums = []
for i in range(5):
    nums.append(list.copy(day7example))
#First, run through the first pass
opcode = 1
while(opcode!=99):
    for i in range(5):
        opcode = 1
        while (opcode!=4) and (opcode!=99):
            if incount[i] >= len(phase[i]):
                nums[i],pos[i],opcode,outval = intcode(nums[i],pos[i],0)
            else:
                nums[i],pos[i],opcode,outval = intcode(nums[i],pos[i],phase[i][incount[i]])                
            if opcode == 3:
                incount[i] += 1
            if opcode == 4:
                if i == 4:
                    phase[0].append(outval)
                else:
                    phase[i+1].append(outval)

print(np.max(np.max(phase)))


#%%
#Hey, that might have worked! Try another example.
day7example = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
phase = [[9,0],[8],[7],[6],[5]]
incount = [0,0,0,0,0]
pos = [int(i) for i in np.zeros(5)]
nums = []
for i in range(5):
    nums.append(list.copy(day7example))
#First, run through the first pass
opcode = 1
while(opcode!=99):
    for i in range(5):
        opcode = 1
        while (opcode!=4) and (opcode!=99):
            if incount[i] >= len(phase[i]):
                nums[i],pos[i],opcode,outval = intcode(nums[i],pos[i],0)
            else:
                nums[i],pos[i],opcode,outval = intcode(nums[i],pos[i],phase[i][incount[i]])                
            if opcode == 3:
                incount[i] += 1
            if opcode == 4:
                if i == 4:
                    phase[0].append(outval)
                else:
                    phase[i+1].append(outval)

print(np.max(np.max(phase)))

#%%
#Dude, it totally worked! Ok, for real this time.
fname = 'day7input.txt'
day7input = np.loadtxt(fname,delimiter=',',dtype=int)
outphase = []
outputs = []
#for p in it.permutations(range(5,10)):
for p in [[9,8,5,6,7]]:
    phase = [[p[0],0],[p[1]],[p[2]],[p[3]],[p[4]]]
    incount = [0,0,0,0,0]
    pos = [int(i) for i in np.zeros(5)]
    nums = []
    for i in range(5):
        nums.append(list.copy(list(day7input)))
    opcode = 1
    while(opcode!=99):
        for i in range(5):
            opcode = 1
            while (opcode!=4) and (opcode!=99):
                if incount[i] >= len(phase[i]):
                    nums[i],pos[i],opcode,outval = intcode(nums[i],pos[i],0)
                else:
                    nums[i],pos[i],opcode,outval = intcode(nums[i],pos[i],phase[i][incount[i]])                
                if opcode == 3:
                    incount[i] += 1
                if (opcode == 4) or (opcode == 99):
                    if i == 4:
                        phase[0].append(outval)
                    else:
                        phase[i+1].append(outval)
    outputs.append(np.max(np.max(phase)))
    outphase.append([i[0] for i in phase])

print('MAX OUTPUT IS ',np.max(outputs),' AT PHASE ',outphase[np.argmax(outputs)])

#Should be 69816958

