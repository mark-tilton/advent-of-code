# The seat string can just be read as a binary number
def get_seat_row(boarding_pass):
    seat_id = 0
    for ci in range(7):
        c = boarding_pass[ci]
        p = 6 - ci
        seat_id += pow(2, p) * (1 if c == 'B' else 0)
    return seat_id

def get_seat_column(boarding_pass):
    seat_id = 0
    for ci in range(3):
        c = boarding_pass[ci+7]
        p = 2 - ci
        seat_id += pow(2, p) * (1 if c == 'R' else 0)
    return seat_id

def get_seat_id(boarding_pass):
    return get_seat_row(boarding_pass) * 8 + get_seat_column(boarding_pass)

with open(r'binary_boarding_input.txt', mode='r') as f:
    boarding_passes = f.readlines()
    seat_ids = [get_seat_id(boarding_pass) for boarding_pass in boarding_passes]
    rows = [get_seat_row(boarding_pass) for boarding_pass in boarding_passes]
    columns = [get_seat_column(boarding_pass) for boarding_pass in boarding_passes]

def get_max_id():
    return max(seat_ids)

def get_missing_id_sort():
    seat_ids.sort()
    prev_id = None
    for seat_id in seat_ids:
        if prev_id != None and seat_id - prev_id > 1:
            return prev_id + 1
        prev_id = seat_id

def get_missing_id_set():
    id_set = set(seat_ids)
    for seat_id in id_set:
        next_id = seat_id + 1
        if not next_id in id_set and (next_id + 1) in id_set:
            return next_id

from collections import Counter
def get_missing_id_counter():
    seated_rows = Counter(rows)
    seated_columns = Counter(columns)
    missing_row = seated_rows.most_common()[-1][0]
    missing_column = seated_columns.most_common()[-1][0]
    return missing_row * 8 + missing_column
    

print(f'Max seat ID: {get_max_id()}')
print(f'Your seat ID: {get_missing_id_sort()}')
print(f'Your seat ID: {get_missing_id_set()}')
print(f'Your seat ID: {get_missing_id_counter()}')

# Profile the missing functions:
import time
iterations = 20000

def profile(f):
    t0 = time.time()
    for i in range(iterations):
        f()
    return time.time() - t0

t_sort = profile(get_missing_id_sort)
t_set = profile(get_missing_id_set)
t_counter = profile(get_missing_id_counter)

print(f'Sort time: {t_sort}')
print(f'Set time: {t_set}')
print(f'Counter time: {t_counter}')