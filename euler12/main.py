triangnum = 0
adder = 1
divisors = 0
while divisors < 500:
    divisors = 0
    triangnum += adder
    adder += 1
    for divider in range(1, triangnum/2):
        if triangnum % divider == 0:
            divisors += 1
    divisors += 1
    if divisors > 250:
        print(triangnum)
    if divisors >= 500:
        print triangnum
