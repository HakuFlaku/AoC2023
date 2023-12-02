import os
import re

inputFile = open(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'input.txt')), "r")
total = 0

for line in inputFile:
    print(line)
    nums = re.findall(r'[0-9]', line)
    print("Individual Numbers", nums)
    print("First Number", nums[0], ", Last Number", nums[-1])
    print("Concatenated number", nums[0] + nums[-1])
    total += int(nums[0] + nums[-1])
    print("Current total: ", total)

inputFile.close()
print("Final number: ", total)

outputFile = open("output.txt", "w")
outputFile.write("Total count: " + str(total))
outputFile.close()
