import os
import re

numberDict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

def main():
    print("Beginning execution...")
    
    inputFile = open(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'input.txt')), "r")
    total = 0

    for line in inputFile:
        print("\n******* Processing line ********\n\n", line)

        nums = re.findall(r'(?=([1-9]|one|two|three|four|five|six|seven|eight|nine))', line)
        print("All numbers found, ", nums)
        print("Using ", nums[0], " and ", nums[-1], " in our calculation.")

        if(numberDict.__contains__(nums[0])):
            nums[0] = numberDict.get(nums[0])
        
        if(numberDict.__contains__(nums[-1])):
            nums[-1] = numberDict.get(nums[-1])

        print("After converting to numbers we have ", nums[0], " and ", nums[-1])
        total += int(nums[0] + nums[-1])

        print("\n******* Done line ********\n")

    inputFile.close()
    print("Final number: ", total)

    outputFile = open(os.path.abspath(os.path.join(os.path.dirname( __file__ ), "output.txt")), "w")
    outputFile.write("Total count: " + str(total))
    outputFile.close()
    print("Finished execution.")

if __name__ == "__main__":
    main()