import csv
numlist = []
totalnum = 0
with open('/Users/ryankupyn/GitHub/eulerprobs/euler13/numbers.csv') as csvfile:
     numbox = csv.reader(csvfile, delimiter=',', quotechar='|')
     for row in numbox:
         numlist.append(row)
     for hop in numlist:
         totalnum += int(hop[0][0:15])
print(totalnum)
