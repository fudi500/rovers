

from sys import argv
from rovers import Rover

script, inputfile, outputfile = argv

input = open(inputfile)
input.readline()
roverList = []  #list of lists [Rover, orders]

while True:
    line1 = input.readline()
    orders = input.readline()
    if not line1 or not orders:
        break
    rover = Rover(int(line1[0]), int(line1[2]), line1[4])
    roverList.append([rover, orders])

txt.close()

output = open(outputfile, 'w')
output.truncate()

for list in roverList:
    for i in list[1]:
        if i == "L" or i == "R":
            list[0].turn(i)
        if i == "M":
            list[0].move()
    output.write(list[0].position())
    output.write("\n")

output.close()
