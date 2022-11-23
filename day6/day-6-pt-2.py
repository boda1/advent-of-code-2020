import string

all_questions = list(string.ascii_lowercase)
all_group_answers = []
affirmative_answers = 0
everyone_answered = []
num_of_answers = 0

with open('input.txt') as f:
    current_value = ''
    current_value = []
    for line in f.readlines():
        if line != '\n':
            line = line.strip()
            current_value.append(line)
        else:
            all_group_answers.append(current_value)
            current_value = []
    all_group_answers.append(current_value)


for single_group_answers in all_group_answers:
    single_group_answers_string = ''
    num_of_people = len(single_group_answers)
    print("Number of people answering: ", num_of_people)

    for answer in single_group_answers:
        single_group_answers_string += answer
    print("string to check: ", single_group_answers_string)

    for char in all_questions:
        if single_group_answers_string.count(char) == num_of_people:
            everyone_answered.append(char)
        

print("Number of questions all answered 'yes':", len(everyone_answered))






