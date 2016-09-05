import Amicablechecker as am

sumrange = 0

for num in range(1,10001):
    if num == am.factorsum(am.factorsum(num)) and num != am.factorsum(num):
        print(num)
        sumrange += num
print(sumrange)
