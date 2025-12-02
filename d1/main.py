def read_input(path):
    with open(path, 'r') as file:
        content = file.readlines()
        return content

def solve_1():
    lines = read_input('./inputs/1.txt')
    password = 0
    sum = 50 # position starts at 50
    for l in lines:
        num = int(l[1:])
        if l[0] == 'L':
            sum -= num
        else:
            sum += num
        if sum % 100 == 0:
            password += 1
    return password


# 99, R1 => 1
# 70, L70 => 1
# 0, R99 => 0
# 0, L100 => 1
# 0, L201 => 2
def calc_rotations(start_pos, rotation):
    # L if rotation < 0
    if rotation < 0:
        if start_pos == 0:
            start_pos = 100
        diff = start_pos - abs(rotation)
        if diff > 0:
            return 0
        elif diff == 0:
            return 1
        else:
            return 1 + (abs(diff) // 100)
    elif rotation == 0:
        return 0
    else:
        diff = start_pos + rotation
        if diff < 100:
            return 0
        elif diff == 100:
            return 1
        else:
            return diff // 100

def solve_2():
    lines = read_input('./inputs/1.txt')
    password = 0
    sum = 50 # position starts at 50
    for l in lines:
        print(f'{l[:-1]} - START')
        num = int(l[1:])
        if l[0] == 'L':
            password += calc_rotations(sum, -num)
            sum -= num
        else:
            password += calc_rotations(sum, num)
            sum += num
        sum %= 100
        print(f'{l[:-1]}: sum={sum} password={password}')
    return password


print(f'Solution to problem 1: {solve_1()}')
print(f'Solution to problem 2: {solve_2()}')
