import math

number_of_rows = 128
initial_rows_list = [i for i in range(number_of_rows)]
current_row_list = []
number_of_columns = 8
initial_columns_list = [i for i in range(number_of_columns)]
current_column_list = []
seat_ids_with_tickets = []
highest_seat_value = 0
my_seat = 0


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
        seat_ids_with_tickets.append(current_row_list[0] * 8 + current_column_list[0])


for value in seat_ids_with_tickets:
    if value > highest_seat_value:
        highest_seat_value = value

print("All seat with tickets: ", seat_ids_with_tickets)


# part 2: find the missing boarding pass to identify my seat

"""

Generate complete list of IDs for 128x8 seats
Compare with input list provided
Find the values present in complete list that are missing from input list

"""


all_seat_ids = [row * 8 + column for row in initial_rows_list for column in initial_columns_list]
missing_seats = [seat if seat not in seat_ids_with_tickets and seat + 1 in seat_ids_with_tickets and seat - 1 in seat_ids_with_tickets else None for seat in all_seat_ids]


for seat in missing_seats:
    if seat is not None:
        my_seat = seat

print("My seat number is: ", my_seat)


