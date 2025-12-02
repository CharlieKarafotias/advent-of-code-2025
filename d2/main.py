def open_file(path):
    with open(path, 'r') as f:
        return f.read()

def parse(input):
    elems = input.split(',')
    lst = []
    for e in elems:
        s, e = e.split('-')
        lst.append((int(s.strip()), int(e.strip())))
    return lst

def solve_1():
    id_range_tuples = parse(open_file('./inputs/real.txt'))
    invalid_ids = []
    for (start, end) in id_range_tuples:
        for i in range(start, end+1):
            num_as_str = str(i)
            if num_as_str[0] == 0:
                assert True, "The ID should never start with 0"

            if (len(num_as_str) % 2 == 0):
                # check if both haves are same if so then identifed invalid id
                half = int(len(num_as_str) / 2)
                left = num_as_str[:half]
                right = num_as_str[half:]
                if left == right:
                    invalid_ids.append(i)

    return sum(invalid_ids)

def check_repeating_pattern_rec(original_str, pattern):
    len_pattern = len(pattern)
    len_str = len(original_str)
    if len_pattern == 0:
        return False

    if len_str % len_pattern == 0:
        # split n and check if all elements match pattern
        
        chunks = [original_str[i:i+len_pattern] for i in range(0, len_str, len_pattern)]
        if all(e == pattern for e in chunks):
            return True
    
    # if pattern not found then recursive check next pattern
    return check_repeating_pattern_rec(original_str, pattern[:-1])


def solve_2():
    id_range_tuples = parse(open_file('./inputs/real.txt'))
    invalid_ids = []
    for (start, end) in id_range_tuples:
        for i in range(start, end+1):
            num_as_str = str(i)
            if num_as_str[0] == 0:
                assert True, "The ID should never start with 0"
            
            half = int(len(num_as_str) / 2)
            left = num_as_str[:half]

            if check_repeating_pattern_rec(num_as_str, left):
                invalid_ids.append(i)

    return sum(invalid_ids)

print(f'Solution to 1: {solve_1()}')
print(f'Solution to 2: {solve_2()}')
