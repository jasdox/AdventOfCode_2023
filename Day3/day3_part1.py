def check_adjacent(lines, i, j):  # This function checks every index in the grid surrounding the i, j parameters and
    if (not lines[i][j - 1].isdigit()) & (lines[i][j - 1] != "."):  # returns true if one is a symbol other than '.'
        return True
    if (not lines[i][j + 1].isdigit()) & (lines[i][j + 1] != "."):
        return True
    if (not lines[i - 1][j].isdigit()) & (lines[i - 1][j] != "."):
        return True
    if (not lines[i - 1][j - 1].isdigit()) & (lines[i - 1][j - 1] != "."):
        return True
    if (not lines[i - 1][j + 1].isdigit()) & (lines[i - 1][j + 1] != "."):
        return True
    if (not lines[i + 1][j].isdigit()) & (lines[i + 1][j] != "."):
        return True
    if (not lines[i + 1][j - 1].isdigit()) & (lines[i + 1][j - 1] != "."):
        return True
    if (not lines[i + 1][j + 1].isdigit()) & (lines[i + 1][j + 1] != "."):
        return True
    return False


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

for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j].isdigit():  # Checks to see if each character is a digit, if so add that digit to the ongoing num
            curNum += lines[i][j]  # string
            if check_adjacent(lines, i, j):  # If this digit has an adjacent symbol, update the curNumReal to show that
                curNumReal = True  # the ongoing number has an adjacent symbol to some digit in it
        else:
            if curNumReal:  # Now that the ongoing number has ended, update the totalSum if this number had an adjacency
                totalSum += int(curNum)  # and reset the ongoing number and it's curNumReal boolean
            curNum = ""
            curNumReal = False

print("The sum of all part numbers: " + str(totalSum))
