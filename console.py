
from rovers import Rover, Plateau
from sys import argv

def readInput(inputfile):

    line = inputfile.readline() # first line from input
    plateau = Plateau(int(line[0]), int(line[2]))

    roverList = []  #list of lists [ [Rover(), orders] [Rover(), orders] ]

    while True:
        line1 = inputfile.readline()    # read liene where are rover coordinations
        orders = inputfile.readline()   # read line where are orders
        if not line1 or not orders:
            break
        rover = Rover(int(line1[0]), int(line1[2]), line1[4], plateau)  # line1 -> string e.g. '1 3 N'
        roverList.append([rover, orders])

    return roverList    #  list of lists [ [Rover(), orders] [Rover(), orders] ]

def executeRoversMoves(roverList):
    for list in roverList:  # list[0] -> Rover() ,  list[1] -> orders
        for i in list[1]:   # i -> next order from order String(list[1])

            if  i == "R":
                list[0].turnRight()

            elif i == "L":
                list[0].turnLeft()

            elif i == "M":
                list[0].move()

            else:
                # order not recognized, do nothing, go to next order
                pass

    return roverList

def returnPosition(roverList,outputfile):
        for list in roverList:
            outputfile.write(list[0].position())
            outputfile.write("\n")  # EOL

def printOutput(roverList):
    for list in roverList:
        print list[0].position()



#-----set names of files--------

inputname =  "input.txt"
outputname = "output.txt"

"""
# $ python console.py inputfile outputfile
script, inputfile, outputfile = argv
inputname =  inputfile
outputname = outputfile

"""

#--------main------------
input = open(inputname)

roverList = readInput(input)
input.close()
executeRoversMoves(roverList)

#---print rovers positions
printOutput(roverList)

#---write to file---
output = open(outputname, 'w')
output.truncate()
output = returnPosition(roverList,output)
