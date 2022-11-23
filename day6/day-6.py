"""

separate groups with blank lines
turn group into string of characters
loop through all letters of alphabet and increment counter if alphabet value appears in input string

"""

import string

all_questions = list(string.ascii_lowercase)
group_answers = []
affirmative_answers = 0

with open('input.txt') as f:
    current_value = ''
    for line in f.readlines():
        if line != '\n':
            line = line.strip()
            current_value = current_value + line
        else:
            group_answers.append(current_value)
            current_value = ''
    group_answers.append(current_value)

print("List of all group's answers: ", group_answers)


for answers in group_answers:
    for letter in all_questions:
        if letter in answers:
            affirmative_answers += 1

print("Number of positive answers: ", affirmative_answers)