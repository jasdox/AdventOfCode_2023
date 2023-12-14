with open('input.txt', 'r') as file:
    lines = file.readlines()

totalSum = 0

lines = [s.split(":") for s in lines]

for i in range(len(lines)):  # For each line, separate all elements past game ID into an array
    lines[i][1] = lines[i][1].strip()
    lines[i][1] = lines[i][1].replace(";", " ")
    lines[i][1] = lines[i][1].replace(",", " ")
    lines[i][1] = lines[i][1].split()
    curGameID = int(lines[i][0].split()[1])

    minRed, minBlue, minGreen = 0, 0, 0

    for j in range(0, len(lines[i][1]), 2):  # From each second element in the line and one after, retrieve the next number and color
        curNum = int(lines[i][1][j])
        curColor = lines[i][1][j+1]

        match curColor:  # Determine color and update the minimum value of that color if the next number is greater than previous min
            case "red":
                if curNum > minRed:
                    minRed = curNum
            case "blue":
                if curNum > minBlue:
                    minBlue = curNum
            case "green":
                if curNum > minGreen:
                    minGreen = curNum

    totalSum += (minRed * minBlue * minGreen)  # Find power of current game and update sum

print("The sum of the power of each set: " + str(totalSum))

