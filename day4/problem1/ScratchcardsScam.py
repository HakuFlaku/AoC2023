import os

def main():
    print("Beginning execution...")
    inputFile = open(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'input.txt')), "r")

    totalCardValue = 0
    for card in inputFile:
        winningNums = card.split('|')[0].split(':')[1].strip().split(' ')
        while winningNums.__contains__(''):
            del winningNums[winningNums.index('')]

        ourNums = card.split('|')[1].strip().split(' ')
        while ourNums.__contains__(''):
            del ourNums[ourNums.index('')]

        print("Winning nums: ", winningNums)
        print("Our num: ", ourNums)

        cardValue = 0
        for num in ourNums:
            if winningNums.__contains__(num):
                if(cardValue == 0):
                    cardValue = 1
                else:
                    cardValue *= 2

        totalCardValue += cardValue

    print(totalCardValue)

    print("Finished execution.")

if __name__ == "__main__":
    main()