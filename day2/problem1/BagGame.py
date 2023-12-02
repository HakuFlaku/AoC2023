from operator import contains
import os

maxDict = {
    'red': 12,
    'green': 13,
    'blue': 14
}

def main():
    print("Beginning execution...")
    
    inputFile = open(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'input.txt')), "r")
    idsTotalValue = 0

    for line in inputFile:
        print("\n*********** LINE PROCESSING START ***********\n")
        print("Processing line: ", line)

        id = int(line.split(':')[0].split(' ')[1])
        print("Found line id to be: ", id)

        rounds = line.strip('\n').split(': ')[1].split('; ')
        print(rounds)

        gameMaxValues = getGameMaxValues(rounds)
        print("This games max values are: ", gameMaxValues)

        if(validGame(gameMaxValues)):
            idsTotalValue += id

        print("\n*********** LINE PROCESSING DONE ***********\n")

    print("Done processing")
    outputFile = open(os.path.abspath(os.path.join(os.path.dirname( __file__ ), 'output.txt')), "w")
    outputFile.write("Id sum value: " + str(idsTotalValue))



def validGame(game):
    valid = True

    print(game)
    for colour, count in game.items():
        if(maxDict[colour] < count):
            valid = False

    return valid

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