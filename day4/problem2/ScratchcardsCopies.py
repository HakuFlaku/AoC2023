import os

def main():
    print("Beginning execution...")
    inputFile = open(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'input.txt')), "r")

    cardMatches = {}

    for card in inputFile:
        id = int(card.split(':')[0].split('Card')[1].strip())

        winningNums = card.split('|')[0].split(':')[1].strip().split(' ')
        while winningNums.__contains__(''):
            del winningNums[winningNums.index('')]

        ourNums = card.split('|')[1].strip().split(' ')
        while ourNums.__contains__(''):
            del ourNums[ourNums.index('')]

        matchingNums = 0
        for num in ourNums:
            if winningNums.__contains__(num):
                matchingNums += 1

        cardMatches[id] = matchingNums

    print("Matches: ", cardMatches)

    cardCopies = {}
    for id, matches in cardMatches.items():
        print("Getting copies for id ", id)
        copies = 1
        if(cardCopies.__contains__(id)):
            copies += cardCopies[id]

        print("We have this many copies for this id ", copies)
        for i in range(matches):
            key = id + i + 1
            print("Adding copy to ", key)
            if(cardCopies.__contains__(key)):
                cardCopies[key] += 1 * copies
            else:
                cardCopies[key] = 1 * copies
    
    print("Copies: ", cardCopies)

    totalCardsWon = 0
    for id in cardMatches.keys():
        totalCardsWon += 1
        if(cardCopies.__contains__(id)):
            totalCardsWon += cardCopies[id]

    print(totalCardsWon)

    print("Finished execution.")

if __name__ == "__main__":
    main()