import re

inputFile = open("input", "r")
forms = inputFile.read().split("\n\n")
anyoneYes = 0
everyoneYes = 0

for form in forms:
    answers = form.split("\n")
    if len(answers) > 1:
        everyoneYes += len(set(answers[0]).intersection(*answers))
    else:
        everyoneYes += len(answers[0])
    anyoneYes += len(dict.fromkeys(form.replace('\n', '')))


print("Number of questions to which anyone answered 'yes' = %d." % (anyoneYes))
print("Number of questions to which everyone answered 'yes' = %d." % (everyoneYes))
