import os

symbols = {}

def main():
    print("Beginning execution...")
        
    map = getMap()
    allMapNumbers = getNumbers(map)

    for rowNumbers in allMapNumbers:
        for number in rowNumbers:
            for numCoord in number.coords:
                key1 = DiKey(numCoord[0] - 1, numCoord[1] - 1)
                key2 = DiKey(numCoord[0] - 1, numCoord[1])
                key3 = DiKey(numCoord[0] - 1, numCoord[1] + 1)
                key4 = DiKey(numCoord[0], numCoord[1] - 1)
                key5 = DiKey(numCoord[0], numCoord[1] + 1)
                key6 = DiKey(numCoord[0] + 1, numCoord[1] - 1)
                key7 = DiKey(numCoord[0] + 1, numCoord[1])
                key8 = DiKey(numCoord[0] + 1, numCoord[1] + 1)

                if(key1 in symbols):
                    symbols[key1].append(number.number)
                    break
                if(key2 in symbols):
                    symbols[key2].append(number.number)
                    break
                if(key3 in symbols):
                    symbols[key3].append(number.number)
                    break
                if(key4 in symbols):
                    symbols[key4].append(number.number)
                    break
                if(key5 in symbols):
                    symbols[key5].append(number.number)
                    break
                if(key6 in symbols):
                    symbols[key6].append(number.number)
                    break
                if(key7 in symbols):
                    symbols[key7].append(number.number)
                    break
                if(key8 in symbols):
                    symbols[key8].append(number.number)
                    break

    partsTotal = 0

    for values in symbols.values():
        if len(values) == 2:
            partsTotal += values[0] * values[1]

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
    y = 0
    while line:
        map.append([])
        line = line.strip()

        for x in range(len(line)):
            if(line[x] == '*'):
                key = DiKey(y, x)
                symbols[key] = []

            map[y].append(line[x])

        y += 1
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

class DiKey:
    def __init__(self, L, R):
        self.L = L
        self.R = R
        
    def __repr__(self):
        return f"{self.L},{self.R}"

    def __eq__(self, other):
        return (self.L, self.R) == (other.L, other.R)

    def __hash__(self) -> int:
        return hash(str(self.L) + str(self.R))

if __name__ == "__main__":
    main()