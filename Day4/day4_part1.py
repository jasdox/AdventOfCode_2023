with open('input.txt', 'r') as file:
    lines = file.readlines()

lines = [s.strip() for s in lines]
totalScore = 0

for i in range(len(lines)):
    numMatches = 0
    cardScore = 0
    lines[i] = lines[i].replace("|", ":")
    lines[i] = lines[i].split(":")
    winningNums = lines[i][1].split()
    numbersYouHave = lines[i][2].split()

    for i in range(len(numbersYouHave)):
        if numbersYouHave[i] in winningNums:
            numMatches += 1

    if numMatches >= 1:
        cardScore = 1
        for i in range(numMatches - 1):
            cardScore *= 2

    totalScore += cardScore

print("Total score is " + str(totalScore))
