import re

inputFile = open("input", "r")
passports = inputFile.read().split("\n\n")
completePassports = 0
validPassports = 0


def check_height(height: str) -> bool:
    h = re.compile("([0-9]+)([a-zA-Z]+)").match(height)

    if h == None:
        return False

    h = h.groups()

    if (h[1] == "cm" and 150 <= int(h[0]) <= 193 or
            h[1] == "in" and 59 <= int(h[0]) <= 76):
        return True

    return False


for passport in passports:
    fields = dict(map(lambda x: x.split(":"), passport.split()))
    isPresent = ("byr" in fields and
                 "iyr" in fields and
                 "eyr" in fields and
                 "hgt" in fields and
                 "hcl" in fields and
                 "ecl" in fields and
                 "pid" in fields)
    if isPresent:
        completePassports += 1
        if (1920 <= int(fields["byr"]) <= 2002 and
            2010 <= int(fields["iyr"]) <= 2020 and
            2020 <= int(fields["eyr"]) <= 2030 and
            check_height(fields["hgt"]) and
            re.search(r'^#(?:[0-9a-fA-F]{6})$', fields["hcl"]) and
            fields["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"] and
                len(fields["pid"]) == 9):
            validPassports += 1

print("Part1: Total complete passports = %d" % (completePassports))
print("Part2: Total valid passports = %d" % (validPassports))
