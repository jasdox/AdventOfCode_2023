with open('input.txt', 'r') as file:
    lines = file.readlines()

lines = [s.strip() for s in lines]

first = []
last = []
sum = 0

for i in range(len(lines)):  # Iterate over each line
    for j in range(len(lines[i])):  # Iterate over this line from left to right
        if lines[i][j].isdigit():  # If a number is found, add to the list of first numbers and stop searching this line
            first.append(lines[i][j])
            break;

    for j in reversed(range(len(lines[i]))):  # Iterate over this line from right to left
        if lines[i][j].isdigit():  # If a number is found, add to the list of last numbers and stop searching this line
            last.append(lines[i][j])
            break;

for i in range(len(first)):  # Combine the first and last number arrays at each index and sum all combinations
    sum += int(first[i] + last[i])

print("Sum of all calibration values: " + str(sum))
