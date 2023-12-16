def check_adjacent(lines, i, j):  # This function checks every index in the grid surrounding the i, j parameters and
    flag = False  # returns a true flag if one is the '*' symbol. Additionally, it returns the index of that gear
    gearIndex = (0, 0)
    if lines[i][j - 1] == "*":
        gearIndex = (i, j-1)
        flag = True
    if lines[i][j + 1] == "*":
        gearIndex = (i, j + 1)
        flag = True
    if lines[i - 1][j] == "*":
        gearIndex = (i - 1, j)
        flag = True
    if lines[i - 1][j - 1] == "*":
        gearIndex = (i - 1, j - 1)
        flag = True
    if lines[i - 1][j + 1] == "*":
        gearIndex = (i - 1, j + 1)
        flag = True
    if lines[i + 1][j] == "*":
        gearIndex = (i + 1, j)
        flag = True
    if lines[i + 1][j - 1] == "*":
        gearIndex = (i + 1, j - 1)
        flag = True
    if lines[i + 1][j + 1] == "*":
        gearIndex = (i + 1, j + 1)
        flag = True
    return flag, gearIndex


with open('input.txt', 'r') as file:
    lines = file.readlines()

lines = [s.strip() for s in lines]
paddingLine = ["." for i in range(len(lines[0]))]  # This is used to create a boundary of '.' around the array so that
lines.insert(0, paddingLine)  # the check_adjacent function does not go out of bounds
lines.append(paddingLine)

for i in range(len(lines)):
    lines[i] = [char for char in lines[i]]
    lines[i].insert(0, ".")
    lines[i].append(".")

curNum = ""
curNumReal = False
totalSum = 0
gears = {}

for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j].isdigit():  # Checks to see if each character is a digit, if so add that digit to the ongoing num
            curNum += lines[i][j]  # string
            check, gearIndex = check_adjacent(lines, i, j)
            if check:   # If this digit has an adjacent '*', update the curNumReal to show that and update the
                curNumReal = True  # curGearIndex to be able to identify the gear relating to this number later
                curGearIndex = gearIndex

        else:
            if curNumReal: # Now that the ongoing number has ended, if this number was adjacent to a gear, see if that
                if gears.get(curGearIndex) is None:  # gear is already within the dictionary using the gear's index
                    gears[curGearIndex] = (int(curNum), 1)  # Either add this gear to the dictionary or update the
                else:  # dictionary to include the gear ratio and how many numbers are adjacent to the gear
                    gears[curGearIndex] = (gears[curGearIndex][0] * int(curNum), gears[curGearIndex][1] + 1)
            curNum = ""
            curNumReal = False

for index in gears:  # Iterated through the gear dictionary and sums the gear ratios of all gears that had exactly two
    if gears[index][1] == 2:  # numbers contributing to them
        totalSum += gears[index][0]

print("The sum of all part numbers: " + str(totalSum))
