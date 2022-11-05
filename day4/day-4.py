docsToCheck = []
validPassports = 0
currentValue = ''
completePassport = ['eyr:', 'pid:', 'hcl:', 'byr:', 'iyr:', 'ecl:', 'hgt:', 'cid:']
C = []

with open('./input.txt') as f:
    passportLines = f.readlines()
    for line in passportLines:
        if line != '\n':
            line = line.replace('\n', ' ')
            currentValue += line
        else:
            docsToCheck.append(currentValue)
            currentValue = ''
    docsToCheck.append(currentValue)

# print('docs to check: ', docsToCheck)

# docsToCheckNoSpaces = [print(doc.split(' ')) for doc in docsToCheck]

# print('Documents to be checked: ', docsToCheck[0].split(' '))

D = [len(doc.split(' ')) for doc in docsToCheck]

C = [(doc, 'valid') if len(doc.split(' ')) == 9 or (len(doc.split(' ')) == 8 and 'cid:' not in doc) else (doc, 'invalid') for doc in docsToCheck]


for item in C:
    if item[1] == 'valid':
        validPassports = validPassports + 1
    else:
        None

print(C)
print(len(docsToCheck))
print(validPassports)

# remove items in current passport from complete list of items in complete passport
# check what remains in complete passport, valid passports are those with nothing or only 'cid' remaining
