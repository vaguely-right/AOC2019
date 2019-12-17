import numpy as np

#%%
#Example
insignal = np.fromiter([i for i in '12345678'],dtype=int)
pattern = np.array([0,1,0,-1])
nphases = 4
#Build the matrix to modify the input signal
fft = np.zeros((len(insignal),len(insignal)))
for i in range(len(insignal)):
    fft[i] = np.tile(np.repeat(pattern,i+1),len(insignal)//(len(pattern)*(i+1))+1)[1:len(insignal)+1]

signal = insignal
for phase in range(nphases):
    signal = abs(np.matmul(fft,signal))%10

#%%
#Example
insignal = np.fromiter([i for i in '80871224585914546619083218645595'],dtype=int)
pattern = np.array([0,1,0,-1])
nphases = 100
#Build the matrix to modify the input signal
fft = np.zeros((len(insignal),len(insignal)))
for i in range(len(insignal)):
    fft[i] = np.tile(np.repeat(pattern,i+1),len(insignal)//(len(pattern)*(i+1))+1)[1:len(insignal)+1]

signal = insignal
for phase in range(nphases):
    signal = abs(np.matmul(fft,signal))%10

print(signal[0:8])
#%%
#Part 1
fname = 'day16input.txt'
with open(fname) as f:
    day16input = f.read()[:-1]
insignal = np.fromiter([i for i in day16input],dtype=int)
pattern = np.array([0,1,0,-1])
nphases = 100
#Build the matrix to modify the input signal
fft = np.zeros((len(insignal),len(insignal)))
for i in range(len(insignal)):
    fft[i] = np.tile(np.repeat(pattern,i+1),len(insignal)//(len(pattern)*(i+1))+1)[1:len(insignal)+1]

signal = insignal
for phase in range(nphases):
    signal = abs(np.matmul(fft,signal))%10

print(signal[0:8])

#%%
#Part 2 example: Trying brute force
insignal = np.fromiter([i for i in '03036732577212944063491565474664'],dtype=int)
signal = np.tile(insignal,10000)
offset = int('03036732577212944063491565474664'[0:7])
pattern = np.array([0,1,0,-1])
nphases = 100
#Can't do it with a matrix; Memory error.
#fft = np.zeros((len(signal),len(signal)))
#for i in range(len(signal)):
#    fft[i] = np.tile(np.repeat(pattern,i+1),len(signal)//(len(pattern)*(i+1))+1)[1:len(signal)+1]

for phase in range(nphases):
    print('Phase ',phase)
    for i in range(len(signal)): 
        fft = np.tile(np.repeat(pattern,i+1),len(signal)//(len(pattern)*(i+1))+1)[1:len(signal)+1]
        signal[i] = abs(np.dot(fft,signal))%10
#    signal = abs(np.matmul(fft,signal))%10

print(signal[offset:offset+8])

#%%
#LOLnope to brute force
#It's a pattern with period 10000, which is a multiple of 4
#
insignal = np.fromiter([i for i in '03036732577212944063491565474664'],dtype=int)
offset = int('03036732577212944063491565474664'[0:7])%len(insignal)
pattern = np.array([0,1,0,-1])
nphases = 100
fft = np.zeros((len(insignal),len(insignal)))
for i in range(len(insignal)):
    fft[i] = np.tile(np.repeat(pattern,i+1),len(insignal)//(len(pattern)*(i+1))+1)[1:len(insignal)+1]
signal = np.copy(insignal)
for phase in range(nphases):
    newsignal = np.zeros(np.shape(signal))
    for i in range(10000):
        newsignal += np.matmul(fft,signal)
    signal = abs(signal)%10

print(np.tile(signal,2)[offset:offset+8])
#Doesn't work; didn't account for the increasing length of the pattern

#%%
#

#%%
#Part 2
#Try brute force? Doubt it.
fname = 'day16input.txt'
with open(fname) as f:
    day16input = f.read()[:-1]
insignal = np.fromiter([i for i in day16input],dtype=int)
signal = np.tile(insignal,10000)
offset = int(day16input[0:7])
























