
expenseFile = open('./input.txt')
expenseContent = expenseFile.readlines()

for i in range(len(expenseContent)):
    for j in range(len(expenseContent)):
        if int(expenseContent[i]) + int(expenseContent[j]) == 2020:
            print(int(expenseContent[i]) * int(expenseContent[j]))


for i in range(len(expenseContent)):
    for j in range(len(expenseContent)):
        for k in range(len(expenseContent)):
            if int(expenseContent[i]) + int(expenseContent[j]) + int(expenseContent[k]) == 2020:
                print(int(expenseContent[i]) * int(expenseContent[j]) * int(expenseContent[k]))