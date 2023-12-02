import os
import re

inputFile = open(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'input.txt')), "r")
total = 0

for line in inputFile:
    print(line)

inputFile.close()
print("Final number: ", total)

outputFile = open("output.txt", "w")
outputFile.write("Total count: " + str(total))
outputFile.close()
