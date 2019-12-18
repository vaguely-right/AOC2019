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
        print('Program exit: error code ',opcode)
#    print('OPCODE ',opcode,'  parameters ',pars,' modes ',mode, 'output ',outval,' base ',base)
    return nums,pos,opcode,outval,base


#%%
#Example    
camera = '..#..........\n\
..#..........\n\
#######...###\n\
#.#...#...#.#\n\
#############\n\
..#...#...#..\n\
..#####...^..'

alignment = 0
camera = camera.split('\n')
for i in range(1,len(camera)-1):
    for j in range(1,len(camera[i])-1):
        if (all(x in ['<','>','^','v','#'] for x in [camera[i][j],camera[i-1][j],camera[i+1][j],camera[i][j-1],camera[i][j+1]])):
            alignment += i*j

print(alignment)

#Works!

#%%
#Part 1
fname = 'day17input.txt'
d17 = list(np.loadtxt(fname,delimiter=',',dtype=np.int64))

camera=''
nums = d17 + [0]*10000
pos = 0
opcode = 1
base = 0
inval = 0
while opcode != 99:
    nums,pos,opcode,outval,base = intcode(nums,pos,inval,base)
    if opcode == 4:
        camera += chr(outval)
    
alignment = 0
camera = camera.split('\n')[:-2]
for i in range(1,len(camera)-1):
    for j in range(1,len(camera[i])-1):
        if (all(x in ['<','>','^','v','#'] for x in [camera[i][j],camera[i-1][j],camera[i+1][j],camera[i][j-1],camera[i][j+1]])):
            alignment += i*j

print(alignment)

#%%









