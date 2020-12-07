# Note this solution is largely inspired from other solutions.
import re

with open("input") as f:
    rules = {
        re.match(r"^\w+ \w+", line).group(0): re.findall(r"(\d+) (\w+ \w+)", line)
        for line in f
    }


def contain_bag(color):
    for bag, content in rules.items():
        if any(innerBag[1] == color for innerBag in content):
            yield bag
            yield from contain_bag(bag)


def bags_required(color):
    total = 1
    for count, color in rules[color]:
        total += int(count) * bags_required(color)
    return total


print("%d bag colors can contain at least one shiny gold bag." %
      (len(set(contain_bag("shiny gold")))))
print("%d individual bags are required inside a single shiny gold bag." %
      (bags_required("shiny gold")))
