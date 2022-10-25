passwordFile = open('./input.txt')
passwords = passwordFile.readlines()
validPasswords = 0


for i in range(len(passwords)):
    minCharacters = int(passwords[i].split(' ')[0].split('-')[0])
    maxCharacters = int(passwords[i].split(' ')[0].split('-')[1])
    requiredCharacter = passwords[i].split(' ')[1].replace(':', '')
    password = passwords[i].split(' ')[2]

    numOfReqCharacters = 0

    for j in range(len(password)):
        if password[j] == requiredCharacter:
            numOfReqCharacters = numOfReqCharacters + 1
        elif j == (len(password) - 1) and numOfReqCharacters >= minCharacters and numOfReqCharacters <= maxCharacters:
            validPasswords = validPasswords + 1
            print('Password: ', password, 'Required character: ', requiredCharacter, '# of req characters: ', numOfReqCharacters, 'Total of valid: ', validPasswords)