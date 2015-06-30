maxnum = 0
maxsteps = 0
for startnum in range(0,1000001):
    testnum = startnum
    numsteps = 0
    while testnum > 1:
        if testnum % 2 == 0:
            testnum = testnum/2
        else:
            testnum = 3 * testnum + 1
        numsteps += 1
    print startnum
    if numsteps > maxsteps:
        maxnum = startnum
        maxsteps = numsteps
print maxnum
