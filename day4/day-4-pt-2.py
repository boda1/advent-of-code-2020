docsToCheck = []
validPassports = 0
currentValue = ''
completePassport = ['eyr:', 'pid:', 'hcl:', 'byr:', 'iyr:', 'ecl:', 'hgt:', 'cid:']
list_counting_valid_passports_1 = []
list_counting_valid_passports_2 = []
document_dictionaries = []
eye_colour = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
num_valid_keys = 0
num_valid_passports = 0

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

# Check whether each document has the required fields

C = ['valid' if len(doc.split(' ')) == 8 or (len(doc.split(' ')) == 7 and 'cid:' not in doc) else 'invalid' for doc in docsToCheck]

# Count number of valid documents

for item in C:
    if item == 'valid':
        validPassports = validPassports + 1
    else:
        None

print("Number of valid passports: ", validPassports)

# part 2, validating document the values of the fields in each document

documentLists = [list(doc.split(' ')) for doc in docsToCheck]


def convert(lst):
    # convert list to dictionary
    res_dict = {str(doc.split(' ')[j].split(':')[0]): str(doc.split(' ')[j].split(':')[1]) for doc in lst for j in range(len(doc.split(' ')))}
    return res_dict


for i in range(len(documentLists)):
    document_dictionaries.append(convert(documentLists[i]))


for document in document_dictionaries:
    num_valid_keys = 0
    for key, value in document.items():
        if key == 'byr':
            if 2002 >= int(value) >= 1920:
                num_valid_keys += 1
                print(value, num_valid_keys, "byr valid")
        elif key == 'iyr':
            if 2020 >= int(value) >= 2010:
                num_valid_keys += 1
                print(value, num_valid_keys, "iyr valid")
        elif key == 'eyr':
            if 2030 >= int(value) >= 2020:
                num_valid_keys += 1
                print(value, num_valid_keys, "eyr valid")
        elif key == 'hgt':
            if value[-2:] == 'cm' and len(value) == 5 and 193 >= int(value[:3]) >= 150:
                num_valid_keys += 1
                print(value, num_valid_keys, "hgt cm valid")
            elif value[-2:] == 'in' and 76 >= int(value[:2]) >= 59:
                num_valid_keys += 1
                print(value, num_valid_keys, "hgt in valid")
        elif key == 'hcl':
            if value[0] == '#' and len(value) == 7 and value.split('#')[1].isalnum():
                num_valid_keys += 1
                print(value, num_valid_keys, "hcl valid")
        elif key == 'ecl':
            if value in eye_colour:
                num_valid_keys += 1
                print(value, num_valid_keys, "ecl valid")
        elif key == 'pid':
            if len(value) == 9:
                num_valid_keys += 1
                print(value, num_valid_keys, "pid valid")
    if num_valid_keys == 7:
        num_valid_passports += 1


print("number of valid passports: ", num_valid_passports)