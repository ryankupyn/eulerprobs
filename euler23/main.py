import abundantlistgenerator

abundantlist = abundantlistgenerator.abundantlister(28123)
notsumtotal = 0

for testnum in range(28123):
    abundantsum = 0
    for entry in abundantlist:
        opposite = testnum - entry
        if opposite in abundantlist:
            abundantsum = 1
            break
    if abundantsum == 0:
        notsumtotal += testnum
        print(testnum)
print(notsumtotal)
