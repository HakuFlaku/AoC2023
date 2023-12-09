import os
import string

symbolCoords = []

def main():
    print("Beginning execution...")
        
    map = getMap()
    print(map)

    allMapNumbers = getNumbers(map)
    print(allMapNumbers)

    partsTotal = 0
    for rowNumbers in allMapNumbers:
        for number in rowNumbers:
            for numCoord in number.coords:
                if(symbolCoords.__contains__([numCoord[0] - 1, numCoord[1] - 1]) or 
                    symbolCoords.__contains__([numCoord[0] - 1, numCoord[1]]) or
                    symbolCoords.__contains__([numCoord[0] - 1, numCoord[1] + 1]) or
                    symbolCoords.__contains__([numCoord[0], numCoord[1] - 1]) or
                    symbolCoords.__contains__([numCoord[0], numCoord[1] + 1]) or
                    symbolCoords.__contains__([numCoord[0] + 1, numCoord[1] - 1]) or
                    symbolCoords.__contains__([numCoord[0] + 1, numCoord[1]]) or
                    symbolCoords.__contains__([numCoord[0] + 1, numCoord[1] + 1])
                ):
                    print("Got one!")
                    print("Number retrieved is ", number.number)
                    partsTotal += number.number
                    break
    
    print(partsTotal)

    print("Finished execution.")

def getNumbers(map):
    toReturn = []

    for y in range(len(map)):
        row = map[y]

        rowNums = []
        isSameNumber = False
        for x in range(len(row)):
            col = row[x]
            if col.isnumeric() and not isSameNumber:
                newValue = Value(int(col), [[y, x]])
                rowNums.append(newValue)
                isSameNumber = True
            elif col.isnumeric() and isSameNumber:
                rowNums[-1].number = rowNums[-1].number * 10 + int(col)
                rowNums[-1].coords.append([y, x])
            elif not col.isnumeric():
                isSameNumber = False
        
        if rowNums:
            toReturn.append(rowNums)
    
    return toReturn

def getMap():
    inputFile = open(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'input.txt')), "r")
    map = []
    
    line = inputFile.readline()
    x = 0
    while line:
        map.append([])
        line = line.strip()

        for y in range(len(line)):
            if(line[y] != '.' and string.punctuation.__contains__(line[y])):
                symbolCoords.append([x, y])

            map[x].append(line[y])

        x += 1
        line = inputFile.readline()
    
    return map

class Value:
    def __init__(self, number, coords):
        self.number = number
        self.coords = coords

    def __str__(self):
        return "Number: " + str(self.number) + " coords: " + str(self.coords)
        
    def __repr__(self):
        return "Number: " + str(self.number) + " coords: " + str(self.coords)


if __name__ == "__main__":
    main()