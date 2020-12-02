inputFile = open("input", "r")
countP1 = 0
countP2 = 0

for s in inputFile:
    s = s.replace('-', ' ')
    s = s.replace(':', '')
    s = s.replace('\n', '')    
    s = s.split(" ")

    occurrencesP1 = s[3].count(s[2])
    if int(s[0]) <= occurrencesP1 and int(s[1]) >= occurrencesP1 :
        countP1 += 1

    occurrencesP2 = 0

    if s[3][int(s[0]) - 1] == s[2] :
        occurrencesP2 += 1

    if s[3][int(s[1]) - 1] == s[2] :
        occurrencesP2 += 1
    
    if occurrencesP2 == 1 :
        countP2 += 1

print("Part1: Total valid passwords = %d" % (countP1))
print("Part2: Total valid passwords = %d" % (countP2))
