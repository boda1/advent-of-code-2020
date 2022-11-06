docsToCheck = []
validPassports = 0
currentValue = ''
completePassport = ['eyr:', 'pid:', 'hcl:', 'byr:', 'iyr:', 'ecl:', 'hgt:', 'cid:']
C = []

with open('./input.txt') as f:
    passportLines = f.readlines()
    for line in passportLines:
        if line != '\n':
            # line = line.strip()
            line = line.replace('\n', ' ')
            currentValue += line
        else:
            docsToCheck.append(currentValue[:-1])
            currentValue = ''
    docsToCheck.append(currentValue)

print('Documents to be checked: ', docsToCheck[0].split(' '))

D = [len(doc.split(' ')) for doc in docsToCheck]

C = ['valid' if len(doc.split(' ')) == 8 or (len(doc.split(' ')) == 7 and 'cid:' not in doc) else 'invalid' for doc in docsToCheck]


for item in C:
    if item == 'valid':
        validPassports = validPassports + 1
    else:
        None

print("Number of valid passports: ", validPassports)

# remove items in current passport from complete list of items in complete passport
# check what remains in complete passport, valid passports are those with nothing or only 'cid' remaining
