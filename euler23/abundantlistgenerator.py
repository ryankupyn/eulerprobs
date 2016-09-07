def isabundant(num):
    total = 0
    abundant = 0
    for hop in range(1,int(num/2)+1):
        if num % hop == 0:
            total += hop
    if total > num:
        abundant = 1
    return abundant

def abundantlister(maxnum):
    abundantlist = []
    for testnum in range(maxnum + 1):
        if isabundant(testnum):
            abundantlist.append(testnum)
    return abundantlist
