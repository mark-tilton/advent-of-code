
with open('report_repair_input.txt', mode='r') as f:
    nums = [int(line) for line in f.readlines()]

target = 2020

def get_pair():
    visited_nums = set()
    for num in nums:
        complement = target - num
        if complement in visited_nums:
            print(num)
            print(complement)
            print(num * complement)
            break
        visited_nums.add(num)

def get_triple():
    visited_nums = set()
    for num in nums:
        for other in visited_nums:
            pair_val = other + num
            if pair_val > target:
                continue
            complement = target - pair_val
            if complement in visited_nums:
                print(num)
                print(other)
                print(complement)
                print(num * other * complement)
                break
        visited_nums.add(num)

get_triple()
