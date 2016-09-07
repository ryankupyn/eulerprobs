innum = 1
lennum = 0
a = 1
b = 0

while lennum < 1000:
    hold = a
    a += b
    b = hold
    lennum = len(str(a))
    print(a)
    innum += 1


print(lennum)
print(innum)
