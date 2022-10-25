passwordFile = open('./input.txt')
passwords = passwordFile.readlines()
validPasswords = 0


for i in range(len(passwords)):
    positionOne = int(passwords[i].split(' ')[0].split('-')[0]) - 1
    positionTwo = int(passwords[i].split(' ')[0].split('-')[1]) - 1
    requiredCharacter = passwords[i].split(' ')[1].replace(':', '')
    charactersToCheck = [0, 0]
    password = passwords[i].split(' ')[2]

    numOfReqCharacters = 0

    for j in range(len(password)):
        if j == positionOne:
            charactersToCheck[0] = password[j]
        elif j == positionTwo:
            charactersToCheck[1] = password[j]
            print(charactersToCheck)

    if charactersToCheck[0] == requiredCharacter and charactersToCheck[1] != requiredCharacter:
        validPasswords += 1
    elif charactersToCheck[0] != requiredCharacter and charactersToCheck[1] == requiredCharacter:
        validPasswords += 1

    print('Number of valid passwords: ', validPasswords)

