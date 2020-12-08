
def old_validate():
    valid_count = 0

    with open('password_philosophy_input.txt', mode='r') as f:
        for line in f.readlines():
            letter_range, letter, password = line.split(' ')
            letter = letter[:-1]
            letter_count = 0
            for c in password:
                if c == letter:
                    letter_count += 1
            range_min, range_max = [int(val) for val in letter_range.split('-')]
            if letter_count >= range_min and letter_count <= range_max:
                valid_count += 1

    print(valid_count)

def new_validate():
    valid_count = 0

    with open('password_philosophy_input.txt', mode='r') as f:
        for line in f.readlines():
            letter_range, letter, password = line.split(' ')
            letter = letter[:-1]
            letter_indices = [int(val) - 1 for val in letter_range.split('-')]
            letter_matches = 0
            for i in letter_indices:
                if i >= len(password):
                    continue
                if password[i] == letter:
                    letter_matches += 1
            if letter_matches == 1:
                valid_count += 1

    print(valid_count)
    
new_validate()
