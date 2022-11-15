import math

number_of_rows = 128
initial_rows_list = [i for i in range(number_of_rows)]
current_row_list = []

number_of_columns = 8
initial_columns_list = [i for i in range(number_of_columns)]
current_column_list = []

seat_id = []

highest_seat_value = 0

print(initial_rows_list)
print(initial_columns_list)


with open('./input.txt') as f:
    for line in f.readlines():
        line = line.strip()
        current_row_list = initial_rows_list
        current_column_list = initial_columns_list
        for char in line:
            if char == 'F':
                current_row_list = current_row_list[:len(current_row_list)//2]
            elif char == 'B':
                current_row_list = current_row_list[len(current_row_list)//2:]
            elif char == 'L':
                current_column_list = current_column_list[:len(current_column_list)//2]
            elif char == 'R':
                current_column_list = current_column_list[len(current_column_list)//2:]
        seat_id.append(current_row_list[0] * 8 + current_column_list[0])


for value in seat_id:
    if value > highest_seat_value:
        highest_seat_value = value

print("Highest seat ID is: ", highest_seat_value)