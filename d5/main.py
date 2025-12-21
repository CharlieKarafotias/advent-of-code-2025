DEBUG = True

def read_to_lines(path):
    with open(path, 'r') as f:
        return [x.strip() for x in f.readlines()]

def solve_1(input):
    append_to_range = True
    ranges = []
    ingredients = []
    fresh_count = 0
    for e in input:
        if e == '':
            append_to_range = False
            continue
        if append_to_range:
            ranges.append(e)
        else:
            ingredients.append(e)
    if DEBUG:
        print(f'Ranges: {ranges}')
        print(f'Ingredients: {ingredients}')
    for i in ingredients:
        for s in ranges:
            (start, end) = s.split('-')
            if int(i) in range(int(start), int(end)+1):
                if DEBUG: 
                    print(f'Ingredient {i} in range {s}')
                fresh_count += 1
                break
    return fresh_count

def reduce_ranges(ranges):
    r_ranges = []
    for i in ranges:
        (s, e) = i.split('-')
        s = int(s)
        e = int(e)
        r_ranges.append([s, e])
    r_ranges = sorted(r_ranges)
    i = 0
    if DEBUG:
        print(f'Start of alg: {r_ranges}')
    while i < len(r_ranges):
        # check curr start and next start, if same then take higher end and drop the smaller end from r_ranges
        if i+1 < len(r_ranges) and r_ranges[i][0] == r_ranges[i+1][0]:
            if DEBUG:
                print(f'same curr_start and next_start. Take higher end number')
            if r_ranges[i][1] < r_ranges[i+1][1]:
                r_ranges[i][1] = r_ranges[i+1][1]
            # delete next row
            del r_ranges[i+1]
        # ELIF end of curr > start of next, then take next end and set as end to current AND delete next s/e from r_ranges
        elif i+1 < len(r_ranges) and r_ranges[i][1] > r_ranges[i+1][0]:
            if DEBUG:
                print(f'end of curr > start of next. Take next end and set as end of current')
            r_ranges[i][1] = r_ranges[i+1][1]
            del r_ranges[i+1]
        # ELSE end of curr < start of next, so leave as is
        else:
            i+= 1
        if DEBUG:
            print(f'Iteration {i} complete: {r_ranges}')
        
    return r_ranges

def solve_2(input):
    append_to_range = True
    ranges = []
    ingredients = []
    for e in input:
        if e == '':
            append_to_range = False
            continue
        if append_to_range:
            ranges.append(e)
        else:
            ingredients.append(e)
    reduce_r = reduce_ranges(ranges)
    if DEBUG:
        print(f'Ranges: {ranges}')
        print()
        print(f'Reduced Ranges: {reduce_r}')
        print(f'{len(ranges)} -> {len(reduce_r)}')
    c = 0
    for r in reduce_r:
        (s, e) = r

        c += len(range(s, e+1))
    return c

if __name__ == '__main__':
    path = './input.txt'
    input = read_to_lines(path)
    # print(f'Solution to problem 1: {solve_1(input)}')
    print(f'Solution to problem 2: {solve_2(input)}')
