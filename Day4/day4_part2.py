def processCards(card, cards):
    if card[1] == 0:
        return 1

    numCardCopies = 1
    for i in range(card[1]):
        numCardCopies += processCards(cards[card[0] + i], cards)

    return numCardCopies


with open('input.txt', 'r') as file:
    lines = file.readlines()

lines = [s.strip() for s in lines]
cards = []
totalCards = 0

for i in range(len(lines)):
    numMatches = 0
    cardScore = 0
    lines[i] = lines[i].replace("|", ":")
    lines[i] = lines[i].split(":")
    winningNums = lines[i][1].split()
    numbersYouHave = lines[i][2].split()

    for j in range(len(numbersYouHave)):
        if numbersYouHave[j] in winningNums:
            numMatches += 1

    cards.append((i + 1, numMatches))

for i in range(len(cards)):
    newCards = processCards(cards[i], cards)
    totalCards += newCards

print("Total cards: " + str(totalCards))
