DEBUG = False

def read_to_lines(path):
    with open(path, 'r') as f:
        return [x.strip() for x in f.readlines()]

def check_pos(world, pos_r, pos_c):
    if world[pos_r][pos_c] != '@':
        if DEBUG:
            print(f'Current position ({pos_r}, {pos_c}) is not an "@"')
        return False

    c = 0
    pos_to_check = [
        (pos_r - 1, pos_c - 1),
        (pos_r - 1, pos_c),
        (pos_r - 1, pos_c + 1),
        (pos_r, pos_c - 1),
        (pos_r, pos_c + 1),
        (pos_r + 1, pos_c - 1),
        (pos_r +1, pos_c),
        (pos_r +1, pos_c +1)
    ]
    for (row, col) in pos_to_check:
        if row >= 0 and col >= 0 and row < len(world) and col < len(world[row]) and world[row][col] == '@':
            c += 1
    if c < 4:
        if DEBUG:
            print(f'Current position ({pos_r}, {pos_c}) is surrounded by less than 4 rolls')
        return True

def replace_found_rolls_with_period(input, found_positions):
    for (r, c) in found_positions:
        s = input[r]
        s = s[:c] + '.' + s[c + 1:]
        input[r] = s
    return input


def solve_1(input):
    count = 0
    for (row_idx, row) in enumerate(input):
        for col_idx in range(len(row)):
            if DEBUG:
                print(f'Checking ({row_idx}, {col_idx}) - count={count}')
            if check_pos(input, row_idx, col_idx):
                count += 1
            if DEBUG:
                print(f'After Check of ({row_idx}, {col_idx}) - count={count}')
    return count

def solve_2(input):
    count = 0
    prev_input = None
    while input != prev_input:
        prev_input = input.copy()
        found_positions = []
        for (row_idx, row) in enumerate(input):
            for col_idx in range(len(row)):
                if DEBUG:
                    print(f'Checking ({row_idx}, {col_idx}) - count={count}')
                if check_pos(input, row_idx, col_idx):
                    found_positions.append((row_idx, col_idx))
                    count += 1
                if DEBUG:
                    print(f'After Check of ({row_idx}, {col_idx}) - count={count}')
        input = replace_found_rolls_with_period(input, found_positions)
        if DEBUG:
            print(f'input != prev_input is {input != prev_input}')
            print(prev_input)
            print(input)
    return count

if __name__ == '__main__':
    path = './input.txt'
    input = read_to_lines(path)
    print(f'Solution to problem 1: {solve_1(input)}')
    print(f'Solution to problem 2: {solve_2(input)}')
