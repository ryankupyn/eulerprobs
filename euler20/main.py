finalnum = 1
addnum = 0
for num in range(1,100):
    finalnum *= num
numchar = str(finalnum)
for numlet in numchar:
    addnum += int(numlet)

print(addnum)
