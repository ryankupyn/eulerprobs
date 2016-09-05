import math
def factorsum(num):
    total = 0
    for hop in range(1,int(num/2)+1):
        if num % hop == 0:
            total += hop
    return total
