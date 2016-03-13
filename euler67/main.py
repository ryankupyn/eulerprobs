numlist = []
with open('numbers.txt') as numberfile:
    numlist = [[int(i) for i in line.strip().split(' ')] for line in numberfile]
numlist.reverse()
for entry in range(1,100):
    for item in range(0, len(numlist[entry])):
        numlist[entry][item] += max(numlist[entry - 1][item],numlist[entry - 1][item + 1])
print(numlist[99])
