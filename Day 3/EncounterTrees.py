inputFile = open("input", "r")
inputArray = inputFile.read().split("\n")
slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
total = 1

for slope in slopes:
    treesEncounter = 0
    pos = 0

    for i in range(0, len(inputArray)-1, slope[1]):
        line = inputArray[i]
        if pos != 0 and line[pos % len(line)] == "#":
            treesEncounter += 1
        pos += slope[0]

    print("Trees encounterd = %d" % (treesEncounter))
    total *= treesEncounter

print("Total = %d" % (total))

