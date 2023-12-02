import os

def main():
    print("Beginning execution...")
    
    inputFile = open(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'input.txt')), "r")
    powerSum = 0

    for line in inputFile:
        print("\n*********** LINE PROCESSING START ***********\n")
        print("Processing line: ", line)

        rounds = line.strip('\n').split(': ')[1].split('; ')
        print(rounds)

        gameMaxValues = getGameMaxValues(rounds)
        print("This games max values are: ", gameMaxValues)

        gamePower = 1
        for value in gameMaxValues.values():
            gamePower *= value
        
        powerSum += gamePower
        print("\n*********** LINE PROCESSING DONE ***********\n")

    print("Done processing")
    outputFile = open(os.path.abspath(os.path.join(os.path.dirname( __file__ ), 'output.txt')), "w")
    outputFile.write("Sum of each games 'power': " + str(powerSum))

def getGameMaxValues(game):
    gameMaxValues = {}
    for round in game:
        for pair in round.split(', '):
            value, key = pair.split(' ')
            value = int(value)

            if key in gameMaxValues:
                if(gameMaxValues[key] < value):
                    gameMaxValues[key] = value
            else:
                gameMaxValues[key] = value
    return gameMaxValues

if __name__ == "__main__":
    main()