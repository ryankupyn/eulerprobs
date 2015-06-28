import numpy
import csv
maxset = 0
numlist = []
with open('/Users/ryankupyn/GitHub/eulerprobs/euler11/numbers.txt') as csvfile:
     numbox = csv.reader(csvfile, delimiter=',', quotechar='|')
     for row in numbox:
         numlist.append(row)
print numlist
for line in range(0, 20):
    for col in range(0, 20):
        if line <= 16:
            if int(numlist[line][col])*int(numlist[line+1][col])*int(numlist[line+2][col])*int(numlist[line+3][col]) > maxset:
                maxset = int(numlist[line][col])*int(numlist[line+1][col])*int(numlist[line+2][col])*int(numlist[line+3][col])
        if col <= 16:
            if int(numlist[line][col])*int(numlist[line][col+1])*int(numlist[line][col+2])*int(numlist[line][col+3]) > maxset:
                maxset = int(numlist[line][col])*int(numlist[line][col+1])*int(numlist[line][col+2])*int(numlist[line][col+3])
        if line <= 16 and col <= 16:
            if int(numlist[line][col])*int(numlist[line+1][col+1])*int(numlist[line+2][col+2])*int(numlist[line+3][col+3]) > maxset:
                maxset = int(numlist[line][col])*int(numlist[line+1][col+1])*int(numlist[line+2][col+2])*int(numlist[line+3][col+3])
        if line <= 16 and col >= 3:
            if int(numlist[line][col])*int(numlist[line+1][col-1])*int(numlist[line+2][col-2])*int(numlist[line+3][col-3]) > maxset:
                maxset = int(numlist[line][col])*int(numlist[line+1][col-1])*int(numlist[line+2][col-2])*int(numlist[line+3][col-3])
print(maxset)
