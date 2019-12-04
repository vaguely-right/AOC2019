lower = 246540
upper = 787419


#Part 1
#Set the count to zero
part1 = 0
part2 = 0

#Loop over the possible passwords
for pwd in range(lower,upper):
#Set the initial condition as False
    check = False
    txt = str(pwd)
#Check that the digits are all increasing
    for i in range(1,len(txt)):
        if int(txt[i]) >= int(txt[i-1]):
#Check if there is a run of consecutive digits
            if int(txt[i]) == int(txt[i-1]):
                check = True
        else:
            check = False
            break
    if check:
        part1 += 1
#Check if there is a run of exactly two digits
        check = False
        for i in range(1,(len(txt)-1)):
            if ((int(txt[i-1])==int(txt[i])) or (int(txt[i])==int(txt[i+1]))) and (int(txt[i-1])!=int(txt[i+1])):
                check = True
                break
            else:
                check = False
        if check:
            part2 += 1
    
print(part1)
print(part2)


