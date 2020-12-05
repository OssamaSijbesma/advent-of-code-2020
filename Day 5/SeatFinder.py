inputFile = open("input", "r")
seatIDs = []

for s in inputFile:
    s = (s.replace('F', '0')
         .replace('L', '0')
         .replace('B', '1')
         .replace('R', '1'))

    row = int(s[0:7], 2)
    column = int(s[7:10], 2)
    seatID = row * 8 + column
    seatIDs.append(seatID)

    print("row %d, column %d, seat ID %d." % (row, column, seatID))

l = min(seatIDs)
h = max(seatIDs)
print("Highest seat ID = %d." % (h))
print("My seat ID = %d." %
      (int((l + (h - l) / 2) * (len(seatIDs) + 1)) - sum(seatIDs)))
