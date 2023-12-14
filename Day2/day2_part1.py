NUM_RED, NUM_GREEN, NUM_BLUE = 12, 13, 14
count = 0
possible = True

with open('input.txt', 'r') as file:
    lines = file.readlines()

lines = [s.split(":") for s in lines]

for i in range(len(lines)):  # For each line, separate the rounds into a list and retrieve the game ID
    lines[i][1] = lines[i][1].strip()
    lines[i][1] = lines[i][1].split(";")
    curGameID = int(lines[i][0].split()[1])

    for j in range(len(lines[i][1])):  # For each round in the game
        lines[i][1][j] = lines[i][1][j].split()

        for k in range(0, len(lines[i][1][j]), 2):  # Look at every second element in the round and the one after to retrieve the next number and color
            curNum = int(lines[i][1][j][k])
            curColor = lines[i][1][j][k + 1]
            curColor = curColor.strip(",")

            match curColor:  # Determine the color and check if that number of the color is possible and update possibility flag
                case "red":
                    if curNum > NUM_RED:
                        possible = False
                        break
                case "blue":
                    if curNum > NUM_BLUE:
                        possible = False
                        break
                case "green":
                    if curNum > NUM_GREEN:
                        possible = False
                        break
                case _:
                    print("Invalid input")
        else:
            continue
        break

    if possible:  # If nothing in the last game was impossible, update the count by game ID
        count += curGameID
    else:  # Reset possibility flag
        possible = True


print("Sum of ID's of possible games: " + str(count))
