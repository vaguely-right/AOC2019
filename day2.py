import numpy as np
import os
os.chdir('AOC2019')

#%%
#Part 1
def intcode(nums,pos):
    opcode = nums[pos]
    if opcode == 1:
        nums[nums[pos+3]] = nums[nums[pos+1]] + nums[nums[pos+2]]
        pos = pos + 4
        return nums,pos,opcode
    elif opcode == 2:
        nums[nums[pos+3]] = nums[nums[pos+1]] * nums[nums[pos+2]]
        pos = pos + 4
        return nums,pos,opcode
    elif opcode == 99:
        print('Program exit code 99')
        return nums,pos,opcode
    else:
        print('Program exit: error code ',opcode)
        return nums,pos,opcode

#%%
#Run an example first
day2example = [1,9,10,3,2,3,11,0,99,30,40,50]
nums = list.copy(day2example)
opcode = 1
pos = 0

while opcode in [1,2]:
    nums,pos,opcode = intcode(nums,pos)

#%%
#For real now
fname = 'day2input.txt'
nums = np.loadtxt(fname,delimiter=',',dtype=int)
opcode = 1
pos = 0

nums[1] = 12
nums[2] = 2


while opcode in [1,2]:
    nums,pos,opcode = intcode(nums,pos)

#%%
#Part 2
fname = 'day2input.txt'
day2input = np.loadtxt(fname,delimiter=',',dtype=int)

for noun in range(100):
    for verb in range(100):
        memory = np.copy(day2input)
        opcode = 1
        pointer = 0
        memory[1] = noun
        memory[2] = verb
        while opcode in [1,2]:
            memory,pointer,opcode = intcode(memory,pointer)
        if memory[0] == 19690720:
            break
    else:
        continue
    break

print(noun,verb)
day2answer = 100 * noun + verb
print('Day2 Part 2 answser is: ',day2answer)











